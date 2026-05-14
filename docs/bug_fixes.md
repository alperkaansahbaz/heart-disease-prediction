# Karşılaşılan Sorunlar ve Çözümler

## UCI Heart Disease Dataset Etiket Paradoksu

### Problem

Proje Sprint 4 ve sonrasında, sistemin **klinik beklentilere ters** sonuçlar ürettiği tespit edildi:

- 26 yaşında, tüm değerleri normal bir kadın → **%100 Hasta** olarak değerlendirildi
- Klinik olarak yüksek riskli bir profil → **Sağlıklı** olarak değerlendirilebiliyordu

### Kök Neden Analizi

UCI Heart Disease Dataset'in **standart konvansiyondan farklı** etiket şeması olduğu tespit edildi:
Bu durum şu veri ile doğrulandı:

| Target | Yaş Ortalaması | Yaş Aralığı |
|--------|----------------|-------------|
| target=0 | 56.6 (yaşlı) | 35-77 |
| target=1 | 52.5 (genç) | 29-76 |

Yaşlı bireylerin "target=0" grubunda olması, bu grubun **hasta** olduğunu gösterir.

### Çözüm

`prediction_service.py` içinde **label inversion** uygulandı:

```python
# Modelden ham tahmin al
raw_prediction = self.model.predict(X_scaled)[0]
raw_proba = self.model.predict_proba(X_scaled)[0]

# Dataset'e gore ters cevir
prediction = 1 - raw_prediction        # 0 -> 1, 1 -> 0
probability = raw_proba[0]              # Class 0 (dataset'te Hasta)
```

Bu sayede:
- Dış arayüzde **1=Hasta, 0=Saglikli** standart konvansiyonu korundu
- Model çıktısı klinik beklentilerle uyumlu hale geldi

### Doğrulama

3 farklı profil ile test edildi:

| Profil | Beklenen | Sonuç |
|--------|----------|-------|
| 26 yaş, normal değerler | Sağlıklı | ✅ Sağlıklı (%0) |
| 70 yaş, kötü değerler | Hasta | ✅ Hasta (%100) |
| 52 yaş, karışık değerler | Orta | ✅ Orta (%60) |

### Akademik Değer

Bu sorun, gerçek dünya ML projelerinde **dataset bias** ve **labeling inconsistency**'nin önemini vurgulamaktadır. UCI Heart Disease dataset'in birçok farklı versiyonu mevcut olup, etiket konvansiyonları arasında farklılıklar olabilmektedir.

### Ders

- ✅ Modelin **klinik mantığa uygun** çıktı ürettiğinin **manuel olarak doğrulanması** önemlidir
- ✅ Birim testler her zaman semantic doğruluğu yakalayamaz
- ✅ Dataset'in **dökümanını** detaylı incelemek gerekir
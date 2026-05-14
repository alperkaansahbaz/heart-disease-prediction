# Karşılaşılan Sorunlar ve Çözümler

Bu dokümanda proje geliştirme sürecinde karşılaşılan kritik sorunlar ve uygulanan çözümler detaylı olarak açıklanmaktadır.

---

## UCI Heart Disease Dataset Etiket Paradoksu

### Problem Tanımı

Proje Sprint 4 sonrası yapılan kullanıcı kabul testlerinde, sistemin **klinik beklentilere tamamen ters** sonuçlar ürettiği tespit edilmiştir.

**Örnek Senaryo:** 26 yaşında, tüm klinik değerleri normal aralıkta olan bir kadın hastaya ait veri girildiğinde, sistem **%100 olasılıkla "Hasta"** olarak tahmin yapmaktadır. Bu durum tıbbi olarak mantıksızdır ve sistemin güvenilirliğini sorgulatmaktadır.

### Tespit Süreci

Sorun, manuel klinik testler sırasında tespit edildi. Otomatik birim testler bu sorunu yakalayamadı çünkü testler **fonksiyonel doğruluğu** (return tipi, alan varlığı) test ediyordu, **semantik doğruluğu** değil.

### Kök Neden Analizi

Dataset analizi yapıldığında, UCI Heart Disease Dataset'in **standart ML konvansiyonundan farklı** bir etiket şeması kullandığı tespit edildi:
### Doğrulama Verisi

Hipotezi doğrulamak için target sınıflarının demografik özellikleri analiz edildi:

| Target Sınıfı | Yaş Ortalaması | Yaş Aralığı | Yorum |
|---------------|----------------|-------------|-------|
| target = 0    | 56.6           | 35-77       | Yaşlı popülasyon → **Hasta grubu** |
| target = 1    | 52.5           | 29-76       | Genç popülasyon → **Sağlıklı grubu** |

Klinik mantık gereği kalp hastalığı riski yaşla artar. Yaş ortalaması yüksek olan grubun "hasta" grubu olması gerekir. Bu, target=0'ın hasta grubu olduğunu kanıtlamaktadır.

### Uygulanan Çözüm

`app/services/prediction_service.py` dosyasında **label inversion** tekniği uygulanmıştır:

```python
# Modelden ham tahmin al
raw_prediction = self.model.predict(X_scaled)[0]
raw_proba = self.model.predict_proba(X_scaled)[0]

# Etiketleri standart konvansiyona çevir
prediction = 1 - raw_prediction   # 0 -> 1 (Hasta), 1 -> 0 (Sağlıklı)
probability = raw_proba[0]         # Class 0 olasılığı = Gerçek hasta olma olasılığı
```

### Doğrulama Testleri

Çözüm sonrası 3 farklı klinik profil ile sistem doğrulandı:

| Profil | Demografik | Klinik Beklenti | Sistem Çıktısı | Sonuç |
|--------|------------|-----------------|----------------|-------|
| Genç Sağlıklı | 26 yaş, normal değerler | Düşük Risk | Sağlıklı (%0) | ✅ |
| Yaşlı Hasta | 70 yaş, kötü değerler | Yüksek Risk | Hasta (%100) | ✅ |
| Orta Yaş Karışık | 52 yaş, karışık değerler | Orta Risk | Orta (%60) | ✅ |

Tüm testler klinik beklentilerle uyumlu sonuçlar üretmiştir.

### Akademik Değerlendirme

Bu sorun gerçek dünya ML projelerinde sıklıkla karşılaşılan **dataset bias** ve **etiket tutarsızlığı** problemlerinin bir örneğidir.

**Önemli Bulgular:**

1. **Dataset doğrulama kritiktir:** Sadece dökümana güvenmek yerine, etiketlerin demografik analizi ile doğrulanması gereklidir.

2. **Klinik domain bilgisi şarttır:** Saf istatistiksel doğruluk yeterli değildir. Sonuçlar **uzman alan bilgisi** ile karşılaştırılmalıdır.

3. **Manuel test önemlidir:** Otomatik testler her zaman semantik doğruluğu yakalayamaz.

4. **Iterative debugging:** Bug detection → root cause analysis → solution → verification döngüsü uygulanmalıdır.

### Çıkarılan Dersler

- ✅ ML modelleri **klinik mantığa uygun** çıktı üretmelidir
- ✅ Birim testler **semantik doğruluk** için yetersiz olabilir
- ✅ **Demografik dağılım analizi** etiket doğrulamasında etkilidir
- ✅ Production sistemler **manuel kabul testleri** ile mutlaka doğrulanmalıdır

---

## Diğer Karşılaşılan Sorunlar

### Python 3.14 - scikit-learn Uyumsuzluğu

Proje başlangıcında Python 3.14 ile scikit-learn 1.5.2 uyumsuzluğu nedeniyle Python 3.12.10'a geçilmiştir.

### VS Code __init__.py Karışıklığı

Aynı isimde 7 farklı `__init__.py` dosyası olduğundan, doğru dosyaya kod yazmak için terminal komutları (`code app/__init__.py`) tercih edilmiştir.

### Pytest conftest.py Yazım Hatası

Dosya adı yanlışlıkla `confest.py` olarak oluşturuldu. Bu, pytest'in fixture'ları bulamamasına neden oldu. Dosya silinip doğru isimle yeniden oluşturuldu.

### Notebook Kaydetme Sorunu

VS Code'da notebook hücreleri çalıştırılsa bile Ctrl+S yapılmadığında GitHub'a boş olarak yüklenmektedir. **Auto Save** ayarı açılarak bu sorun çözüldü.

---

## Sonuç

Bu sorunlar proje geliştirme sürecinin doğal bir parçasıdır ve her biri yazılım mühendisliği pratikleri için değerli öğrenme deneyimleri sağlamıştır. Tüm sorunlar sistematik **debug yaklaşımı** ile çözülmüş ve dokümante edilmiştir.
# Keşifsel Veri Analizi (EDA) Raporu

**Proje:** Klinik Özelliklere Dayalı Makine Öğrenmesi ile Kalp Hastalığı Risk Tahmini  
**Sprint:** Sprint 1 — Veri Analizi  
**Tarih:** 2026  
**Hazırlayanlar:** Alperen ARSLAN, Alper Kaan ŞAHBAZ  
**Veri Seti:** Heart Disease Dataset (1025 satır, 14 sütun)

---

## 1. Yönetici Özeti

Bu rapor, kalp hastalığı risk tahmini projesi için kullanılacak Heart Disease veri setinin keşifsel analizini içermektedir. Yapılan analizler sonucunda veri setinin **modellemeye hazır** olduğu, ancak **iki kritik ön işleme adımının** zorunlu olduğu tespit edilmiştir:

1. **Tekrar eden satırların temizlenmesi** (1025 satırın 723'ü duplicate)
2. **Aykırı değer (outlier) yönetimi** (özellikle `chol` ve `oldpeak` için)

Ayrıca veri setinin **sınıf dengesinin doğal olarak iyi** olduğu (%51-49) tespit edilmiş, böylece SMOTE gibi dengeleme tekniklerine ihtiyaç duyulmadığı sonucuna varılmıştır.

---

## 2. Veri Seti Genel Bilgileri

| Özellik | Değer |
|---------|-------|
| Satır sayısı | 1025 |
| Sütun sayısı | 14 (13 özellik + 1 hedef) |
| Eksik değer | **0** ✅ |
| **Tekrar eden satır** | **723 (%70.54)** 🚨 |
| Veri tipleri | 13 int + 1 float |
| Bellek | 112 KB |

### Sütunlar

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| age | Numerik | Yaş |
| sex | Binary | Cinsiyet (0=Kadın, 1=Erkek) |
| cp | Kategorik | Göğüs ağrısı tipi (0-3) |
| trestbps | Numerik | İstirahat kan basıncı |
| chol | Numerik | Serum kolesterol |
| fbs | Binary | Açlık kan şekeri >120 |
| restecg | Kategorik | Dinlenme EKG (0-2) |
| thalach | Numerik | Maks kalp atış hızı |
| exang | Binary | Egzersize bağlı anjina |
| oldpeak | Numerik | ST depresyonu |
| slope | Kategorik | ST eğimi (0-2) |
| ca | Numerik | Floroskopi damar sayısı |
| thal | Kategorik | Talasemi (0-3) |
| **target** | **Binary** | **Kalp hastalığı (1=Var, 0=Yok)** |

---

## 3. Hedef Değişken Analizi

| Sınıf | Sayı | Yüzde |
|-------|------|-------|
| Sağlıklı (0) | 499 | %48.68 |
| Hasta (1) | 526 | %51.32 |

**Sonuç:** Sınıf dengesi mükemmel; SMOTE veya class weighting gerekmemektedir.

📊 **Görsel:** `reports/figures/01_target_distribution.png`

---

## 4. Korelasyon Analizi (Pearson)

### Hedef ile Güçlü Korelasyonlu Değişkenler (|r| > 0.4)

| Değişken | Korelasyon | Yön |
|----------|-----------|-----|
| oldpeak | -0.438 | ST depresyonu yüksekse → hastalık |
| exang | -0.438 | Egzersize bağlı anjina → hastalık |
| cp | +0.435 | Göğüs ağrısı tipi (asemptomatik → hastalık) |
| thalach | +0.423 | Düşük max kalp hızı → hastalık |

### Orta Korelasyonlu Değişkenler (0.2 < |r| < 0.4)

| Değişken | Korelasyon |
|----------|-----------|
| ca | -0.382 |
| slope | +0.346 |
| thal | -0.338 |
| sex | -0.280 |
| age | -0.229 |

### Zayıf Korelasyonlu Değişkenler (|r| < 0.2)

| Değişken | Korelasyon | Not |
|----------|-----------|-----|
| trestbps | -0.139 | Şaşırtıcı düşük |
| restecg | +0.134 | - |
| chol | -0.100 | **Çok şaşırtıcı** — literatüre aykırı |
| fbs | -0.041 | Neredeyse ilişkisiz |

📊 **Görsel:** `reports/figures/02_correlation_heatmap.png`

---

## 5. Şaşırtıcı Bulgular ve Tartışma

### 5.1. Kolesterol Paradoksu

Tıbbi literatürde kolesterol seviyesinin kalp hastalığının en güçlü göstergelerinden biri olduğu kabul edilirken, bu veri setinde `chol` değişkeninin hedefle korelasyonu yalnızca **-0.10** olarak tespit edilmiştir. Bu durum şu nedenlerle açıklanabilir:

- **Tedavi etkisi:** Kalp hastalığı tanısı almış bireyler statin gibi kolesterol düşürücü ilaçlar kullanıyor olabilir.
- **Sample bias:** Veri toplama döneminde belirli bir yaş veya bölge grubu üzerinde yoğunlaşılmış olabilir.

### 5.2. Yaş Paradoksu

Sağlıklı bireylerin ortalama yaşı **56.57**, hasta bireylerin ortalama yaşı **52.41**'dir. Yani **hastalar, sağlıklılardan ortalama 4 yaş daha gençtir**. Bu paradoks şu hipotezlerle açıklanabilir:

- **Healthy survivor effect:** İleri yaşa kadar yaşayanlar genetik olarak daha sağlıklı bir alt küme olabilir.
- **Erken başlangıçlı kalp hastalıkları:** Genetik yatkınlığa bağlı kalp hastalıkları daha genç yaşlarda ortaya çıkabilir.
- **Sample bias:** Veri toplama merkezi genç hasta odaklı olabilir.

### 5.3. Cinsiyet Bulgusu

Veri setinin %30'u kadın, %70'i erkektir. Ancak çapraz analizde **kadınların %72.44'ünün hasta** olduğu, **erkeklerin ise %42.08'inin hasta** olduğu görülmüştür. Bu durum mutlak risk farkı değil, **sample bias** sonucudur:

> Kadınlar belirti gösterene kadar hastaneye gitmemekte, gittiklerinde ise durum daha ileri seviyede olmaktadır.

Bu bulgu, "kadınlarda kalp hastalığı erken belirti vermez" tezini doğrular niteliktedir.

### 5.4. Göğüs Ağrısı Tipi (CP) Paradoksu

| CP Tipi | Açıklama | Hastalık Oranı |
|---------|----------|----------------|
| 0 | Tipik anjina | %24.55 |
| 1 | Atipik anjina | **%80.24** |
| 2 | Anjina dışı ağrı | **%77.11** |
| 3 | Asemptomatik | **%66.23** |

Tipik anjina (klasik kalp ağrısı) gösteren bireylerde hastalık oranının düşük olması, bu bireylerin tedavi altında olduğunu, asemptomatik bireylerin ise teşhis edilmemiş "sessiz" hastalar olduğunu düşündürmektedir.

📊 **Görsel:** `reports/figures/05_chest_pain_analysis.png`

---

## 6. Aykırı Değer (Outlier) Analizi

IQR yöntemi ile yapılan analizde:

| Değişken | Outlier Sayısı | Yüzde |
|----------|----------------|-------|
| age | 0 | %0.00 |
| trestbps | 30 | %2.93 |
| chol | 16 | %1.56 |
| thalach | 4 | %0.39 |
| oldpeak | 7 | %0.68 |

**Toplam outlier oranı %5.56** olup veri setinin sağlıklılığına işaret etmektedir. Bu değerlerin **klinik gerçeklik** taşıyabileceği (örn. yüksek tansiyon hastaları) göz önünde bulundurularak **tamamen silmek yerine winsorization** önerilmektedir.

📊 **Görsel:** `reports/figures/06_numerical_boxplots.png`

---

## 7. Sonuç ve Sprint 2 İçin Stratejiler

### 7.1. Yapılacak Ön İşlemeler
- ✅ **Duplicate temizleme** (öncelikli)
- ✅ Outlier yönetimi (winsorization)
- ✅ Feature scaling (StandardScaler)
- ⚠️ Encoding gerekmez (tüm değişkenler sayısal)

### 7.2. Önerilen Modelleme Stratejisi
- En güçlü 4 değişken (oldpeak, exang, cp, thalach) modelin temel taşları
- **Boruta** ile feature selection yapılarak `fbs` gibi zayıf korelasyonlu değişkenler dışlanabilir
- Sınıf dengesi iyi olduğu için SMOTE gerekmez
- Hedef metrikler: Accuracy, F1-Score, ROC-AUC

### 7.3. Risk Faktörleri
- Duplicate'lerin temizlenmesinden sonra kalan ~302 satır küçük bir veri seti (overfitting riski)
- Cross-validation (5-fold) kullanımı zorunlu

---

## 8. Üretilen Görseller

Tüm grafikler `reports/figures/` altında:

1. `01_target_distribution.png`
2. `02_correlation_heatmap.png`
3. `03_age_distribution.png`
4. `04_gender_vs_disease.png`
5. `05_chest_pain_analysis.png`
6. `06_numerical_boxplots.png`
7. `07_scatter_and_fbs.png`

---

**Rapor Hazırlama Tarihi:** Sprint 1 sonu  
**Rapor Versiyonu:** 1.0
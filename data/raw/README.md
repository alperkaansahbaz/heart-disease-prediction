# Data Directory

Bu klasör veri setlerini içerir. Veri dosyaları **Git'e commit edilmez**.

## Yapı

```
data/
├── raw/          # Ham veri (orijinal CSV) - değiştirilmez
├── processed/    # Temizlenmiş, feature engineering uygulanmış veri
└── external/     # Dış kaynaklardan ek veriler (varsa)
```

## Veri Seti

**Heart Disease Dataset (UCI Machine Learning Repository)**

- **İndirme Linki:** https://archive.ics.uci.edu/dataset/45/heart+disease
- **Alternatif (Kaggle):** https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset
- **Dosya Adı:** `heart.csv`
- **Yerleştirme:** `data/raw/heart.csv`

## Özellikler (Features)

| # | Özellik | Açıklama | Tip |
|---|---------|----------|-----|
| 1 | age | Yaş | Numerik |
| 2 | sex | Cinsiyet (1=Erkek, 0=Kadın) | Kategorik |
| 3 | cp | Göğüs ağrısı tipi (0-3) | Kategorik |
| 4 | trestbps | İstirahat kan basıncı (mm Hg) | Numerik |
| 5 | chol | Serum kolesterol (mg/dl) | Numerik |
| 6 | fbs | Açlık kan şekeri > 120 mg/dl (1=Evet, 0=Hayır) | Binary |
| 7 | restecg | Dinlenme EKG sonuçları (0-2) | Kategorik |
| 8 | thalach | Maksimum kalp atış hızı | Numerik |
| 9 | exang | Egzersize bağlı anjina (1=Evet, 0=Hayır) | Binary |
| 10 | oldpeak | ST depresyonu | Numerik |
| 11 | slope | ST eğimi (0-2) | Kategorik |
| 12 | ca | Floroskopi ile renklendirilen damar sayısı (0-3) | Numerik |
| 13 | thal | Talasemi (0-3) | Kategorik |
| 14 | **target** | **Kalp hastalığı (1=Var, 0=Yok)** | **Hedef** |

## Notlar

- Ham veri asla doğrudan değiştirilmez (`raw/` salt-okunur kabul edilir).
- Tüm dönüşümler `src/data/` ve `src/features/` altında yapılır.
- İşlenmiş veri `processed/` altına kaydedilir.

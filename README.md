# 🫀 Heart Disease Prediction System

> Klinik özelliklere dayalı makine öğrenmesi ile kalp hastalığı risk tahmini

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Sistem Mimarisi](#-sistem-mimarisi)
- [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
- [Klasör Yapısı](#-klasör-yapısı)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Model Performansı](#-model-performansı)
- [Test](#-test)
- [Geliştirme Yol Haritası](#-geliştirme-yol-haritası)
- [Ekip](#-ekip)

---

## 🎯 Proje Hakkında

Bu proje, **OSTİM Teknik Üniversitesi Bilgisayar Mühendisliği** bölümü mezuniyet projesi olarak geliştirilmektedir. Amaç, bireylere ait klinik özellikleri (yaş, kolesterol, tansiyon, göğüs ağrısı tipi vb.) kullanarak makine öğrenmesi yöntemleriyle kalp hastalığı riskini tahmin eden bir **web tabanlı karar destek sistemi** geliştirmektir.

### Problem Tanımı

Kalp ve damar hastalıkları dünya genelinde ölüm nedenleri arasında ilk sırada yer almaktadır. Geleneksel risk skorlama yöntemleri (örn. Framingham) sınırlı sayıda değişken kullanır ve doğrusal yaklaşımlara dayanır. Bu proje, çok değişkenli klinik verilerden **ensemble learning** yöntemleriyle daha doğru tahmin yapan bir sistem önermektedir.

### Hedefler

- ✅ ≥%85 doğruluk oranına ulaşan bir ML modeli geliştirmek
- ✅ Kullanıcı dostu bir web arayüzü tasarlamak
- ✅ Model ve arayüzü entegre eden çalışan bir MVP üretmek
- ✅ Akademik standartlarda dokümantasyon ve test sağlamak

---

## 🏗️ Sistem Mimarisi

```
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│                  │      │                  │      │                  │
│   USER (Browser) │ ───► │  Flask Web App   │ ───► │   ML Model       │
│   HTML + CSS     │ ◄─── │  (Controller)    │ ◄─── │   (joblib .pkl)  │
│                  │      │                  │      │                  │
└──────────────────┘      └──────────────────┘      └──────────────────┘
       Frontend               Application Layer         ML Inference Layer
```

Detaylı mimari için → [docs/architecture.md](docs/architecture.md)

---

## 🛠️ Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| **Backend** | Python 3.10+, Flask 3.0 |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Machine Learning** | scikit-learn, XGBoost |
| **Veri İşleme** | pandas, NumPy |
| **Model Kaydı** | joblib |
| **Görselleştirme** | matplotlib, seaborn |
| **Test** | pytest, pytest-flask |
| **Versiyon Kontrol** | Git, GitHub |

---

## 📁 Klasör Yapısı

```
heart-disease-prediction/
├── data/              # Veri setleri (raw, processed)
├── models/            # Eğitilmiş modeller ve metrikler
├── src/               # ML pipeline (eğitim, feature engineering)
├── app/               # Flask web uygulaması
├── static/            # CSS, JS, görseller
├── templates/         # HTML şablonları
├── tests/             # Birim ve entegrasyon testleri
├── notebooks/         # Jupyter notebook'lar (EDA)
├── docs/              # Dokümantasyon
├── reports/           # Akademik rapor için grafikler
├── config.py          # Konfigürasyon
├── run.py             # Uygulama giriş noktası
└── requirements.txt   # Bağımlılıklar
```

---

## ⚙️ Kurulum

### Ön Gereksinimler

- Python 3.10 veya üstü
- pip
- Git

### Adımlar

```bash
# 1. Repo'yu klonla
git clone https://github.com/<kullanici-adi>/heart-disease-prediction.git
cd heart-disease-prediction

# 2. Sanal ortam oluştur
python -m venv venv

# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Veri setini indir (data/raw/ içine yerleştir)
# Heart Disease Dataset: https://archive.ics.uci.edu/dataset/45/heart+disease

# 5. Modeli eğit
python -m src.models.train_model

# 6. Uygulamayı başlat
python run.py
```

Uygulama varsayılan olarak `http://127.0.0.1:5000` adresinde çalışır.

---

## 💻 Kullanım

1. Tarayıcıda `http://127.0.0.1:5000` adresine gidin.
2. Klinik bilgilerinizi forma girin:
   - Yaş, cinsiyet, göğüs ağrısı tipi
   - Kan basıncı, kolesterol seviyesi
   - Açlık kan şekeri, EKG sonuçları
   - Maksimum kalp atış hızı, vb.
3. **"Risk Tahmini Yap"** butonuna tıklayın.
4. Sonucu ve risk skorunu görüntüleyin.

> ⚠️ **Tıbbi Sorumluluk Reddi:** Bu sistem akademik bir prototiptir ve tıbbi tanı amacıyla kullanılamaz.

---

## 📊 Model Performansı

> Bu bölüm model eğitimi tamamlandıktan sonra güncellenecektir.

| Model | Accuracy | F1-Score | ROC-AUC |
|-------|----------|----------|---------|
| Logistic Regression | TBD | TBD | TBD |
| KNN | TBD | TBD | TBD |
| SVM | TBD | TBD | TBD |
| Decision Tree | TBD | TBD | TBD |
| Random Forest | TBD | TBD | TBD |
| XGBoost | TBD | TBD | TBD |
| **Ensemble (Stacking)** | **TBD** | **TBD** | **TBD** |

---

## 🧪 Test

```bash
# Tüm testleri çalıştır
pytest

# Coverage raporu
pytest --cov=app --cov=src --cov-report=html
```

---

## 🗺️ Geliştirme Yol Haritası

- [x] Sprint 0: Proje altyapısı ve kurulum
- [ ] Sprint 1: Veri analizi ve EDA
- [ ] Sprint 2: Model eğitimi ve seçimi
- [ ] Sprint 3: Ensemble yöntemleri ve optimizasyon
- [ ] Sprint 4: Flask backend geliştirme
- [ ] Sprint 5: Frontend (HTML + Bootstrap)
- [ ] Sprint 6: Entegrasyon ve test
- [ ] Sprint 7: Dokümantasyon ve sunum

---

## 👥 Ekip

| İsim | Rol | GitHub |
|------|-----|--------|
| **Alperen ARSLAN** | ML Engineer & Backend Developer | [@kullanici](https://github.com/) |
| **Alper Kaan ŞAHBAZ** | Frontend Developer & Data Analyst | [@kullanici](https://github.com/) |

**Danışman:** Murad NAGHİYEV  
**Kurum:** OSTİM Teknik Üniversitesi - Bilgisayar Mühendisliği Bölümü

---

## 📜 Lisans

Bu proje akademik amaçlı geliştirilmiştir. Detaylar için `LICENSE` dosyasına bakınız.

---

## 📚 Kaynaklar

- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)


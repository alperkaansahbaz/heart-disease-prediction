# 🫀 Heart Disease Prediction System

> Klinik özelliklere dayalı makine öğrenmesi ile **kalp hastalığı risk tahmini** yapan, web tabanlı bir karar destek sistemi.

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-orange.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-5.3.3-purple.svg)
![License](https://img.shields.io/badge/license-Academic-yellow.svg)
![Tests](https://img.shields.io/badge/tests-56%20passed-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-76%25-brightgreen.svg)
![Accuracy](https://img.shields.io/badge/accuracy-86.89%25-success.svg)

---

## 📖 Proje Hakkında

Bu proje, **OSTİM Teknik Üniversitesi Bilgisayar Mühendisliği** bölümü bitirme tezi kapsamında geliştirilmiştir. **TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projeleri Destek Programı** kapsamında değerlendirilmektedir.

Sistem, 13 klinik özelliği (yaş, kan basıncı, kolesterol vb.) kullanarak bir kişinin **kalp hastalığı riskini** anlık olarak tahmin eder. Kullanıcı dostu bir web arayüzü ile herkes tarafından kullanılabilir.

### 🎯 Hedef

Yapay zeka tabanlı klinik karar destek sistemlerinin **erken teşhis** alanındaki potansiyelini araştırmak ve prototip bir uygulama geliştirmek.

---

## ✨ Özellikler

- 🤖 **9 ML modeli** karşılaştırıldı, en iyisi (KNN) seçildi
- 📊 **%86.89 doğruluk**, 0.91 ROC-AUC skoru
- 🎨 **Responsive web arayüz** (Bootstrap 5)
- 🌐 **REST API** desteği (JSON)
- ✅ **56 otomatik test**, %76 code coverage
- 🩺 **3 risk seviyesi**: Düşük, Orta, Yüksek
- 📋 **Klinik öneri sistemi**
- 🖨️ **Sonuç yazdırma** desteği

---

## 🏗️ Mimari
┌──────────────────────────────────────────────────┐
│  Frontend (Bootstrap 5 + Jinja2)                  │
│  ↓ HTTP                                           │
│  Flask Routes (Blueprints)                        │
│  ↓                                                │
│  Validators & Formatters                          │
│  ↓                                                │
│  PredictionService (Singleton)                    │
│  ↓                                                │
│  KNN Classifier + StandardScaler                  │
└──────────────────────────────────────────────────┘
### 🛠️ Teknoloji Stack

**Backend:** Python 3.12, Flask 3.0  
**ML:** scikit-learn 1.5.2, XGBoost 2.1.1, pandas 2.2.2  
**Frontend:** Bootstrap 5.3.3, Bootstrap Icons 1.11.3  
**Testing:** pytest 8.3.3, pytest-cov 5.0.0  
**Version Control:** Git, GitHub

---

## 🚀 Kurulum ve Çalıştırma

### Önkoşullar

- Python 3.12+
- pip

### Adımlar

1. **Repository'i klonlayın:**
```bash
   git clone https://github.com/alperkaansahbaz/heart-disease-prediction.git
   cd heart-disease-prediction
```

2. **Virtual environment oluşturun:**
```bash
   python -m venv venv
```

3. **Virtual environment'ı aktive edin:**
```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
```

4. **Bağımlılıkları yükleyin:**
```bash
   pip install -r requirements.txt
```

5. **Uygulamayı çalıştırın:**
```bash
   python run.py
```

6. **Tarayıcıda açın:**
http://127.0.0.1:5000
---

## 📡 API Kullanımı

### POST /api/predict

Tahmin yapan ana endpoint.

**İstek:**
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}
```

**Yanıt:**
```json
{
  "prediction": 0,
  "prediction_label": "Saglikli",
  "probability": 0.4,
  "probability_pct": "%40.0",
  "risk_level": "Orta",
  "recommendation": "Bir doktora başvurarak detaylı muayene yaptırmanız önerilir...",
  "disclaimer": "UYARI: Bu sistem bir tıbbi tanı aracı değildir..."
}
```

### Diğer Endpoint'ler

| Method | URL | Açıklama |
|--------|-----|----------|
| GET | `/` | Anasayfa |
| GET | `/about` | Proje hakkında |
| GET | `/predict` | Form sayfası |
| POST | `/predict` | Form submit (HTML) |
| GET | `/health` | Sağlık kontrolü |
| GET | `/api/info` | API alan bilgileri |
| POST | `/api/predict` | JSON API tahmin |

---

## 🤖 Model Performansı

### Karşılaştırma

| Model | Test Accuracy | Test ROC-AUC |
|-------|---------------|--------------|
| **KNN (Optimized)** ⭐ | **%86.89** | **0.9058** |
| Voting (Soft) | %81.97 | 0.9037 |
| Stacking | %83.61 | 0.9026 |
| Bagging | %83.61 | 0.8999 |
| Logistic Regression | %80.33 | 0.8810 |
| SVM | %80.33 | 0.8810 |
| Random Forest | %77.05 | 0.8582 |
| XGBoost | %73.77 | 0.8355 |
| Decision Tree | %70.49 | 0.7971 |

### Final Model (KNN)

```python
{
    'n_neighbors': 15,
    'metric': 'manhattan',
    'weights': 'uniform',
    'algorithm': 'auto'
}
```

### Veri Seti

- **Kaynak:** UCI Heart Disease Dataset
- **Boyut:** 1025 → 302 satır (duplicate temizliği)
- **Özellikler:** 13 klinik özellik
- **Sınıf Dağılımı:** Dengeli (%51 hasta, %49 sağlıklı)

---

## 🧪 Test

```bash
# Tüm testleri çalıştır
pytest tests/ -v

# Coverage raporu (terminal)
pytest tests/ --cov=app --cov-report=term-missing

# Coverage raporu (HTML)
pytest tests/ --cov=app --cov-report=html
```

### Test İstatistikleri

| Kategori | Test Sayısı |
|----------|-------------|
| Unit Tests | 41 |
| Integration Tests | 15 |
| **Toplam** | **56 PASSED** |
| **Coverage** | **%76** |

---

## 📁 Proje Yapısı
heart-disease-prediction/
├── app/                    # Flask uygulaması
│   ├── routes/             # URL endpoint'leri
│   ├── services/           # İş mantığı (model)
│   ├── utils/              # Yardımcı fonksiyonlar
│   └── init.py         # Application Factory
├── data/                   # Veri setleri
│   ├── raw/                # Ham veri
│   └── processed/          # Temiz veri
├── models/                 # Eğitilmiş modeller
│   ├── trained/            # .pkl dosyaları
│   └── metrics/            # Performans metrikleri
├── notebooks/              # Jupyter notebook'lar (EDA, modeling)
├── reports/figures/        # Görselleştirmeler
├── templates/              # HTML şablonları
├── static/                 # CSS, JS, görseller
├── tests/                  # pytest test dosyaları
│   ├── unit/               # Birim testler
│   └── integration/        # Entegrasyon testleri
├── docs/                   # Dokümantasyon
├── config.py               # Konfigürasyon
├── run.py                  # Giriş noktası
└── requirements.txt        # Python bağımlılıkları
---

## 👥 Ekip

| Rol | İsim |
|-----|------|
| **ML Engineer & Backend** | Alperen ARSLAN |
| **Frontend & Data Analyst** | Alper Kaan ŞAHBAZ |
| **Akademik Danışman** | Murad NAGHİYEV |

---

## 📚 Dokümantasyon

Detaylı dokümantasyon için `docs/` klasörüne bakın:

- `architecture.md` — Sistem mimarisi
- `eda_report.md` — Veri analizi raporu
- `sprint_plan.md` — Sprint planlaması
- `test_strategy.md` — Test stratejisi
- `visualization_plan.md` — Görselleştirme planı

---

## ⚠️ Tıbbi Sorumluluk Reddi

> **ÖNEMLİ:** Bu sistem **yalnızca akademik amaçlı bir prototiptir** ve hiçbir koşulda tıbbi tanı, tedavi veya klinik karar verme aracı olarak kullanılamaz. Sağlığınızla ilgili her türlü karar için mutlaka bir uzman hekime danışınız.

---

## 📝 Lisans

Bu proje akademik bir mezuniyet projesi olarak geliştirilmiştir.

---

## 🏛️ Akademik Kurum

**OSTİM Teknik Üniversitesi**  
Mühendislik Fakültesi · Bilgisayar Mühendisliği Bölümü  
Mezuniyet Projesi · 2025-2026

---

<p align="center">
  <strong>🫀 HeartCheck — Yapay Zeka Destekli Kalp Sağlığı Değerlendirmesi 🫀</strong>
</p>
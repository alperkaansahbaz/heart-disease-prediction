# Sistem Mimarisi (Architecture Document)

## 1. Mimari Yaklaşım

Bu proje **3-Tier (Üç Katmanlı) Mimari** üzerine kurulmuştur. Her katman birbirinden bağımsız geliştirilir, test edilir ve güncellenir.

```
┌───────────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                           │
│  (HTML + CSS + Bootstrap + Vanilla JS)                        │
│  - Form girişi, sonuç gösterimi, kullanıcı etkileşimi         │
└───────────────────────┬───────────────────────────────────────┘
                        │ HTTP Request/Response (JSON/HTML)
                        ▼
┌───────────────────────────────────────────────────────────────┐
│                  APPLICATION LAYER                            │
│  (Flask Web Framework)                                        │
│  - Routing, Form validation, Session management               │
│  - app/routes/  →  Controller (HTTP endpoints)                │
│  - app/services/ →  Business logic (PredictionService)        │
│  - app/utils/   →  Helpers (validators, formatters)           │
└───────────────────────┬───────────────────────────────────────┘
                        │ Function call
                        ▼
┌───────────────────────────────────────────────────────────────┐
│                  ML INFERENCE LAYER                           │
│  (scikit-learn + XGBoost)                                     │
│  - models/trained/best_model.pkl  →  Eğitilmiş model          │
│  - models/trained/scaler.pkl       →  Feature scaler          │
│  - src/models/predict.py           →  Tahmin fonksiyonu       │
└───────────────────────────────────────────────────────────────┘
```

## 2. Veri Akışı (Data Flow)

```
Kullanıcı → Form Doldurur
    │
    ▼
Frontend (HTML Form) → POST /predict
    │
    ▼
Flask Route (app/routes/prediction_routes.py)
    │
    ▼
Form Validator (app/utils/validators.py)
    │  ✓ Eksik alan kontrolü
    │  ✓ Tip kontrolü (int/float)
    │  ✓ Aralık kontrolü (örn: yaş 0-120)
    ▼
Prediction Service (app/services/prediction_service.py)
    │  ✓ Feature dictionary oluştur
    │  ✓ Sırayı modelin beklediği sıraya getir
    ▼
Model Loader (src/models/predict.py)
    │  ✓ Joblib ile model yükle (lazy loading + cache)
    │  ✓ Scaler ile özellikleri ölçeklendir
    │  ✓ model.predict() ve model.predict_proba()
    ▼
Sonuç JSON / HTML
    │  { "risk": "high", "probability": 0.87, "confidence": "%87" }
    ▼
Frontend → Sonuç Sayfası (templates/result.html)
```

## 3. ML Pipeline Mimarisi (Eğitim Süreci)

```
data/raw/heart.csv
    │
    ▼
[ src/data/load_data.py ]            ← Veri yükleme & validasyon
    │
    ▼
[ src/data/preprocess.py ]           ← Eksik değer, aykırı değer
    │
    ▼
[ src/features/build_features.py ]   ← Encoding, scaling, feature selection
    │
    ▼
data/processed/heart_processed.csv
    │
    ▼
[ src/models/train_model.py ]        ← Train/Test split, eğitim
    │  ├─ Logistic Regression
    │  ├─ KNN, SVM, Decision Tree
    │  ├─ Random Forest, XGBoost
    │  └─ Ensemble (Voting/Stacking)
    │
    ▼
[ src/models/evaluate_model.py ]     ← Accuracy, F1, ROC-AUC
    │
    ▼
models/trained/best_model.pkl  +  models/metrics/metrics.json
```

## 4. Tasarım Prensipleri

### 4.1. Separation of Concerns (SoC)
Her modülün tek bir sorumluluğu var:
- `routes/` → sadece HTTP işler
- `services/` → sadece iş mantığı
- `models/` → sadece ML

### 4.2. Single Responsibility Principle (SRP)
Her fonksiyon/sınıf tek bir iş yapar. Örn: `validate_age()` sadece yaş kontrolü yapar.

### 4.3. Dependency Inversion
`PredictionService` doğrudan model dosyasını yüklemez; `ModelLoader` arayüzünü kullanır. Bu sayede mock'larla test edilebilir.

### 4.4. Configuration over Hardcoding
Tüm yollar, sabitler `config.py` ve `.env` üzerinden yönetilir. Kod içinde hardcode yok.

### 4.5. Reproducibility
- `random_state=42` her yerde sabit
- `requirements.txt` sürümleri pinli
- Veri pipeline'ı deterministik

## 5. Güvenlik Notları

- **CSRF Protection:** Flask-WTF ile aktif
- **Input Validation:** Tüm form girişleri server-side doğrulanır
- **Secret Key:** `.env` üzerinden yönetilir, repo'da yok
- **Tıbbi Veri:** Hiçbir kullanıcı verisi diske yazılmaz (stateless)

## 6. Ölçeklenebilirlik (Gelecek Çalışma)

Mevcut tasarım monolit ama modüler. İlerideki geliştirmeler için:
- Model serving → FastAPI / TensorFlow Serving
- Caching → Redis
- Async predictions → Celery
- Database → PostgreSQL (kullanıcı geçmişi için)

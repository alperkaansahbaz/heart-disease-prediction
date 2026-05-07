# Test Stratejisi

## 🎯 Test Piramidi

```
              ┌─────────────────┐
              │   E2E / Manual  │   %10  (Az ama kritik)
              └─────────────────┘
            ┌─────────────────────┐
            │  Integration Tests  │   %30  (Flask + Model)
            └─────────────────────┘
        ┌──────────────────────────────┐
        │       Unit Tests             │   %60  (Hızlı, çok)
        └──────────────────────────────┘
```

## 📋 Test Kategorileri

### 1. Unit Tests (`tests/unit/`)
Tek fonksiyon/sınıf seviyesinde, hızlı, izole testler.

**Test edilecek modüller:**
- `validators.py` → input doğrulama
- `preprocess.py` → veri temizleme fonksiyonları
- `build_features.py` → encoding fonksiyonları
- `prediction_service.py` → tahmin pipeline'ı (mock ile)

### 2. Integration Tests (`tests/integration/`)
Birden fazla bileşenin birlikte çalışmasını test eder.

**Test edilecek senaryolar:**
- Flask route'u → Service → Model entegrasyonu
- Form gönderimi → Tahmin → Sonuç akışı
- Hatalı girdi → Error response

### 3. End-to-End / Manual Tests
Gerçek tarayıcıda kullanıcı senaryoları.

---

## 🧪 Test Senaryoları

### Senaryo 1: Form Validation (Pozitif)
**Girdi:** Tüm alanlar geçerli (yaş=55, kolesterol=240, ...)  
**Beklenen:** Tahmin sayfasına yönlendirme + sonuç gösterimi

### Senaryo 2: Form Validation (Negatif - Eksik Alan)
**Girdi:** Yaş alanı boş  
**Beklenen:** Hata mesajı, formdan ayrılmama

### Senaryo 3: Form Validation (Negatif - Geçersiz Tip)
**Girdi:** Yaş = "abc"  
**Beklenen:** "Yaş sayısal olmalı" hatası

### Senaryo 4: Form Validation (Sınır Değerler)
**Girdi:** Yaş = 0, Yaş = 150, Kolesterol = -10  
**Beklenen:** Aralık dışı hatası

### Senaryo 5: Yüksek Risk Tahmini
**Girdi:** Yaş=70, kolesterol=350, göğüs ağrısı=tipik anjina, exang=1, oldpeak=3.5  
**Beklenen:** "Yüksek risk" sonucu, olasılık > 0.5

### Senaryo 6: Düşük Risk Tahmini
**Girdi:** Yaş=30, kolesterol=180, göğüs ağrısı=asemptomatik, exang=0, oldpeak=0  
**Beklenen:** "Düşük risk" sonucu, olasılık < 0.5

### Senaryo 7: Model Yükleme Hatası
**Girdi:** Model dosyası silinmiş  
**Beklenen:** 500 hata sayfası, log'a yazma

### Senaryo 8: Beklenmedik HTTP Method
**Girdi:** GET /predict  
**Beklenen:** 405 Method Not Allowed veya yönlendirme

### Senaryo 9: SQL Injection / XSS Denemesi
**Girdi:** `<script>alert('xss')</script>` form alanına  
**Beklenen:** Escape edilmiş çıktı, kod çalışmaz

### Senaryo 10: Eş Zamanlı İstek (Concurrency)
**Girdi:** 10 paralel POST isteği  
**Beklenen:** Hepsi cevap dönmeli, race condition yok

### Senaryo 11: Responsive Tasarım
**Girdi:** Mobil (375px), Tablet (768px), Masaüstü (1920px)  
**Beklenen:** Layout her boyutta düzgün

### Senaryo 12: Tarayıcı Uyumluluğu
**Test edilecek:** Chrome, Firefox, Safari, Edge  
**Beklenen:** Tutarlı görünüm ve davranış

---

## 📊 Model Test Senaryoları

### Model Test 1: Reproducibility
Aynı veriyle eğitilen model her seferinde aynı sonucu vermeli (`random_state=42`).

### Model Test 2: Performance Threshold
- Accuracy ≥ %85
- F1-Score ≥ 0.80
- ROC-AUC ≥ 0.85

### Model Test 3: Cross-Validation
5-Fold CV'de standart sapma < %5 (overfitting göstergesi).

### Model Test 4: Feature Order Sensitivity
Feature sırası değiştirilirse sonuç değişmeli mi? (Defansif programlama testi)

### Model Test 5: Edge Case Predictions
- Tüm değerler minimum
- Tüm değerler maksimum
- Karışık değerler
→ Model çökmemeli, mantıklı sonuç vermeli

---

## 🛠️ Test Araçları

| Araç | Kullanım |
|------|----------|
| `pytest` | Test runner |
| `pytest-flask` | Flask test client |
| `pytest-cov` | Code coverage |
| `unittest.mock` | Mock objects |
| Lighthouse | Frontend performans/accessibility |
| Postman | Manual API testleri |

## 📈 Coverage Hedefleri

| Modül | Hedef Coverage |
|-------|----------------|
| `app/services/` | %90+ |
| `app/utils/` | %95+ |
| `src/models/` | %80+ |
| `src/features/` | %85+ |
| **Genel** | **%70+** |

## ⚙️ Çalıştırma

```bash
# Tüm testler
pytest

# Belirli kategori
pytest tests/unit/
pytest tests/integration/

# Coverage raporu (HTML)
pytest --cov=app --cov=src --cov-report=html
# Sonra: htmlcov/index.html aç

# Sadece başarısız olanları yeniden çalıştır
pytest --lf

# Verbose
pytest -v
```

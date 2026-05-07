# Sprint Planı ve Görev Dağılımı

## 📅 Genel Takvim (6 Ay)

| Sprint | Süre | Tarih Aralığı | Konu |
|--------|------|---------------|------|
| Sprint 0 | 1 hafta | Hazırlık | Proje Altyapısı (✅ tamamlandı) |
| Sprint 1 | 2 hafta | Hafta 2-3 | Veri Analizi & EDA |
| Sprint 2 | 2 hafta | Hafta 4-5 | Tekil Model Eğitimi |
| Sprint 3 | 2 hafta | Hafta 6-7 | Ensemble & Optimizasyon |
| Sprint 4 | 2 hafta | Hafta 8-9 | Flask Backend |
| Sprint 5 | 2 hafta | Hafta 10-11 | Frontend (HTML+Bootstrap) |
| Sprint 6 | 2 hafta | Hafta 12-13 | Entegrasyon & Test |
| Sprint 7 | 1 hafta | Hafta 14 | Dokümantasyon & Sunum |

---

## 👥 Görev Dağılımı

> İki kişilik takımda **uzmanlaşma** ve **çapraz inceleme (peer review)** prensibi.

### Alperen ARSLAN — ML Engineer & Backend Lead
**Birincil Sorumluluk:** Makine öğrenmesi pipeline'ı + Flask backend

- Veri ön işleme ve feature engineering
- Model seçimi, eğitim ve hiperparametre optimizasyonu
- Ensemble yöntemleri (bagging, boosting, stacking)
- Flask routing ve service katmanı
- Model serileştirme ve yükleme
- Backend testleri (pytest)

### Alper Kaan ŞAHBAZ — Frontend Lead & Data Analyst
**Birincil Sorumluluk:** Veri analizi + web arayüzü

- EDA (Exploratory Data Analysis) raporu
- Akademik rapor için görselleştirmeler
- HTML şablonları (Jinja2)
- Bootstrap ile responsive tasarım
- Form validasyonu (client-side JS)
- Kullanıcı deneyimi (UX) testleri
- Dokümantasyon ve README güncellemeleri

### 🤝 Ortak Sorumluluklar
- Code review (her PR çift kişi onayı ister)
- Sprint planlama ve retrospektif toplantılar
- Akademik rapor yazımı
- Final sunum hazırlığı

---

## 📋 Sprint Detayları

### ✅ Sprint 0 — Project Setup (TAMAMLANDI)
**Hedef:** Profesyonel proje altyapısı

- [x] Klasör yapısı oluşturma
- [x] requirements.txt
- [x] .gitignore, README, .env.example
- [x] Mimari dokümantasyon
- [x] Sprint planı

**Definition of Done:** GitHub'a ilk commit yapılabilir, klasör yapısı standart.

---

### Sprint 1 — Veri Analizi & EDA
**Hedef:** Veriyi tanımak ve modelleme stratejisi belirlemek

**Tasks:**
- [ ] T1.1 — UCI/Kaggle Heart Disease Dataset indir
- [ ] T1.2 — `notebooks/01_eda.ipynb` oluştur
- [ ] T1.3 — Eksik değer analizi
- [ ] T1.4 — Aykırı değer (outlier) tespiti
- [ ] T1.5 — Korelasyon matrisi
- [ ] T1.6 — Hedef değişken dağılımı (sınıf dengesi)
- [ ] T1.7 — Feature dağılım grafikleri
- [ ] T1.8 — EDA raporu yazılması

**Definition of Done:**
- Notebook çalıştırılabilir
- En az 8 grafik üretilmiş
- EDA raporu `docs/eda_report.md` altında

---

### Sprint 2 — Tekil Model Eğitimi
**Hedef:** Baseline modelleri eğitmek ve karşılaştırmak

**Tasks:**
- [ ] T2.1 — `src/data/load_data.py`
- [ ] T2.2 — `src/data/preprocess.py`
- [ ] T2.3 — `src/features/build_features.py`
- [ ] T2.4 — `src/models/train_model.py` — Logistic Regression
- [ ] T2.5 — KNN, SVM, Decision Tree eğitimi
- [ ] T2.6 — Random Forest, XGBoost eğitimi
- [ ] T2.7 — `src/models/evaluate_model.py` — Accuracy, F1, ROC-AUC
- [ ] T2.8 — Confusion matrix ve ROC eğrisi grafikleri

**Definition of Done:**
- 6 farklı model eğitilmiş
- Performans tablosu üretilmiş
- En iyi tekil model seçilmiş

---

### Sprint 3 — Ensemble & Hiperparametre Optimizasyonu
**Hedef:** Performansı %85+ doğruluğa çıkarmak

**Tasks:**
- [ ] T3.1 — Voting Classifier (hard & soft)
- [ ] T3.2 — Bagging Classifier
- [ ] T3.3 — Stacking Classifier
- [ ] T3.4 — GridSearchCV ile hiperparametre arama
- [ ] T3.5 — Cross-validation (5-fold)
- [ ] T3.6 — En iyi modeli `joblib` ile kaydet
- [ ] T3.7 — Metrikleri JSON olarak kaydet

**Definition of Done:**
- En az 1 ensemble model %85+ accuracy
- Model dosyası `models/trained/best_model.pkl`
- Karşılaştırma raporu

---

### Sprint 4 — Flask Backend
**Hedef:** API ve routing katmanını oluşturmak

**Tasks:**
- [ ] T4.1 — `app/__init__.py` (Application Factory)
- [ ] T4.2 — `config.py` (Config sınıfları)
- [ ] T4.3 — `run.py` (Entry point)
- [ ] T4.4 — `app/routes/main_routes.py` (anasayfa)
- [ ] T4.5 — `app/routes/prediction_routes.py` (/predict)
- [ ] T4.6 — `app/services/prediction_service.py`
- [ ] T4.7 — `app/utils/validators.py` (input validation)
- [ ] T4.8 — Error handlers (404, 500)

**Definition of Done:**
- `python run.py` ile uygulama açılıyor
- `/predict` endpoint'i POST ile çalışıyor (Postman)

---

### Sprint 5 — Frontend
**Hedef:** Kullanıcı arayüzü

**Tasks:**
- [ ] T5.1 — `templates/base.html` (layout)
- [ ] T5.2 — `templates/index.html` (anasayfa + tanıtım)
- [ ] T5.3 — `templates/predict.html` (form sayfası)
- [ ] T5.4 — `templates/result.html` (sonuç sayfası)
- [ ] T5.5 — `static/css/custom.css` (Bootstrap özelleştirme)
- [ ] T5.6 — `static/js/form_validation.js` (client-side)
- [ ] T5.7 — Responsive test (mobil/tablet/masaüstü)
- [ ] T5.8 — Erişilebilirlik (a11y) kontrolü

**Definition of Done:**
- Mobile-first tasarım
- Lighthouse accessibility skoru ≥ 90
- Tüm formlar çalışıyor

---

### Sprint 6 — Entegrasyon & Test
**Hedef:** End-to-end çalışan stabil MVP

**Tasks:**
- [ ] T6.1 — Backend ↔ Frontend entegrasyonu
- [ ] T6.2 — Unit testler (`tests/unit/`)
- [ ] T6.3 — Integration testler (`tests/integration/`)
- [ ] T6.4 — Edge case testleri
- [ ] T6.5 — Performance testi (response time)
- [ ] T6.6 — Bug fix turu
- [ ] T6.7 — Code coverage ≥ %70

**Definition of Done:**
- Tüm testler geçiyor
- Coverage raporu üretildi
- Manual smoke test başarılı

---

### Sprint 7 — Dokümantasyon & Sunum
**Hedef:** Akademik teslim hazırlığı

**Tasks:**
- [ ] T7.1 — README final güncellemesi
- [ ] T7.2 — Akademik rapor (PDF)
- [ ] T7.3 — Sunum (PowerPoint)
- [ ] T7.4 — Demo videosu (3-5 dakika)
- [ ] T7.5 — Poster (varsa)
- [ ] T7.6 — GitHub repo public yapılması

**Definition of Done:**
- Tüm dokümantasyon hazır
- Sunum prova edildi

---

## 🔄 Sprint Ritüelleri

| Ritüel | Süre | Sıklık |
|--------|------|--------|
| Sprint Planning | 1 saat | Sprint başında |
| Daily Standup | 15 dakika | Her gün (15:00) |
| Sprint Review | 30 dakika | Sprint sonu |
| Retrospektif | 30 dakika | Sprint sonu |

## 📌 Branch Stratejisi (Git Flow)

```
main           ← Sadece stabil sürümler (release)
  └─ develop   ← Aktif geliştirme branch'i
       ├─ feature/sprint1-eda
       ├─ feature/sprint2-knn-model
       ├─ feature/sprint4-flask-routing
       └─ bugfix/form-validation
```

**Kural:** Hiçbir kod doğrudan `main`'e push edilmez. Pull Request ve onay şart.

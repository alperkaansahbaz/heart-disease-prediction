# Analiz ve Görselleştirme Planı

Akademik rapor ve sunum için **Sprint 1 (EDA)** ve **Sprint 2 (Model)** aşamalarında üretilecek grafikler.

## 🎨 Görsel Standartları

- **Boyut:** 1200x800 px (yüksek çözünürlük rapor için)
- **Kayıt formatı:** PNG (rapor için), SVG (vektörel sunum için)
- **Renk paleti:** Tek tutarlı palet (örn: seaborn `colorblind` veya `viridis`)
- **Yazı tipi:** Arial / Helvetica (akademik standart)
- **Kayıt yeri:** `reports/figures/`

---

## 📊 EDA Aşaması Grafikleri (Sprint 1)

### G1. Hedef Değişken Dağılımı
**Tip:** Bar chart  
**Amaç:** Sınıf dengesini görmek (kalp hastası var/yok oranı)  
**Önemi:** Eğer dengesizlik varsa SMOTE/Class Weight gerekli  
**Dosya:** `target_distribution.png`

### G2. Yaş Dağılımı (Histogram + KDE)
**Tip:** Histogram + Kernel Density Estimate  
**Amaç:** Yaş aralığını ve dağılım şeklini anlamak  
**Bonus:** Hedefe göre renklendirme (hue=target)  
**Dosya:** `age_distribution.png`

### G3. Cinsiyete Göre Hastalık Oranı
**Tip:** Grouped bar chart  
**Amaç:** Cinsiyetin riskle ilişkisi  
**Dosya:** `gender_vs_disease.png`

### G4. Korelasyon Matrisi (Heatmap)
**Tip:** Heatmap  
**Amaç:** Tüm sayısal değişkenlerin birbirleriyle ilişkisi  
**Önemi:** Multicollinearity tespiti, feature selection için ipucu  
**Dosya:** `correlation_heatmap.png`

### G5. Boxplot — Tüm Sayısal Özellikler
**Tip:** Multi-panel boxplot  
**Amaç:** Aykırı değerleri (outlier) görselleştirmek  
**Dosya:** `numerical_boxplots.png`

### G6. Kolesterol vs Hastalık (Violin Plot)
**Tip:** Violin plot  
**Amaç:** Kolesterol seviyesinin hastalıkla ilişkisi  
**Dosya:** `cholesterol_violin.png`

### G7. Maksimum Kalp Atış Hızı vs Yaş (Scatter)
**Tip:** Scatter plot (hue=target)  
**Amaç:** İki sürekli değişkenin ilişkisi ve hedefe göre ayrışma  
**Dosya:** `thalach_vs_age.png`

### G8. Göğüs Ağrısı Tipi Dağılımı
**Tip:** Count plot (hue=target)  
**Amaç:** Hangi göğüs ağrısı tipi daha riskli  
**Dosya:** `chestpain_distribution.png`

### G9. Pair Plot (Üst Düzey Bakış)
**Tip:** Seaborn pairplot  
**Amaç:** Tüm sayısal değişkenler arası ikili ilişkiler  
**Dosya:** `pairplot.png`

### G10. Eksik Değer Haritası
**Tip:** Heatmap (boolean missing)  
**Amaç:** Eksik veri varsa görselleştirme  
**Dosya:** `missing_values.png`

---

## 🤖 Model Aşaması Grafikleri (Sprint 2-3)

### G11. Model Karşılaştırma (Bar Chart)
**Tip:** Grouped bar chart  
**Amaç:** Tüm modellerin Accuracy, F1, ROC-AUC karşılaştırması  
**Dosya:** `model_comparison.png`

### G12. Confusion Matrix
**Tip:** Heatmap  
**Amaç:** True/False Positive/Negative dağılımı  
**Adet:** Her model için 1 tane (en az en iyi 3 model)  
**Dosya:** `confusion_matrix_<model>.png`

### G13. ROC Eğrisi (Multi-model)
**Tip:** Line plot (her model bir çizgi)  
**Amaç:** Modellerin AUC karşılaştırması  
**Dosya:** `roc_curves.png`

### G14. Precision-Recall Eğrisi
**Tip:** Line plot  
**Amaç:** Dengesiz veri varsa daha bilgilendirici  
**Dosya:** `precision_recall.png`

### G15. Feature Importance (Random Forest / XGBoost)
**Tip:** Horizontal bar chart  
**Amaç:** Hangi özellikler model için en önemli  
**Dosya:** `feature_importance.png`

### G16. Learning Curve
**Tip:** Line plot (train vs validation accuracy)  
**Amaç:** Overfitting / underfitting tespiti  
**Dosya:** `learning_curve.png`

### G17. Cross-Validation Skorları (Box plot)
**Tip:** Boxplot (her model için 5 fold skoru)  
**Amaç:** Modelin kararlılığı (variance)  
**Dosya:** `cv_scores.png`

### G18. Hiperparametre Optimizasyon Heatmap
**Tip:** Heatmap (Grid Search sonuçları)  
**Amaç:** En iyi hiperparametre kombinasyonunu görmek  
**Dosya:** `hyperparameter_heatmap.png`

### G19. Ensemble vs Tekil Modeller
**Tip:** Bar chart  
**Amaç:** Ensemble'in tekil modellere üstünlüğünü göstermek  
**Dosya:** `ensemble_vs_single.png`

### G20. Threshold Analizi
**Tip:** Line plot (Precision/Recall vs threshold)  
**Amaç:** Tıbbi senaryoda threshold seçiminin önemi  
**Dosya:** `threshold_analysis.png`

---

## 📐 Sistem Tasarım Diyagramları

### D1. Sistem Mimarisi (3-Tier)
**Araç:** draw.io, Lucidchart, Mermaid  
**Format:** SVG / PNG  
**Dosya:** `system_architecture.svg`

### D2. Veri Akış Diyagramı (DFD)
Form → Validation → Service → Model → Response

### D3. ML Pipeline Diyagramı
Raw Data → Preprocessing → Feature Engineering → Training → Evaluation → Deployment

### D4. Use Case Diyagramı
Aktör (Kullanıcı) → Use Case'ler (Form Doldur, Sonuç Gör, Hakkında Oku)

### D5. Sequence Diyagramı
Tahmin işleminin zaman akışı

### D6. ER Diyagramı (gelecek için)
Mevcut projede DB yok ama gelecek geliştirme için planlanan şema

---

## 📑 Akademik Rapora Eklenecek Tablolar

| Tablo | İçerik |
|-------|--------|
| T1 | Veri seti özellikleri özeti |
| T2 | Eksik değer ve aykırı değer raporu |
| T3 | Tekil model performans karşılaştırma |
| T4 | Ensemble model performans karşılaştırma |
| T5 | En iyi modelin sınıflandırma raporu |
| T6 | Hiperparametre arama uzayı |
| T7 | Çalışma takvimi (gerçekleşen vs planlanan) |
| T8 | Test sonuçları özeti |

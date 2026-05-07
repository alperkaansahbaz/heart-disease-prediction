# `src/` — Machine Learning Pipeline

Bu klasör **veri bilimi** tarafıyla ilgili tüm kodları içerir. Web uygulamasından (`app/`) tamamen ayrıdır; tek başına çalıştırılabilir.

## Yapı

```
src/
├── data/             # Veri yükleme ve temel işleme
│   ├── load_data.py       # CSV oku, doğrula
│   └── preprocess.py      # Eksik değer, aykırı değer, temizleme
│
├── features/         # Feature engineering
│   ├── build_features.py  # Encoding, scaling, feature selection
│   └── transformers.py    # Custom sklearn transformer'lar
│
├── models/           # Model eğitimi ve değerlendirme
│   ├── train_model.py     # Tek model eğitimi
│   ├── train_ensemble.py  # Ensemble model eğitimi
│   ├── evaluate_model.py  # Metrikler ve raporlama
│   └── predict.py         # Yüklenmiş modelle tahmin
│
└── visualization/    # Grafikler
    ├── eda_plots.py       # EDA grafikleri
    └── model_plots.py     # Confusion matrix, ROC, vb.
```

## Çalıştırma Sırası (Pipeline)

```bash
# 1. Veriyi yükle ve önişle
python -m src.data.preprocess

# 2. Feature engineering
python -m src.features.build_features

# 3. Modeli eğit
python -m src.models.train_model

# 4. Ensemble eğit (opsiyonel ama kritik)
python -m src.models.train_ensemble

# 5. Değerlendirme raporu
python -m src.models.evaluate_model
```

## Tasarım Prensipleri

- Her dosya **bağımsız çalıştırılabilir** (CLI desteği için `if __name__ == "__main__"`).
- Tüm yollar `config.py` üzerinden gelir (hardcoded yol yok).
- `random_state=42` her yerde sabit (reproducibility).
- Loglar `print` yerine `logging` modülü ile.

## Web Uygulamasıyla Bağlantı

`app/services/prediction_service.py` sadece `src/models/predict.py` içindeki `load_model()` ve `predict_risk()` fonksiyonlarını çağırır. Aralarındaki sınır net.

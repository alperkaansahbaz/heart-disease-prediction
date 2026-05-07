# `app/` — Flask Web Application

Bu klasör web uygulamasının **MVC** benzeri katmanlı yapısını içerir.

## Yapı

```
app/
├── __init__.py          # Application Factory pattern
│
├── routes/              # Controller katmanı (HTTP endpoint'ler)
│   ├── main_routes.py        # /, /about
│   └── prediction_routes.py  # /predict (GET, POST)
│
├── services/            # Business logic
│   └── prediction_service.py # Modeli yükle, tahmin yap, sonuç formatla
│
└── utils/               # Yardımcı fonksiyonlar
    ├── validators.py         # Form input doğrulama
    ├── formatters.py         # Sonuç formatlama (yüzde, etiket)
    └── exceptions.py         # Custom exception sınıfları
```

## Application Factory Pattern

`app/__init__.py` içinde `create_app()` fonksiyonu vardır. Bu desen:
- Test edilebilirliği artırır (her test için yeni app instance)
- Konfigürasyona göre farklı app'ler oluşturulabilir (dev/prod/test)
- Circular import'tan kaçınır

```python
# Kullanım örneği (run.py):
from app import create_app
app = create_app('development')
app.run()
```

## Sorumluluk Ayrımı (Separation of Concerns)

| Katman | Sorumluluk | Örnek |
|--------|-----------|-------|
| **routes/** | HTTP request/response | `request.form`, `render_template` |
| **services/** | İş mantığı | `predict_risk(features)` |
| **utils/** | Yardımcılar | `validate_age(value)` |

> **Kural:** `routes/` doğrudan model yüklemez veya tahmin yapmaz; `services/` çağırır.

## Endpoint'ler

| Method | Path | Açıklama |
|--------|------|----------|
| GET | `/` | Anasayfa |
| GET | `/about` | Proje hakkında |
| GET | `/predict` | Form sayfası |
| POST | `/predict` | Form gönderimi → tahmin |

## Hata Yönetimi

Tüm exception'lar `app/utils/exceptions.py` içinde tanımlı:
- `InvalidInputError` → 400
- `ModelNotLoadedError` → 500

Global error handler'lar `app/__init__.py` içinde register edilir.

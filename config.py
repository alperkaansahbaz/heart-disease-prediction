"""
config.py — Uygulama Konfigürasyonu
====================================

Tüm konfigürasyon değerleri bu dosyada toplanır.
Ortam değişkenleri `.env` dosyasından yüklenir.

Sprint 4'te doldurulacak.
"""

# TODO (Sprint 4):
# - BaseConfig sınıfı (ortak ayarlar)
# - DevelopmentConfig (DEBUG=True)
# - ProductionConfig (DEBUG=False, güvenli secret key)
# - TestingConfig (test veritabanı, mock model)
# - get_config(env: str) factory fonksiyonu
#
# Ayrıca burada toplanacak sabitler:
# - MODEL_PATH, SCALER_PATH
# - FEATURE_NAMES (modelin beklediği sıra)
# - VALIDATION_RULES (yaş 0-120, kolesterol 0-600 vb.)

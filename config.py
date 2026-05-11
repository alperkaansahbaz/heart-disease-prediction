"""
config.py — Uygulama Konfigurasyonu
====================================
Tum konfigurasyon degerleri burada toplanir.
Hardcoded yol/sabit yok.
"""

import os
from pathlib import Path

# ============================================================
# PROJE YOLLARI
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'models' / 'trained' / 'best_model.pkl'
SCALER_PATH = BASE_DIR / 'models' / 'trained' / 'scaler.pkl'
METRICS_PATH = BASE_DIR / 'models' / 'metrics' / 'final_model_info.json'


# ============================================================
# MODELİN BEKLEDİĞİ ÖZELLİKLER (SIRA ÖNEMLİ!)
# ============================================================
# Bu sıra eğitim sırasındaki sıra ile birebir aynı olmalı.
FEATURE_NAMES = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak',
    'slope', 'ca', 'thal'
]


# ============================================================
# VALIDATION KURALLARI
# ============================================================
# Her özellik için (min, max, tip) aralıkları
VALIDATION_RULES = {
    'age': {'min': 0, 'max': 120, 'type': int},
    'sex': {'min': 0, 'max': 1, 'type': int},
    'cp': {'min': 0, 'max': 3, 'type': int},
    'trestbps': {'min': 50, 'max': 250, 'type': int},
    'chol': {'min': 100, 'max': 600, 'type': int},
    'fbs': {'min': 0, 'max': 1, 'type': int},
    'restecg': {'min': 0, 'max': 2, 'type': int},
    'thalach': {'min': 50, 'max': 250, 'type': int},
    'exang': {'min': 0, 'max': 1, 'type': int},
    'oldpeak': {'min': 0.0, 'max': 10.0, 'type': float},
    'slope': {'min': 0, 'max': 2, 'type': int},
    'ca': {'min': 0, 'max': 4, 'type': int},
    'thal': {'min': 0, 'max': 3, 'type': int}
}


# ============================================================
# FLASK KONFIGURASYON SINIFLARI
# ============================================================
class BaseConfig:
    """Tum ortamlarda ortak olan ayarlar."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    JSON_AS_ASCII = False  # Turkce karakter destegi


class DevelopmentConfig(BaseConfig):
    """Gelistirme ortami."""
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """Production ortami."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Mutlaka env'den


class TestingConfig(BaseConfig):
    """Test ortami."""
    DEBUG = False
    TESTING = True


# Konfigurasyonlari isimle al
config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


def get_config(env='development'):
    """Ortama gore konfigurasyonu dondur."""
    return config_map.get(env, DevelopmentConfig)
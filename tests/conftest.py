"""
conftest.py — pytest fixtures
================================
Tum testler tarafindan paylasilan setup'lar burada.
pytest bu dosyayi otomatik yukler.
"""

import pytest
from app import create_app


@pytest.fixture(scope='session')
def app():
    """Flask uygulamasi - session boyunca 1 kez olusur.
    
    Tum testler ayni uygulamayi paylasir.
    """
    app = create_app(env='testing')
    return app


@pytest.fixture
def client(app):
    """Flask test client - HTTP istekleri yapar.
    
    Gercek tarayici yerine kullanilir, hizli.
    """
    return app.test_client()


@pytest.fixture
def valid_form_data():
    """Gecerli form verisi - orta riskli bir hasta orneği."""
    return {
        'age': '52',
        'sex': '1',
        'cp': '0',
        'trestbps': '125',
        'chol': '212',
        'fbs': '0',
        'restecg': '1',
        'thalach': '168',
        'exang': '0',
        'oldpeak': '1.0',
        'slope': '2',
        'ca': '2',
        'thal': '3'
    }


@pytest.fixture
def high_risk_form_data():
    """Yuksek riskli hasta verisi."""
    return {
        'age': '65',
        'sex': '1',
        'cp': '0',
        'trestbps': '150',
        'chol': '280',
        'fbs': '1',
        'restecg': '0',
        'thalach': '110',
        'exang': '1',
        'oldpeak': '2.5',
        'slope': '0',
        'ca': '3',
        'thal': '3'
    }


@pytest.fixture
def low_risk_form_data():
    """Dusuk riskli kisi verisi."""
    return {
        'age': '35',
        'sex': '0',
        'cp': '2',
        'trestbps': '110',
        'chol': '180',
        'fbs': '0',
        'restecg': '0',
        'thalach': '180',
        'exang': '0',
        'oldpeak': '0.0',
        'slope': '2',
        'ca': '0',
        'thal': '2'
    }
"""
test_prediction_service.py — Prediction Service Testleri
==========================================================
PredictionService sinifinin test edilmesi.
Gercek modeli yukler (mock yok).
"""

import pytest

from app.services.prediction_service import PredictionService, prediction_service
from app.utils.exceptions import (
    ModelNotLoadedError,
    InvalidInputError,
    MissingFieldError
)


# ============================================================
# PredictionService SINIF TESTLERI
# ============================================================

class TestPredictionService:
    """PredictionService sinifinin temel davranisi."""
    
    def test_yeni_servis_yuklu_degil(self):
        """Yeni olusan servis henuz yuklu olmamali."""
        service = PredictionService()
        assert service.is_loaded() == False
        assert service.model is None
        assert service.scaler is None
    
    def test_load_modeli_yukler(self):
        """load() cagrilinca model ve scaler yuklenmeli."""
        service = PredictionService()
        service.load()
        
        assert service.is_loaded() == True
        assert service.model is not None
        assert service.scaler is not None
    
    def test_yuklu_olmadan_tahmin_hata(self):
        """Yuklu olmayan servis predict cagrildiginda hata firlatmali."""
        service = PredictionService()  # YENI, load() cagrilmadi
        
        with pytest.raises(ModelNotLoadedError):
            service.predict({'age': '52'})
    
    def test_get_model_info_yuklenmis(self):
        """Yuklenmis servisin model bilgilerini dondurmeli."""
        service = PredictionService()
        service.load()
        
        info = service.get_model_info()
        
        assert info['loaded'] == True
        assert info['feature_count'] == 13
        assert 'features' in info
        assert info['model_type'] == 'KNeighborsClassifier'


# ============================================================
# GLOBAL SERVICE TESTLERI (Singleton)
# ============================================================

class TestGlobalService:
    """Global prediction_service instance'i icin testler."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Her test oncesi servisin yuklendiginden emin ol."""
        if not prediction_service.is_loaded():
            prediction_service.load()
    
    def test_gecerli_tahmin_yapar(self, valid_form_data):
        """Gecerli veri ile tahmin yapilabilmeli."""
        result = prediction_service.predict(valid_form_data)
        
        # Donus dict olmali
        assert isinstance(result, dict)
        
        # Gerekli alanlar var mi?
        assert 'prediction' in result
        assert 'probability' in result
        assert 'risk_level' in result
        assert 'recommendation' in result
    
    def test_tahmin_dogru_tipte(self, valid_form_data):
        """Tahmin int olmali, olasilik float olmali."""
        result = prediction_service.predict(valid_form_data)
        
        # prediction 0 veya 1 olmali
        assert result['prediction'] in [0, 1]
        
        # probability 0-1 arasinda float olmali
        assert isinstance(result['probability'], float)
        assert 0.0 <= result['probability'] <= 1.0
    
    def test_yuksek_risk_tahmin(self, high_risk_form_data):
        """Yuksek riskli veri ile tahmin yapilabilmeli (sonuc model bagimli)."""
        result = prediction_service.predict(high_risk_form_data)
        
        # Sonuc gecerli bir risk seviyesi olmali
        assert result['risk_level'] in ['Dusuk', 'Orta', 'Yuksek']
        # Tahmin 0 veya 1 olmali
        assert result['prediction'] in [0, 1]
    
    def test_dusuk_risk_tahmin(self, low_risk_form_data):
        """Dusuk riskli veri ile tahmin yapilabilmeli (sonuc model bagimli)."""
        result = prediction_service.predict(low_risk_form_data)
        
        # Sonuc gecerli bir risk seviyesi olmali
        assert result['risk_level'] in ['Dusuk', 'Orta', 'Yuksek']
        # Tahmin 0 veya 1 olmali
        assert result['prediction'] in [0, 1]
    
    def test_eksik_alan_hata_firlatir(self, valid_form_data):
        """Eksik alan MissingFieldError firlatmali."""
        del valid_form_data['age']
        
        with pytest.raises(MissingFieldError):
            prediction_service.predict(valid_form_data)
    
    def test_gecersiz_deger_hata_firlatir(self, valid_form_data):
        """Gecersiz deger InvalidInputError firlatmali."""
        valid_form_data['age'] = '999'
        
        with pytest.raises(InvalidInputError):
            prediction_service.predict(valid_form_data)
    
    def test_input_data_geri_doner(self, valid_form_data):
        """Sonucta orijinal veri 'input_data' alaninda donmeli."""
        result = prediction_service.predict(valid_form_data)
        
        assert 'input_data' in result
        assert result['input_data']['age'] == 52  # int olarak donusmus
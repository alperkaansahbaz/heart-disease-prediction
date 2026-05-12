"""
test_routes.py — Integration Testleri
=======================================
Flask route'larini gercek HTTP istekleriyle test eder.
client fixture'i conftest.py'da tanimlanmistir.
"""

import pytest
import json


# ============================================================
# ANASAYFA TESTLERI
# ============================================================

class TestMainRoutes:
    """Ana route'larin test edilmesi."""
    
    def test_anasayfa_200_doner(self, client):
        """GET / -> 200 OK."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_anasayfa_html_doner(self, client):
        """GET / -> HTML icerigi."""
        response = client.get('/')
        # HTML'de baslik olmali
        assert b'HeartCheck' in response.data or b'Kalp' in response.data
    
    def test_about_sayfasi_200(self, client):
        """GET /about -> 200 OK."""
        response = client.get('/about')
        assert response.status_code == 200
    
    def test_about_html_icerir(self, client):
        """GET /about -> HTML icerigi."""
        response = client.get('/about')
        assert b'OSTIM' in response.data or b'OST' in response.data
    
    def test_health_json_doner(self, client):
        """GET /health -> JSON formatinda 200."""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'status' in data
        assert 'model_loaded' in data
    
    def test_olmayan_sayfa_404(self, client):
        """GET /yanlis-url -> 404."""
        response = client.get('/yanlis-url-asdfgh')
        assert response.status_code == 404


# ============================================================
# PREDICT FORM TESTLERI (HTML)
# ============================================================

class TestPredictForm:
    """GET ve POST /predict route'unun test edilmesi."""
    
    def test_get_predict_form_gosterir(self, client):
        """GET /predict -> form sayfasi."""
        response = client.get('/predict')
        assert response.status_code == 200
        
        # Form'un alanlari var mi?
        assert b'age' in response.data
        assert b'chol' in response.data
        assert b'predict' in response.data.lower() or b'tahmin' in response.data.lower()
    
    def test_post_gecerli_form_sonuc_doner(self, client, valid_form_data):
        """POST /predict gecerli veri -> 200 + sonuc."""
        response = client.post('/predict', data=valid_form_data)
        assert response.status_code == 200
        
        # Sonuc sayfasinda risk kelimesi olmali
        body = response.data.lower()
        assert b'risk' in body or b'sonuc' in body
    
    def test_post_eksik_alan_form_geri_doner(self, client, valid_form_data):
        """POST /predict eksik alan -> form geri (200) + hata mesaji."""
        del valid_form_data['age']
        
        response = client.post('/predict', data=valid_form_data)
        # 200 dondurur cunku form'u tekrar gosterir
        assert response.status_code == 200
        
        # Hata mesaji icermeli
        assert b'eksik' in response.data.lower() or b'hata' in response.data.lower()
    
    def test_post_gecersiz_deger_form_geri_doner(self, client, valid_form_data):
        """POST /predict gecersiz deger -> 200 + hata."""
        valid_form_data['age'] = '999'  # Aralik disi
        
        response = client.post('/predict', data=valid_form_data)
        assert response.status_code == 200


# ============================================================
# API TESTLERI (JSON)
# ============================================================

class TestApiRoutes:
    """JSON API endpoint'lerinin test edilmesi."""
    
    def test_api_info_json_doner(self, client):
        """GET /api/info -> JSON ile alan bilgileri."""
        response = client.get('/api/info')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'required_fields' in data
        assert 'field_count' in data
        assert data['field_count'] == 13
    
    def test_api_predict_gecerli_json(self, client):
        """POST /api/predict gecerli JSON -> 200 + tahmin."""
        valid_json = {
            'age': 52, 'sex': 1, 'cp': 0, 'trestbps': 125,
            'chol': 212, 'fbs': 0, 'restecg': 1, 'thalach': 168,
            'exang': 0, 'oldpeak': 1.0, 'slope': 2, 'ca': 2, 'thal': 3
        }
        
        response = client.post(
            '/api/predict',
            data=json.dumps(valid_json),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'prediction' in data
        assert 'probability' in data
        assert 'risk_level' in data
        assert data['risk_level'] in ['Dusuk', 'Orta', 'Yuksek']
    
    def test_api_predict_eksik_alan_400(self, client):
        """POST /api/predict eksik alan -> 400 + hata JSON."""
        invalid_json = {
            'age': 52,
            'sex': 1
            # Diger alanlar eksik
        }
        
        response = client.post(
            '/api/predict',
            data=json.dumps(invalid_json),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'message' in data
    
    def test_api_predict_bos_istek_400(self, client):
        """POST /api/predict bos istek -> 400."""
        response = client.post(
            '/api/predict',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
    
    def test_api_predict_gecersiz_deger_400(self, client):
        """POST /api/predict gecersiz deger -> 400."""
        invalid_json = {
            'age': 999,  # Cok yuksek
            'sex': 1, 'cp': 0, 'trestbps': 125,
            'chol': 212, 'fbs': 0, 'restecg': 1, 'thalach': 168,
            'exang': 0, 'oldpeak': 1.0, 'slope': 2, 'ca': 2, 'thal': 3
        }
        
        response = client.post(
            '/api/predict',
            data=json.dumps(invalid_json),
            content_type='application/json'
        )
        
        assert response.status_code == 400
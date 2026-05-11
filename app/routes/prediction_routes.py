"""
prediction_routes.py — Tahmin Route'lari
==========================================
POST /api/predict  -> JSON ile tahmin yap (form data alir)
GET  /api/info     -> Modelin bekledigi alanlar hakkinda bilgi
"""

from flask import Blueprint, request, jsonify

from app.services.prediction_service import prediction_service
from app.utils.exceptions import (
    InvalidInputError,
    MissingFieldError,
    ModelNotLoadedError,
    PredictionError,
    HeartDiseaseException
)
from config import FEATURE_NAMES, VALIDATION_RULES


# Blueprint olustur (prefix: /api)
prediction_bp = Blueprint('prediction', __name__, url_prefix='/api')


@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """Tahmin yapan ana endpoint.
    
    Beklenen Input (JSON veya form data):
        {
            "age": 52, "sex": 1, "cp": 0, "trestbps": 125,
            "chol": 212, "fbs": 0, "restecg": 1, "thalach": 168,
            "exang": 0, "oldpeak": 1.0, "slope": 2, "ca": 2, "thal": 3
        }
    
    Donus:
        Basarili (200):
            {
                "prediction": 1,
                "prediction_label": "Hasta",
                "probability": 0.87,
                "probability_pct": "%87.0",
                "risk_level": "Yuksek",
                "recommendation": "...",
                "disclaimer": "..."
            }
        
        Hatali (400):
            {"error": "InvalidInputError", "message": "...", "status_code": 400}
        
        Sunucu Hatasi (500):
            {"error": "ModelNotLoadedError", "message": "...", "status_code": 500}
    """
    # 1. Veri tipine gore form_data'yi al
    # JSON ise: request.json
    # Form ise: request.form
    if request.is_json:
        form_data = request.json
    else:
        form_data = request.form.to_dict()
    
    # 2. Bos mu kontrol et
    if not form_data:
        return jsonify({
            'error': 'InvalidInputError',
            'message': 'Bos istek - veri gonderilmedi.',
            'status_code': 400
        }), 400
    
    # 3. Tahmin yap
    try:
        result = prediction_service.predict(form_data)
        return jsonify(result), 200
    
    except (InvalidInputError, MissingFieldError) as e:
        # Kullanici hatasi - 400
        return jsonify(e.to_dict()), e.status_code
    
    except (ModelNotLoadedError, PredictionError) as e:
        # Sunucu hatasi - 500
        return jsonify(e.to_dict()), e.status_code
    
    except Exception as e:
        # Beklenmeyen hata
        return jsonify({
            'error': 'UnknownError',
            'message': f'Beklenmedik bir hata: {str(e)}',
            'status_code': 500
        }), 500


@prediction_bp.route('/info', methods=['GET'])
def info():
    """Modelin bekledigi alanlar hakkinda bilgi dondurur.
    
    Frontend gelistirmek isteyenler veya API kullanicilari icin.
    """
    fields_info = {}
    for field, rule in VALIDATION_RULES.items():
        fields_info[field] = {
            'type': rule['type'].__name__,
            'min': rule['min'],
            'max': rule['max'],
            'description': _get_field_description(field)
        }
    
    return jsonify({
        'required_fields': FEATURE_NAMES,
        'field_count': len(FEATURE_NAMES),
        'field_details': fields_info,
        'example_request': {
            'age': 52, 'sex': 1, 'cp': 0, 'trestbps': 125,
            'chol': 212, 'fbs': 0, 'restecg': 1, 'thalach': 168,
            'exang': 0, 'oldpeak': 1.0, 'slope': 2, 'ca': 2, 'thal': 3
        }
    })


def _get_field_description(field):
    """Her alan icin Turkce aciklama dondurur."""
    descriptions = {
        'age': 'Yas (yil)',
        'sex': 'Cinsiyet (0=Kadin, 1=Erkek)',
        'cp': 'Gogus agrisi tipi (0=Tipik, 1=Atipik, 2=Anjina disi, 3=Asemptomatik)',
        'trestbps': 'Istirahat kan basinci (mm Hg)',
        'chol': 'Serum kolesterol (mg/dl)',
        'fbs': 'Aclik kan sekeri >120 mg/dl (0=Hayir, 1=Evet)',
        'restecg': 'Dinlenme EKG sonuclari (0=Normal, 1=ST-T anormal, 2=Sol ventrikul)',
        'thalach': 'Maksimum kalp atis hizi',
        'exang': 'Egzersize bagli anjina (0=Hayir, 1=Evet)',
        'oldpeak': 'ST depresyonu (egzersiz vs dinlenme)',
        'slope': 'ST segmenti egimi (0=Asagi, 1=Duz, 2=Yukari)',
        'ca': 'Floroskopi ile renklendirilen damar sayisi (0-4)',
        'thal': 'Talasemi (0-3)'
    }
    return descriptions.get(field, 'Aciklama yok')
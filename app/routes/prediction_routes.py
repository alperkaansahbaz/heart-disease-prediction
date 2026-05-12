"""
prediction_routes.py — Tahmin Route'lari
==========================================
GET  /predict       -> Form sayfasi (predict.html)
POST /predict       -> Form gonderildiginde tahmin yap, result.html render et
POST /api/predict   -> JSON API (PowerShell/Postman testleri icin)
GET  /api/info      -> Modelin bekledigi alanlar (JSON)
"""

from flask import Blueprint, request, jsonify, render_template

from app.services.prediction_service import prediction_service
from app.utils.exceptions import (
    InvalidInputError,
    MissingFieldError,
    ModelNotLoadedError,
    PredictionError
)
from config import FEATURE_NAMES, VALIDATION_RULES


# Blueprint - root url ('/'), api'lar ayrica '/api/' altinda
prediction_bp = Blueprint('prediction', __name__)


# ============================================================
# HTML ROUTES (Tarayicidan kullanim)
# ============================================================

@prediction_bp.route('/predict', methods=['GET', 'POST'])
def predict_form():
    """Form sayfasi VE form gonderimi.
    
    GET  : Bos formu goster
    POST : Form'u isle, sonucu goster (result.html) veya hata gosterir (predict.html)
    """
    # GET - Bos form goster
    if request.method == 'GET':
        return render_template('predict.html')
    
    # POST - Form'u isle
    form_data = request.form.to_dict()
    
    try:
        # Tahmin yap (service'de hata kontrolu var)
        result = prediction_service.predict(form_data)
        
        # Sonuc sayfasini goster
        return render_template('result.html', result=result)
    
    except (InvalidInputError, MissingFieldError) as e:
        # Kullanici hatasi - Form'u hata mesajiyla geri goster
        return render_template(
            'predict.html',
            error=e.message,
            form_data=form_data
        )
    
    except (ModelNotLoadedError, PredictionError) as e:
        # Sunucu hatasi - Error sayfasi
        return render_template(
            'error.html',
            error_code=500,
            error_message=e.message
        ), 500
    
    except Exception as e:
        return render_template(
            'error.html',
            error_code=500,
            error_message=f'Beklenmedik bir hata: {str(e)}'
        ), 500


# ============================================================
# JSON API ROUTES (PowerShell/Postman testleri icin)
# ============================================================

@prediction_bp.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON API endpoint - Tahmin yapar.
    
    Beklenen: JSON gonderim
    Donus: JSON sonuc
    """
    # JSON veya form veriyi al
    if request.is_json:
        form_data = request.json
    else:
        form_data = request.form.to_dict()
    
    if not form_data:
        return jsonify({
            'error': 'InvalidInputError',
            'message': 'Bos istek - veri gonderilmedi.',
            'status_code': 400
        }), 400
    
    try:
        result = prediction_service.predict(form_data)
        return jsonify(result), 200
    
    except (InvalidInputError, MissingFieldError) as e:
        return jsonify(e.to_dict()), e.status_code
    
    except (ModelNotLoadedError, PredictionError) as e:
        return jsonify(e.to_dict()), e.status_code
    
    except Exception as e:
        return jsonify({
            'error': 'UnknownError',
            'message': f'Beklenmedik hata: {str(e)}',
            'status_code': 500
        }), 500


@prediction_bp.route('/api/info', methods=['GET'])
def api_info():
    """API kullanim rehberi."""
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
        'cp': 'Gogus agrisi tipi (0-3)',
        'trestbps': 'Istirahat kan basinci (mm Hg)',
        'chol': 'Serum kolesterol (mg/dl)',
        'fbs': 'Aclik kan sekeri >120 mg/dl (0/1)',
        'restecg': 'Dinlenme EKG sonuclari (0-2)',
        'thalach': 'Maksimum kalp atis hizi',
        'exang': 'Egzersize bagli anjina (0/1)',
        'oldpeak': 'ST depresyonu',
        'slope': 'ST segmenti egimi (0-2)',
        'ca': 'Floroskopi damar sayisi (0-4)',
        'thal': 'Talasemi (0-3)'
    }
    return descriptions.get(field, 'Aciklama yok')
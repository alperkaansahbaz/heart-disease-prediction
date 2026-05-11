"""
main_routes.py — Ana Sayfa Route'lari
=======================================
GET /          -> Anasayfa
GET /about     -> Proje hakkinda
GET /health    -> Saglik kontrolu (API'nin calistigini gosterir)
"""

from flask import Blueprint, jsonify

from app.services.prediction_service import prediction_service


# Blueprint olustur (route'lari gruplandirmak icin)
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Anasayfa - API bilgilerini dondurur.
    
    Sprint 5'te HTML sayfasi ekleyecegiz, simdilik JSON.
    """
    return jsonify({
        'name': 'Heart Disease Prediction API',
        'version': '1.0.0',
        'description': 'Klinik ozelliklere dayali kalp hastaligi risk tahmini',
        'endpoints': {
            'GET /': 'Bu sayfa - API bilgileri',
            'GET /about': 'Proje hakkinda detayli bilgi',
            'GET /health': 'Saglik kontrolu',
            'GET /api/predict': 'Form sayfasi (Sprint 5)',
            'POST /api/predict': 'Tahmin yap (JSON)'
        },
        'authors': ['Alperen ARSLAN', 'Alper Kaan SAHBAZ'],
        'project': 'OSTIM Teknik Universitesi - Mezuniyet Projesi'
    })


@main_bp.route('/about')
def about():
    """Proje hakkinda detayli bilgi."""
    return jsonify({
        'project_name': 'Heart Disease Prediction System',
        'university': 'OSTIM Teknik Universitesi',
        'department': 'Bilgisayar Muhendisligi',
        'authors': [
            {'name': 'Alperen ARSLAN', 'role': 'ML Engineer & Backend'},
            {'name': 'Alper Kaan SAHBAZ', 'role': 'Frontend & Data Analyst'}
        ],
        'advisor': 'Murad NAGHIYEV',
        'methodology': {
            'dataset': 'Heart Disease Dataset (UCI)',
            'preprocessing': 'Duplicate removal, StandardScaler',
            'models_tested': 9,
            'final_model': 'KNN (Optimized)',
            'accuracy': '%86.89',
            'roc_auc': 0.9058
        },
        'tech_stack': {
            'backend': 'Flask 3.0',
            'ml': 'scikit-learn 1.5.2, XGBoost 2.1.1',
            'frontend': 'HTML5 + Bootstrap 5'
        },
        'disclaimer': (
            'Bu sistem akademik amacli bir prototiptir ve '
            'tibbi tani amaciyla kullanilamaz.'
        )
    })


@main_bp.route('/health')
def health_check():
    """Saglik kontrolu - API ve modelin durumunu dondurur.
    
    Monitoring araclari (Pingdom, UptimeRobot vb.) icin standart endpoint.
    """
    model_info = prediction_service.get_model_info()
    
    return jsonify({
        'status': 'healthy' if model_info['loaded'] else 'degraded',
        'api_version': '1.0.0',
        'model_loaded': model_info['loaded'],
        'model_info': model_info
    })
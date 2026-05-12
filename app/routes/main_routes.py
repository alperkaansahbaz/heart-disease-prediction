"""
main_routes.py — Ana Sayfa Route'lari
=======================================
GET /          -> Anasayfa (index.html)
GET /about     -> Proje hakkinda (about.html)
GET /health    -> Saglik kontrolu (JSON)
"""

from flask import Blueprint, jsonify, render_template

from app.services.prediction_service import prediction_service


# Blueprint olustur
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Anasayfa - HTML render eder."""
    return render_template('index.html')


@main_bp.route('/about')
def about_page():
    """Proje hakkinda sayfasi - HTML render eder.
    
    NOT: Fonksiyon adi 'about_page', cunku 'about' route adi
    base.html'de url_for('main.about_page') olarak kullaniliyor.
    """
    return render_template('about.html')


@main_bp.route('/health')
def health_check():
    """Saglik kontrolu - JSON dondurur.
    
    Monitoring araclari icin (Pingdom, UptimeRobot vb.)
    """
    model_info = prediction_service.get_model_info()
    
    return jsonify({
        'status': 'healthy' if model_info['loaded'] else 'degraded',
        'api_version': '1.0.0',
        'model_loaded': model_info['loaded'],
        'model_info': model_info
    })
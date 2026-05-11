"""
__init__.py — Flask Application Factory
=========================================
Bu dosya Flask uygulamasini olusturur ve yapilandirir.
create_app() fonksiyonu uygulamanin merkezindedir.
"""

from flask import Flask, jsonify

from config import get_config
from app.utils.exceptions import HeartDiseaseException


def create_app(env='development'):
    """Flask uygulamasini olusturur ve dondurur.
    
    Args:
        env: 'development', 'production' veya 'testing'
    
    Returns:
        Flask: Yapilandirilmis Flask uygulamasi
    """
    # 1. Uygulamayi olustur
    app = Flask(__name__)
    
    # 2. Konfigurasyonu yukle
    config_class = get_config(env)
    app.config.from_object(config_class)
    
    print(f"[Flask] Uygulama olusturuluyor (env: {env})")
    print(f"[Flask] Debug: {app.config['DEBUG']}")
    
    # 3. Model service'i baslat (uygulama basinda 1 kez)
    _initialize_services(app)
    
    # 4. Route'lari kaydet (blueprint'leri)
    _register_blueprints(app)
    
    # 5. Hata handler'lari kaydet
    _register_error_handlers(app)
    
    print(f"[Flask] Uygulama hazir!")
    return app


def _initialize_services(app):
    """Servisleri baslat (model yukleme vb.)."""
    from app.services.prediction_service import prediction_service
    
    try:
        prediction_service.load()
        print(f"[Flask] PredictionService basariyla yuklendi")
    except Exception as e:
        # Production'da bu kritik bir hata, log'lanmali
        print(f"[Flask] HATA: PredictionService yuklenemedi: {e}")
        # Uygulamayi yine de baslat (health endpoint'i hata bildirecek)


def _register_blueprints(app):
    """Tum blueprint'leri uygulamaya ekle."""
    from app.routes.main_routes import main_bp
    from app.routes.prediction_routes import prediction_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(prediction_bp)
    
    print(f"[Flask] Blueprint'ler kaydedildi:")
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            methods = ','.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
            print(f"   {methods:10s} {rule.rule}")


def _register_error_handlers(app):
    """Global hata yakalayicilari kaydet."""
    
    @app.errorhandler(HeartDiseaseException)
    def handle_custom_exception(e):
        """Bizim custom exception'larimiz icin."""
        return jsonify(e.to_dict()), e.status_code
    
    @app.errorhandler(404)
    def not_found(e):
        """404 - Sayfa bulunamadi."""
        return jsonify({
            'error': 'NotFound',
            'message': 'Istenen sayfa bulunamadi.',
            'status_code': 404
        }), 404
    
    @app.errorhandler(405)
    def method_not_allowed(e):
        """405 - Yanlis HTTP method."""
        return jsonify({
            'error': 'MethodNotAllowed',
            'message': 'Bu endpoint icin gecersiz HTTP method.',
            'status_code': 405
        }), 405
    
    @app.errorhandler(500)
    def internal_error(e):
        """500 - Sunucu hatasi."""
        return jsonify({
            'error': 'InternalServerError',
            'message': 'Sunucu hatasi olustu. Lutfen daha sonra tekrar deneyin.',
            'status_code': 500
        }), 500
    
    print(f"[Flask] Error handler'lar kaydedildi")
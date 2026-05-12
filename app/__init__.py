"""
__init__.py — Flask Application Factory
=========================================
"""

from flask import Flask, jsonify

from config import get_config
from app.utils.exceptions import HeartDiseaseException


def create_app(env='development'):
    """Flask uygulamasini olusturur ve dondurur."""
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static'
    )

    config_class = get_config(env)
    app.config.from_object(config_class)

    print(f"[Flask] Uygulama olusturuluyor (env: {env})")
    print(f"[Flask] Debug: {app.config['DEBUG']}")

    _initialize_services(app)
    _register_blueprints(app)
    _register_error_handlers(app)

    print(f"[Flask] Uygulama hazir!")
    return app


def _initialize_services(app):
    from app.services.prediction_service import prediction_service
    try:
        prediction_service.load()
        print(f"[Flask] PredictionService basariyla yuklendi")
    except Exception as e:
        print(f"[Flask] HATA: PredictionService yuklenemedi: {e}")


def _register_blueprints(app):
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
    @app.errorhandler(HeartDiseaseException)
    def handle_custom_exception(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            'error': 'NotFound',
            'message': 'Istenen sayfa bulunamadi.',
            'status_code': 404
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({
            'error': 'MethodNotAllowed',
            'message': 'Bu endpoint icin gecersiz HTTP method.',
            'status_code': 405
        }), 405

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            'error': 'InternalServerError',
            'message': 'Sunucu hatasi olustu.',
            'status_code': 500
        }), 500

    print(f"[Flask] Error handler'lar kaydedildi")
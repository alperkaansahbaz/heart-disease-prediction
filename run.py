"""
run.py — Flask Uygulamasi Giris Noktasi
==========================================
Calistirma:
    python run.py

Uygulama varsayilan olarak http://127.0.0.1:5000 adresinde calisir.
"""

import os
from app import create_app

# Environment degiskeni veya varsayilan
env = os.environ.get('FLASK_ENV', 'development')

# Flask uygulamasini olustur
app = create_app(env)


if __name__ == '__main__':
    print("=" * 60)
    print("HEART DISEASE PREDICTION API")
    print("=" * 60)
    print(f"Adres: http://127.0.0.1:5000")
    print(f"Endpoints:")
    print(f"  GET  http://127.0.0.1:5000/")
    print(f"  GET  http://127.0.0.1:5000/about")
    print(f"  GET  http://127.0.0.1:5000/health")
    print(f"  GET  http://127.0.0.1:5000/api/info")
    print(f"  POST http://127.0.0.1:5000/api/predict")
    print("=" * 60)
    print("Durdurmak icin: Ctrl + C")
    print("=" * 60)
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=False  # Modeli iki kez yuklemesin
    )
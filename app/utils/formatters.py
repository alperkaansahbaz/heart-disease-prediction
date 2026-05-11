"""
formatters.py — Sonuc Formatlama
==================================
Model ciktisini kullaniciya gosterilecek formata cevirir.
"""


def format_probability(prob):
    """Olasiligi yuzde stringine cevirir.
    
    Args:
        prob: 0-1 arasi float (orn: 0.87)
    
    Returns:
        str: Yuzde formati (orn: "%87.0")
    """
    return f"%{prob * 100:.1f}"


def format_risk_level(probability):
    """Olasiliga gore risk seviyesini belirler.
    
    Args:
        probability: 0-1 arasi float
    
    Returns:
        str: 'Dusuk', 'Orta', 'Yuksek'
    """
    if probability < 0.35:
        return 'Dusuk'
    elif probability < 0.65:
        return 'Orta'
    else:
        return 'Yuksek'


def format_recommendation(risk_level):
    """Risk seviyesine gore tavsiye metni dondurur.
    
    Args:
        risk_level: 'Dusuk', 'Orta', 'Yuksek'
    
    Returns:
        str: Tavsiye metni
    """
    recommendations = {
        'Dusuk': (
            'Sonuclariniza gore dusuk risk grubundasiniz. '
            'Yine de duzenli sagk kontrolleri ihmal etmeyin ve '
            'saglikli yasam aliskanliklarini surdurun.'
        ),
        'Orta': (
            'Sonuclariniza gore orta risk grubundasiniz. '
            'Bir doktora basvurarak detayli muayene yaptirmaniz onerilir. '
            'Beslenme ve egzersiz aliskanliklarinizi gozden gecirin.'
        ),
        'Yuksek': (
            'Sonuclariniza gore yuksek risk grubundasiniz. '
            'En kisa surede bir kardiyologa basvurmaniz onemle tavsiye edilir. '
            'Bu bir tibbi tani degildir, sadece bir on degerlendirmedir.'
        )
    }
    return recommendations.get(risk_level, 'Lutfen bir doktora basvurun.')


def format_prediction_result(prediction, probability):
    """Tum sonuc bilgilerini tek bir dict'te toplar.
    
    Args:
        prediction: Model ciktisi (0 veya 1)
        probability: Hasta olma olasiligi (0-1 arasi float)
    
    Returns:
        dict: Kullaniciya gosterilecek tum bilgiler
    """
    risk_level = format_risk_level(probability)
    
    return {
        'prediction': int(prediction),
        'prediction_label': 'Hasta' if prediction == 1 else 'Saglikli',
        'probability': round(float(probability), 4),
        'probability_pct': format_probability(probability),
        'risk_level': risk_level,
        'recommendation': format_recommendation(risk_level),
        'disclaimer': (
            'UYARI: Bu sistem bir tibbi tani aracidir ve doktor muayenesinin '
            'yerine gecmez. Sonuclar yalnizca bilgi amaclidir.'
        )
    }
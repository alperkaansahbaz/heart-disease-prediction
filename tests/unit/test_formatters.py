"""
test_formatters.py — Formatter Testleri
=========================================
Sonuc formatlama fonksiyonlarinin test edilmesi.
"""

import pytest

from app.utils.formatters import (
    format_probability,
    format_risk_level,
    format_recommendation,
    format_prediction_result
)


# ============================================================
# format_probability() TESTLERI
# ============================================================

class TestFormatProbability:
    """format_probability() fonksiyonu icin testler."""
    
    def test_yuzde_donusum(self):
        """0.5 -> '%50.0' donusumu."""
        assert format_probability(0.5) == '%50.0'
    
    def test_sifir(self):
        """0.0 -> '%0.0'"""
        assert format_probability(0.0) == '%0.0'
    
    def test_bir(self):
        """1.0 -> '%100.0'"""
        assert format_probability(1.0) == '%100.0'
    
    def test_ondalik_yuvarlama(self):
        """0.876 -> '%87.6'"""
        assert format_probability(0.876) == '%87.6'


# ============================================================
# format_risk_level() TESTLERI
# ============================================================

class TestFormatRiskLevel:
    """format_risk_level() fonksiyonu icin testler."""
    
    def test_dusuk_risk(self):
        """0.35 altinda 'Dusuk' donmeli."""
        assert format_risk_level(0.0) == 'Dusuk'
        assert format_risk_level(0.20) == 'Dusuk'
        assert format_risk_level(0.34) == 'Dusuk'
    
    def test_orta_risk(self):
        """0.35-0.65 arasi 'Orta' donmeli."""
        assert format_risk_level(0.35) == 'Orta'
        assert format_risk_level(0.50) == 'Orta'
        assert format_risk_level(0.64) == 'Orta'
    
    def test_yuksek_risk(self):
        """0.65 ustu 'Yuksek' donmeli."""
        assert format_risk_level(0.65) == 'Yuksek'
        assert format_risk_level(0.85) == 'Yuksek'
        assert format_risk_level(1.0) == 'Yuksek'


# ============================================================
# format_recommendation() TESTLERI
# ============================================================

class TestFormatRecommendation:
    """format_recommendation() fonksiyonu icin testler."""
    
    def test_dusuk_risk_tavsiyesi(self):
        """Dusuk risk tavsiyesi 'dusuk' kelimesi icermeli."""
        result = format_recommendation('Dusuk')
        assert 'dusuk' in result.lower()
    
    def test_orta_risk_tavsiyesi(self):
        """Orta risk tavsiyesi 'doktor' kelimesi icermeli."""
        result = format_recommendation('Orta')
        assert 'doktor' in result.lower()
    
    def test_yuksek_risk_tavsiyesi(self):
        """Yuksek risk tavsiyesi 'kardiyolog' kelimesi icermeli."""
        result = format_recommendation('Yuksek')
        assert 'kardiyolog' in result.lower()


# ============================================================
# format_prediction_result() TESTLERI
# ============================================================

class TestFormatPredictionResult:
    """format_prediction_result() fonksiyonu icin testler."""
    
    def test_hasta_sonucu(self):
        """prediction=1 -> 'Hasta' label."""
        result = format_prediction_result(1, 0.87)
        
        assert result['prediction'] == 1
        assert result['prediction_label'] == 'Hasta'
        assert result['probability'] == 0.87
        assert result['probability_pct'] == '%87.0'
        assert result['risk_level'] == 'Yuksek'
    
    def test_saglikli_sonucu(self):
        """prediction=0 -> 'Saglikli' label."""
        result = format_prediction_result(0, 0.20)
        
        assert result['prediction'] == 0
        assert result['prediction_label'] == 'Saglikli'
        assert result['probability'] == 0.20
        assert result['risk_level'] == 'Dusuk'
    
    def test_tum_alanlar_var(self):
        """Donen dict tum gerekli alanlari icermeli."""
        result = format_prediction_result(1, 0.5)
        
        required_keys = [
            'prediction', 'prediction_label', 'probability',
            'probability_pct', 'risk_level', 'recommendation',
            'disclaimer'
        ]
        
        for key in required_keys:
            assert key in result, f"Eksik alan: {key}"
    
    def test_disclaimer_uyari_icerir(self):
        """Disclaimer 'UYARI' kelimesi icermeli."""
        result = format_prediction_result(1, 0.8)
        assert 'UYARI' in result['disclaimer']
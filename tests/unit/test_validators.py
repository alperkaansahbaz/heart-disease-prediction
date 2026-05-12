"""
test_validators.py — Validator Testleri
=========================================
Input validation fonksiyonlarinin test edilmesi.
"""

import pytest

from app.utils.validators import validate_field, validate_form, to_feature_vector
from app.utils.exceptions import InvalidInputError, MissingFieldError


# ============================================================
# validate_field() TESTLERI
# ============================================================

class TestValidateField:
    """validate_field() fonksiyonu icin testler."""
    
    # ==================== POZITIF CASE'LER ====================
    
    def test_gecerli_yas_kabul_edilir(self):
        """Yas alani gecerli degerle calismali."""
        result = validate_field('age', '52')
        assert result == 52
        assert isinstance(result, int)
    
    def test_gecerli_oldpeak_float_donduru(self):
        """Oldpeak alani float donmeli."""
        result = validate_field('oldpeak', '1.5')
        assert result == 1.5
        assert isinstance(result, float)
    
    def test_sinir_degerleri_kabul_edilir(self):
        """Min ve max degerleri kabul edilmeli."""
        assert validate_field('age', '0') == 0      # min
        assert validate_field('age', '120') == 120  # max
        assert validate_field('sex', '0') == 0      # min
        assert validate_field('sex', '1') == 1      # max
    
    def test_string_sayi_int_e_donusur(self):
        """'52' stringi 52 int'ine donusmeli."""
        assert validate_field('age', '52') == 52
        assert type(validate_field('age', '52')) is int
    
    def test_float_string_int_e_donusur(self):
        """'52.0' stringi 52 int'ine donusmeli (int alanlarda)."""
        result = validate_field('age', '52.0')
        assert result == 52
    
    # ==================== NEGATIF CASE'LER ====================
    
    def test_negatif_yas_hata_firlatir(self):
        """Negatif yas InvalidInputError firlatmali."""
        with pytest.raises(InvalidInputError):
            validate_field('age', '-5')
    
    def test_cok_buyuk_yas_hata_firlatir(self):
        """200 yas InvalidInputError firlatmali."""
        with pytest.raises(InvalidInputError):
            validate_field('age', '200')
    
    def test_string_metin_hata_firlatir(self):
        """'abc' gibi sayisal olmayan deger hata firlatmali."""
        with pytest.raises(InvalidInputError):
            validate_field('age', 'abc')
    
    def test_bos_string_missing_field_hatasi(self):
        """Bos string MissingFieldError firlatmali."""
        with pytest.raises(MissingFieldError):
            validate_field('age', '')
    
    def test_none_missing_field_hatasi(self):
        """None deger MissingFieldError firlatmali."""
        with pytest.raises(MissingFieldError):
            validate_field('age', None)
    
    def test_bilinmeyen_alan_hata_firlatir(self):
        """Tanimsiz alan adi hata firlatmali."""
        with pytest.raises(InvalidInputError):
            validate_field('unknown_field', '52')
    
    def test_sex_aralik_disi_hata(self):
        """Sex sadece 0 veya 1 olabilir."""
        with pytest.raises(InvalidInputError):
            validate_field('sex', '2')
        with pytest.raises(InvalidInputError):
            validate_field('sex', '5')


# ============================================================
# validate_form() TESTLERI
# ============================================================

class TestValidateForm:
    """validate_form() fonksiyonu icin testler."""
    
    def test_gecerli_form_tam_donusur(self, valid_form_data):
        """Gecerli form verisi tamamen donusmeli."""
        result = validate_form(valid_form_data)
        
        # Tum alanlar var mi?
        assert 'age' in result
        assert 'sex' in result
        assert 'thal' in result
        
        # Tip donusumu olmus mu?
        assert isinstance(result['age'], int)
        assert isinstance(result['oldpeak'], float)
    
    def test_eksik_alan_missing_field_hatasi(self, valid_form_data):
        """Bir alan eksikse MissingFieldError firlatmali."""
        del valid_form_data['age']  # Yas alanini sil
        
        with pytest.raises(MissingFieldError):
            validate_form(valid_form_data)
    
    def test_gecersiz_deger_invalid_hatasi(self, valid_form_data):
        """Bir alan gecersizse InvalidInputError firlatmali."""
        valid_form_data['age'] = '999'  # Cok buyuk yas
        
        with pytest.raises(InvalidInputError):
            validate_form(valid_form_data)


# ============================================================
# to_feature_vector() TESTLERI
# ============================================================

class TestToFeatureVector:
    """to_feature_vector() fonksiyonu icin testler."""
    
    def test_dogru_siralama(self):
        """Vector dogru sirada donmeli."""
        cleaned = {
            'age': 52, 'sex': 1, 'cp': 0, 'trestbps': 125,
            'chol': 212, 'fbs': 0, 'restecg': 1, 'thalach': 168,
            'exang': 0, 'oldpeak': 1.0, 'slope': 2, 'ca': 2, 'thal': 3
        }
        
        result = to_feature_vector(cleaned)
        
        # Liste mi?
        assert isinstance(result, list)
        
        # Uzunluk 13 mu?
        assert len(result) == 13
        
        # Ilk eleman yas mi?
        assert result[0] == 52
        
        # Son eleman thal mi?
        assert result[12] == 3
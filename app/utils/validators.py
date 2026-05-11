"""
validators.py — Input Dogrulama
=================================
Form girdilerini validate eder. Hata varsa exception firlatir.
"""

from config import VALIDATION_RULES, FEATURE_NAMES
from app.utils.exceptions import InvalidInputError, MissingFieldError


def validate_field(field_name, value):
    """Tek bir alani validate eder.
    
    Args:
        field_name: Alan adi (orn: 'age')
        value: Kullanicidan gelen ham deger (genelde string)
    
    Returns:
        Dogrulanmis ve tip donusumu yapilmis deger
    
    Raises:
        MissingFieldError: Deger bos ise
        InvalidInputError: Deger gecersiz ise
    """
    # 1. Bilinen bir alan mi?
    if field_name not in VALIDATION_RULES:
        raise InvalidInputError(f"Bilinmeyen alan: '{field_name}'")
    
    rule = VALIDATION_RULES[field_name]
    
    # 2. Bos mu?
    if value is None or value == '':
        raise MissingFieldError(field_name)
    
    # 3. Dogru tipe donusturulebilir mi?
    try:
        if rule['type'] == int:
            # Once float'a, sonra int'e (kullanici "5.0" yazmis olabilir)
            converted = int(float(value))
        elif rule['type'] == float:
            converted = float(value)
        else:
            converted = value
    except (ValueError, TypeError):
        raise InvalidInputError(
            f"'{field_name}' icin gecerli bir sayi girilmedi: '{value}'"
        )
    
    # 4. Aralikta mi?
    if converted < rule['min'] or converted > rule['max']:
        raise InvalidInputError(
            f"'{field_name}' degeri {rule['min']}-{rule['max']} araliginda olmali. "
            f"Girilen: {converted}"
        )
    
    return converted


def validate_form(form_data):
    """Tum form verisini validate eder.
    
    Args:
        form_data: Dict (form'dan gelen ham veri)
                   Ornek: {'age': '52', 'sex': '1', 'cp': '0', ...}
    
    Returns:
        Dict: Temizlenmis ve dogru sirada veri
              Ornek: {'age': 52, 'sex': 1, 'cp': 0, ...}
    
    Raises:
        MissingFieldError: Eksik alan varsa
        InvalidInputError: Gecersiz deger varsa
    """
    cleaned = {}
    
    # Her zorunlu alan icin
    for feature in FEATURE_NAMES:
        raw_value = form_data.get(feature)
        cleaned[feature] = validate_field(feature, raw_value)
    
    return cleaned


def to_feature_vector(cleaned_data):
    """Temizlenmis veriyi modelin bekledigi sirada listeye cevirir.
    
    Args:
        cleaned_data: validate_form() ciktisi
    
    Returns:
        List: FEATURE_NAMES sirasinda degerlerin listesi
              [52, 1, 0, 125, 212, 0, 1, 168, 0, 1.0, 2, 2, 3]
    """
    return [cleaned_data[name] for name in FEATURE_NAMES]
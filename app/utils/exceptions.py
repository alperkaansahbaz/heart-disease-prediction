"""
exceptions.py — Custom Exception Siniflari
============================================
Uygulamamizda kullanilacak ozel hata siniflari.
Her birinin bir HTTP status code'u var.
"""


class HeartDiseaseException(Exception):
    """Tum custom exception'larin base'i."""
    status_code = 500
    default_message = "Beklenmedik bir hata olustu."

    def __init__(self, message=None, status_code=None):
        super().__init__(message or self.default_message)
        self.message = message or self.default_message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """JSON response icin sozluk halinde dondur."""
        return {
            'error': self.__class__.__name__,
            'message': self.message,
            'status_code': self.status_code
        }


class InvalidInputError(HeartDiseaseException):
    """Kullanici girisi gecersiz oldugunda firlatilir.
    
    Ornek: yas negatif, kolesterol 1000, cinsiyet 5...
    HTTP 400 (Bad Request)
    """
    status_code = 400
    default_message = "Girilen veri gecersiz."


class MissingFieldError(HeartDiseaseException):
    """Zorunlu alan eksik oldugunda firlatilir.
    
    Ornek: form'da 'age' yok
    HTTP 400 (Bad Request)
    """
    status_code = 400
    default_message = "Zorunlu alan eksik."

    def __init__(self, field_name=None):
        message = f"Zorunlu alan eksik: '{field_name}'" if field_name else self.default_message
        super().__init__(message)


class ModelNotLoadedError(HeartDiseaseException):
    """Model dosyasi bulunamadiginda firlatilir.
    
    Ornek: best_model.pkl silinmis
    HTTP 500 (Internal Server Error)
    """
    status_code = 500
    default_message = "Model yuklenemedi. Sistem yoneticisine basvurun."


class PredictionError(HeartDiseaseException):
    """Tahmin sirasinda hata olustugunda firlatilir.
    
    HTTP 500
    """
    status_code = 500
    default_message = "Tahmin yapilirken bir hata olustu."
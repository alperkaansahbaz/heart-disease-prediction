"""
prediction_service.py — Tahmin Is Mantigi
===========================================
Form verisini alir, modeli kullanir, sonucu formatlar.

Bu sinif Singleton pattern ile calisir:
Modeli sadece bir kez yukler, sonra tekrar tekrar kullanir.
"""

import joblib
import numpy as np

from config import MODEL_PATH, SCALER_PATH, FEATURE_NAMES
from app.utils.exceptions import ModelNotLoadedError, PredictionError
from app.utils.validators import validate_form, to_feature_vector
from app.utils.formatters import format_prediction_result


class PredictionService:
    """Tahmin islerinden sorumlu servis sinifi.
    
    Kullanim:
        service = PredictionService()
        service.load()  # Modeli yukle (uygulama basinda 1 kez)
        result = service.predict(form_data)  # Tahmin yap
    """
    
    def __init__(self):
        """Servisi olustur ama modeli henuz yukleme."""
        self.model = None
        self.scaler = None
        self._is_loaded = False
    
    def load(self):
        """Model ve scaler'i diskten yukle.
        
        Bu method uygulama baslangicinda CAGRILMALI.
        Boylece her tahmin icin model yeniden yuklenmez.
        
        Raises:
            ModelNotLoadedError: Dosyalar bulunamazsa
        """
        try:
            self.model = joblib.load(MODEL_PATH)
            self.scaler = joblib.load(SCALER_PATH)
            self._is_loaded = True
            print(f"[PredictionService] Model yuklendi: {type(self.model).__name__}")
            print(f"[PredictionService] Scaler yuklendi: {type(self.scaler).__name__}")
        except FileNotFoundError as e:
            raise ModelNotLoadedError(
                f"Model veya scaler dosyasi bulunamadi: {e.filename}"
            )
        except Exception as e:
            raise ModelNotLoadedError(
                f"Model yuklenirken hata: {str(e)}"
            )
    
    def is_loaded(self):
        """Modelin yuklu olup olmadigini dondurur."""
        return self._is_loaded
    
    def predict(self, form_data):
        """Form verisinden tahmin yapar.
        
        Pipeline:
            1. Validate (validators.py)
            2. Feature vector olustur
            3. Scale (scaler.transform)
            4. Predict (model.predict + predict_proba)
            5. Format (formatters.py)
        
        Args:
            form_data: dict (Flask request.form veya request.json)
        
        Returns:
            dict: Formatlanmis tahmin sonucu
        
        Raises:
            ModelNotLoadedError: Model yuklenmemisse
            InvalidInputError: Validation hatasi
            PredictionError: Tahmin sirasinda hata
        """
        # 0. Hazirlik kontrolu
        if not self._is_loaded:
            raise ModelNotLoadedError(
                "Model henuz yuklenmedi. Once load() metodunu cagirin."
            )
        
        # 1. Validate (hata firlatabilir)
        cleaned_data = validate_form(form_data)
        
        # 2. Feature vector
        feature_vector = to_feature_vector(cleaned_data)
        
        try:
            # 3. Numpy array'e cevir (scaler bekliyor)
            X = np.array([feature_vector])  # shape: (1, 13)
            
            # 4. Scale et
            X_scaled = self.scaler.transform(X)
            
            # 5. Tahmin yap
            prediction = self.model.predict(X_scaled)[0]
            probability = self.model.predict_proba(X_scaled)[0][1]  # Class 1 olasiligi
            
            # 6. Formatla ve dondur
            result = format_prediction_result(prediction, probability)
            
            # Bonus: Kullanicinin girdigi temizlenmis veriyi de ekle
            result['input_data'] = cleaned_data
            
            return result
        
        except Exception as e:
            raise PredictionError(f"Tahmin sirasinda hata: {str(e)}")
    
    def get_model_info(self):
        """Model hakkinda bilgi dondurur (debug icin)."""
        if not self._is_loaded:
            return {'loaded': False}
        
        return {
            'loaded': True,
            'model_type': type(self.model).__name__,
            'scaler_type': type(self.scaler).__name__,
            'feature_count': len(FEATURE_NAMES),
            'features': FEATURE_NAMES
        }


# ============================================================
# GLOBAL SERVICE INSTANCE
# ============================================================
# Singleton pattern: Tum uygulama boyunca tek bir service var.
prediction_service = PredictionService()
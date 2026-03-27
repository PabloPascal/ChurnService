import joblib
import pandas as pd 
import os 
import numpy as np 
#implementation later ...

#trained_model
dir = os.curdir

print(os.curdir)

class ChurnPredictor:

    def __init__(self):
        self.model = joblib.load('ml/trained_model/model.pkl')
        self.threshold = np.load('ml/trained_model/best_threshold.npy')
        self.scaler = joblib.load('ml/trained_model/scaler.pkl')
        self.feature_names = joblib.load('ml/trained_model/feature_names.pkl') 

    def preprocessing(self, data : dict):
        df = pd.DataFrame([data])
        df = df.reindex(columns=self.feature_names, fill_value=0)
        scaled_data = self.scaler.transform(df)
        return scaled_data 


    def predict(self, data : dict) -> dict[str, float]:
        
        print("predict in predictor")
        scaled = self.preprocessing(data)
        
        print("predict_proba")

        predict_proba = self.model.predict_proba(scaled)[0, 1]

        print("predict with threshold")

        predict = int(predict_proba > self.threshold)

        return {'churn_probability': float(predict_proba), 'churn_prediction': predict}

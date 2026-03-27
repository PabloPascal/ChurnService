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
        self.pipeline = joblib.load(dir + '/ml/trained_model/pipeline.pkl')
        self.threshold = np.load(dir + '/ml/trained_model/best_threshold.npy') 

    def preprocessing(self, data : dict):
        pass 


    def predict(self, data : dict) -> dict[str, float]:
        
        df = pd.DataFrame([data])
        predict_proba = self.pipeline.predict_proba(df)[0, 1]
        predict = int(predict_proba > self.threshold)

        return {'churn_probability': float(predict_proba), 'churn_prediction': predict}

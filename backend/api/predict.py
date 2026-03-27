from fastapi import APIRouter, BackgroundTasks, Request
from ml.predictor import ChurnPredictor
from api.models import ChurnRequest, ChurnResponse
from fastapi.exceptions import HTTPException
from core.logger import logger
from database.db_routes import save_prediction_log
from time import time 


router = APIRouter()

predictor = ChurnPredictor()

@router.post("/predict",  response_model=ChurnResponse)
async def predict(request : ChurnRequest, req : Request, background_task : BackgroundTasks):
    try:
        start = time()
        result = predictor.predict(request.model_dump())
        end = time()

        duration = end - start 

        background_task.add_task(save_prediction_log, 
        {
            "client_ip": req.client.host,
            "input_data": request.model_dump(),
            "probability": result["churn_probability"],
            "prediction": result["churn_prediction"],
            "processing_time_ms": duration,
        })

        return ChurnResponse(**result) 
    
    except Exception as ex:
        print(f"Prediction error: {ex}")
        raise HTTPException(status_code=500, detail="Prediction failed")







from fastapi import APIRouter
from ml.predictor import ChurnPredictor
from api.models import ChurnRequest, ChurnResponse
from fastapi.exceptions import HTTPException
from core.logger import logger

router = APIRouter()

predictor = ChurnPredictor()

@router.post("/predict",  response_model=ChurnResponse)
async def predict(request : ChurnRequest):
    try:
        result = predictor.predict(request.model_dump())
        return ChurnResponse(**result) 
    except Exception as ex:
        print(f"Prediction error: {ex}")
        raise HTTPException(status_code=500, detail="Prediction failed")

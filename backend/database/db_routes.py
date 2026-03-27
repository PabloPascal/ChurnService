from database.db_models import PredictionLog
from database.db_init import AsyncSessionLocal


async def save_prediction_log(data : dict):

    try:
        async with AsyncSessionLocal() as sessin:
            
            log = PredictionLog(**data)
            sessin.add(log) 
            await sessin.commit()
    except Exception as ex:
        print(f"save_prediction_failed: {ex}")
        



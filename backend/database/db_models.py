from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, DateTime, String, JSON, func
from datetime import datetime, timezone


Base = declarative_base()


class PredictionLog(Base):
    __tablename__ = "prediction_logs"


    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    
    #предсказание 
    probability : Mapped[float] = mapped_column(Float) 
    prediction : Mapped[int] = mapped_column(Integer)
    
    #введенные данные 
    input_data : Mapped[dict] = mapped_column(JSON)

    #дополнительная инфа 
    client_ip : Mapped[str] = mapped_column(String)
    model_version : Mapped[str] = mapped_column(String, default="1.0")
    processing_time_ms : Mapped[float] = mapped_column(Float)
    #timestamp : Mapped[datetime] = \
    #       mapped_column(default=lambda: datetime.now(timezone.utc), nullable=False)



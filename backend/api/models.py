from pydantic import BaseModel, Field, field_validator
from typing import Literal

class ChurnRequest(BaseModel):
    CreditScore: int = Field(ge=0, description="кредитный рейтинг")
    Age: int = Field(ge=18, le=100, description="возраст от 18 лет")
    Tenure: int = Field(ge=0, le=120, description="Количество лет обслуживания")
    Balance: float = Field(ge=0, description="Баланс счета (неотрицательный)")
    NumOfProducts: int = Field(ge=0, description="Количество продуктов банка (1-4)")
    HasCrCard: Literal[0, 1] = Field(description="имеется ли карта")
    IsActiveMember: Literal[0, 1] = Field(description="активный клиент")
    EstimatedSalary: float = Field(ge=0)
    Geography : Literal['France', 'Germany', 'Spain'] = Field(description="Страна: France, Germany или Spain")
    Gender: Literal['Male', 'Female'] = Field(description="пол человека")



class ChurnResponse(BaseModel):
    churn_probability: float
    churn_prediction: int
    model_version: str = "1.0"



 

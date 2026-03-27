from pydantic import BaseModel


class ChurnRequest(BaseModel):
    CreditScore : int 
    Age : int 
    Tenure : int 
    Balance : float  
    NumOfProducts : int 
    HasCrCard : int 
    IsActiveMember : int 
    Geography_France : int 
    Geography_Germany : int 
    Geography_Spain : int  
    Gender_Female : int 
    Gender_Male : int 
    EstimatedSalary : float 


class ChurnResponse(BaseModel):
    churn_probability: float
    churn_prediction: int
    model_version: str = "1.0"



 

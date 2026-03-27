import os 


class Settings:
    URL_DB = os.getenv("DATABASE_URL", "postgresql+asyncpg://churn_service:1248@localhost/churn_service_db")


setting = Settings()
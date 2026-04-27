import os 
from dotenv import load_dotenv

load_dotenv()


class Settings:
    URL_DB = os.getenv("DATABASE_URL")
    if URL_DB is None:
        raise ValueError("DATABASE_URL environment variable is not set")


    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"



setting = Settings()
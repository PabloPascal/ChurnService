from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from database.db_models import Base 
from core.config import setting

engine = create_async_engine(setting.URL_DB, echo = True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)



async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

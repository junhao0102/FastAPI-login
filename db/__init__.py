from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from dotenv import load_dotenv
import os

load_dotenv()

# 創建一個非同步的資料庫引擎
asyncEngine = create_async_engine(f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}", echo=False)

#  創建一個非同步的資料庫會話工廠
asyncSession = sessionmaker(asyncEngine, expire_on_commit=False, class_=AsyncSession)

""" 建立資料庫會話 """
async def getSession():
    session = asyncSession()
    try:
        yield session
    except Exception as e:
        await session.rollback()
        print(f"資料庫會話錯誤: {e}")
        raise
    finally:
        await session.close()

""" 初始化建立資料庫 """
async def initDB():
    try:
        async with asyncEngine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("資料庫初始化成功")
    except Exception as e:
        print(f"資料庫初始化失敗: {e}")
        raise



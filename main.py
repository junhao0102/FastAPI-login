import uvicorn
from fastapi import FastAPI
from api import apiRouter
from contextlib import asynccontextmanager
from db import initDB
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
serverPort = os.getenv("SERVER_PORT") if os.getenv("SERVER_PORT") else 8000
serverHost = os.getenv("SERVER_HOST") if os.getenv("SERVER_HOST") else "localhost"

""" 生命週期管理 """
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initDB()
    yield # 交出控制權給 FastAPI，app 開始運行

#　建立 FastAPI 應用
app = FastAPI(lifespan=lifespan)

# 掛載統一的路由器到應用
app.include_router(apiRouter)

if __name__ == "__main__":
    print("啟動伺服器.....")
    uvicorn.run("main:app", host=serverHost, port=int(serverPort), reload=False)
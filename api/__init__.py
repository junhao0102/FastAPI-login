from fastapi import APIRouter
from .user import router as userRouter


# 建立APIRouter
apiRouter = APIRouter()

# 註冊子路由
apiRouter.include_router(userRouter)

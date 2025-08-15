from fastapi import APIRouter
from .user import router as userRouter
from .login import router as loginRouter

# 建立APIRouter
apiRouter = APIRouter()

# 註冊子路由
apiRouter.include_router(userRouter)
apiRouter.include_router(loginRouter)

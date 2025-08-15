from fastapi import APIRouter
from schemas import CreateUser, CreateUserResponse, ReadUserResponse
from fastapi import HTTPException
from db import getSession
from db.fun import addUser, getUser
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["user"], prefix="/api")


@router.get("/user", response_model=ReadUserResponse)
async def get_user(session: AsyncSession = Depends(getSession)):
    try:
        user = await getUser(session)
        if not user:
            raise HTTPException(status_code=404, detail="User does not exist")
        return {
            "status": "success",
            "message": "User retrieved successfully",
            "data": user,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.post("/user", response_model=CreateUserResponse)
async def create_user(
    create_user: CreateUser, session: AsyncSession = Depends(getSession)
):
    try:
        new_user = await addUser(
            create_user.name, create_user.email, create_user.password, session
        )
        return {
            "status": "success",
            "message": "User created successfully",
            "data": new_user,
        }
    except IntegrityError as e:
        await session.rollback()
        errorMessage = str(e.orig)
        if "email" in errorMessage:
            raise HTTPException(status_code=400, detail="Email already exists")
        elif "name" in errorMessage:
            raise HTTPException(status_code=400, detail="Name already exists")
        else:
            raise HTTPException(status_code=400, detail="Integrity error occurred")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

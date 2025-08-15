from fastapi import APIRouter, Depends, HTTPException
from schemas import LoginResponse, Login
from sqlalchemy.ext.asyncio import AsyncSession
from db import getSession
from db.fun import getHashByUser
from utils.security import verifyPassword

router = APIRouter(tags=["login"], prefix="/api")


@router.post("/login", response_model=LoginResponse)
async def login(login: Login, session: AsyncSession = Depends(getSession)):
    try:
        hashedPassword = await getHashByUser(login.name,session)
        if not hashedPassword:
            raise HTTPException(status_code=404, detail="User not found")
        if verifyPassword(login.password, hashedPassword):
            return {"status":"success","message":"Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Password is incorrect")
    except HTTPException :
        raise 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
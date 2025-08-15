from db.models import UserModel
from sqlalchemy.future import select
from utils.security import hashPassword

async def getUser(session):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()

async def addUser(name, email, password, session):
    newUser = UserModel(name=name, email=email, password=hashPassword(password))
    session.add(newUser)
    await session.commit()
    await session.refresh(newUser)
    return newUser

async def getHashByUser(name, session):
    query = select(UserModel).where(UserModel.name == name)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if user:
        return user.password
    return None

from db.models import UserModel
from sqlalchemy.future import select

""" 搜尋所有 User """
async def getUser(session):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()


""" 添加 User """
async def addUser(name, email, password,session):
    new_user = UserModel(name=name, email=email, password=password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


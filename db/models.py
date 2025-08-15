from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# 創建 Base 類，用於所有模型繼承
Base = declarative_base()

""" 定義 User 模型 """
class UserModel(Base):
    __tablename__ = "user" 

    id = Column(Integer, primary_key=True)  
    name = Column(String, unique=True, nullable=False) 
    email = Column(String, unique=True, nullable=False) 
    password = Column(String, nullable=False)  
    


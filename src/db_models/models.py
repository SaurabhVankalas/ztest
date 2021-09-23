from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db_models.database import Base

class Telegram_Data(Base):
    __tablename__ = "telegram_data"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=False, index=True)
    date = Column(String,unique=False, index=True)


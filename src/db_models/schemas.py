from typing import List

from pydantic import BaseModel

class Telegram_DataBase(BaseModel):
    text:str
    date:str
class Telegram_Data(Telegram_DataBase):
    id: int

    class Config:
        orm_mode = True

class Telegram_Data_Create(Telegram_DataBase):
    pass

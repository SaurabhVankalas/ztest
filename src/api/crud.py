from sqlalchemy.orm import Session
from db_models import models,schemas



def get_last_update(db:Session,tele_id:int):
    return db.query(models.Telegram_Data).filter(models.Telegram_Data.id == tele_id).first()

def create_update(db: Session, data1: schemas.Telegram_Data_Create):
    db_data = models.Telegram_Data(text=data1.text, date=data1.date)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_updates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Telegram_Data).offset(skip).limit(limit).all()

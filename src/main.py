from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response
from api import crud
from db_models import models, schemas
import uvicorn
from db_models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.post("/data/")  # , response_model=schemas.Telegram_DataBase)
def create_update(data: schemas.Telegram_DataBase, db: Session = Depends(get_db)):
    crud.create_update(db=db, data1=data)
    return {"response": "Success", "data": data}


@app.get("/read_data/", response_model=List[schemas.Telegram_Data])
def read_updates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_data = crud.get_updates(db, skip=skip, limit=limit)
    return all_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

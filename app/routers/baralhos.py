from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/baralhos/", response_model=schemas.Baralho)
def create_baralho(baralho: schemas.BaralhoCreate, db: Session = Depends(database.get_db)):
    return crud.create_baralho(db=db, baralho=baralho)

@router.get("/baralhos/", response_model=list[schemas.Baralho])
def read_baralhos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    baralhos = crud.get_baralhos(db, skip=skip, limit=limit)
    return baralhos

@router.get("/baralhos/{baralho_id}", response_model=schemas.Baralho)
def read_baralho(baralho_id: int, db: Session = Depends(database.get_db)):
    db_baralho = crud.get_baralho(db, baralho_id=baralho_id)
    if db_baralho is None:
        raise HTTPException(status_code=404, detail="Baralho not found")
    return db_baralho

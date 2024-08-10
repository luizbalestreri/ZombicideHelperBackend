from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database, auth

router = APIRouter()

@router.post("/cartas/", response_model=schemas.Carta)
def create_carta(carta: schemas.CartaCreate, db: Session = Depends(database.get_db), jogador: models.Jogador = Depends(auth.get_current_jogador)):
    return crud.create_carta(db=db, carta=carta)

@router.get("/cartas/", response_model=list[schemas.Carta])
def read_cartas(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), jogador: models.Jogador = Depends(auth.get_current_jogador)):
    cartas = crud.get_cartas(db, skip=skip, limit=limit)
    return cartas

@router.get("/cartas/{carta_id}", response_model=schemas.Carta)
def read_carta(carta_id: int, db: Session = Depends(database.get_db), jogador: models.Jogador = Depends(auth.get_current_jogador)):
    db_carta = crud.get_carta(db, carta_id=carta_id)
    if db_carta is None:
        raise HTTPException(status_code=404, detail="Carta not found")
    return db_carta

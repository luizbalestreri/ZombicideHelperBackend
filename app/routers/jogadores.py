from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/jogadores/", response_model=schemas.Jogador)
def create_jogador(jogador: schemas.JogadorCreate, db: Session = Depends(database.get_db)):
    return crud.create_jogador(db=db, jogador=jogador)

@router.get("/jogadores/", response_model=list[schemas.Jogador])
def read_jogadores(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    jogadores = crud.get_jogadores(db, skip=skip, limit=limit)
    return jogadores

@router.get("/jogadores/{jogador_id}", response_model=schemas.Jogador)
def read_jogador(jogador_id: int, db: Session = Depends(database.get_db)):
    db_jogador = crud.get_jogador(db, jogador_id=jogador_id)
    if db_jogador is None:
        raise HTTPException(status_code=404, detail="Jogador not found")
    return db_jogador

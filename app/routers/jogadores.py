from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db
from ..auth import get_current_jogador

router = APIRouter()

@router.post("/jogadores/", response_model=schemas.Jogador)
def create_jogador(jogador: schemas.JogadorCreate, db: Session = Depends(get_db)):
    return crud.create_jogador(db=db, jogador=jogador)

@router.get("/jogadores/", response_model=List[schemas.Jogador])
def read_jogadores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_jogadores(db, skip=skip, limit=limit)

@router.get("/jogadores/{jogador_id}", response_model=schemas.Jogador)
def read_jogador(jogador_id: int, db: Session = Depends(get_db)):
    db_jogador = crud.get_jogador(db, jogador_id=jogador_id)
    if db_jogador is None:
        raise HTTPException(status_code=404, detail="Jogador not found")
    return db_jogador

@router.get("/me", response_model=schemas.Jogador)
def get_me(jogador: models.Jogador = Depends(get_current_jogador)):
    return jogador

@router.post("/assign_models_to_player/", response_model=schemas.Jogador)
def assign_models_to_player(jogador_id: int, modelo_ids: List[int], db: Session = Depends(get_db)):
    return crud.assign_models_to_player(db=db, jogador_id=jogador_id, modelo_ids=modelo_ids)

@router.get("/assigned_models/{jogador_id}", response_model=List[int])
def get_assigned_models(jogador_id: int, db: Session = Depends(get_db)):
    return crud.get_assigned_models(db=db, jogador_id=jogador_id)
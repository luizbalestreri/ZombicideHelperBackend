from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/personagem_modelos/", response_model=schemas.PersonagemModeloResponse)
def create_personagem_modelo(modelo: schemas.PersonagemModeloCreate, db: Session = Depends(get_db)):
    return crud.create_personagem_modelo(db=db, modelo=modelo)

@router.get("/personagem_modelos/", response_model=List[schemas.PersonagemModeloResponse])
def read_personagem_modelos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_personagem_modelos(db, skip=skip, limit=limit)
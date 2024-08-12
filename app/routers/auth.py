from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import crud

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from ..database import get_db
import secrets

router = APIRouter()

@router.post("/token", response_model=schemas.Jogador)
def generate_new_token(login_data: schemas.LoginData, db: Session = Depends(get_db)):
    token = secrets.token_urlsafe(32)
    jogador = crud.create_jogador(db, schemas.JogadorCreate(nome=login_data.nome, token=token))
    return jogador

def get_current_jogador(token: str, db: Session = Depends(get_db)):
    jogador = crud.get_jogador_by_token(db, token)
    if not jogador:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return jogador
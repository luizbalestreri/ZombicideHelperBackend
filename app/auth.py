import secrets
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from .database import get_db
from .models import Jogador

api_key_header = APIKeyHeader(name="X-Token")

def generate_token():
    return secrets.token_hex(16)

def verify_token(db: Session, token: str):
    jogador = db.query(Jogador).filter(Jogador.token == token).first()
    if jogador:
        return jogador
    raise HTTPException(status_code=401, detail="Invalid token")

def get_current_jogador(db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    return verify_token(db, token)

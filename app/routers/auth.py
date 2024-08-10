from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import auth, models, schemas, database

router = APIRouter()

@router.post("/token", response_model=schemas.Jogador)
def generate_new_token(nome: str, db: Session = Depends(database.get_db)):
    token = auth.generate_token()
    jogador = models.Jogador(nome=nome, token=token)  # Usar o nome fornecido
    db.add(jogador)
    db.commit()
    db.refresh(jogador)
    return jogador

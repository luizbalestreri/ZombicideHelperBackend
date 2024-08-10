from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/personagens/", response_model=schemas.Personagem)
def create_personagem(personagem: schemas.PersonagemCreate, db: Session = Depends(database.get_db)):
    return crud.create_personagem(db=db, personagem=personagem)

@router.get("/personagens/", response_model=list[schemas.Personagem])
def read_personagens(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    personagens = crud.get_personagens(db, skip=skip, limit=limit)
    return personagens

@router.get("/personagens/{personagem_id}", response_model=schemas.Personagem)
def read_personagem(personagem_id: int, db: Session = Depends(database.get_db)):
    db_personagem = crud.get_personagem(db, personagem_id=personagem_id)
    if db_personagem is None:
        raise HTTPException(status_code=404, detail="Personagem not found")
    return db_personagem

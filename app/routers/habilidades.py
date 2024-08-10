from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/habilidades/", response_model=schemas.Habilidade)
def create_habilidade(habilidade: schemas.HabilidadeCreate, db: Session = Depends(database.get_db)):
    return crud.create_habilidade(db=db, habilidade=habilidade)

@router.get("/habilidades/", response_model=list[schemas.Habilidade])
def read_habilidades(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    habilidades = crud.get_habilidades(db, skip=skip, limit=limit)
    return habilidades

@router.get("/habilidades/{habilidade_id}", response_model=schemas.Habilidade)
def read_habilidade(habilidade_id: int, db: Session = Depends(database.get_db)):
    db_habilidade = crud.get_habilidade(db, habilidade_id=habilidade_id)
    if db_habilidade is None:
        raise HTTPException(status_code=404, detail="Habilidade not found")
    return db_habilidade

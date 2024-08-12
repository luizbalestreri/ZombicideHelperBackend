from http.client import HTTPException
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas

def get_carta(db: Session, carta_id: int):
    return db.query(models.Carta).filter(models.Carta.id == carta_id).first()

def get_cartas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Carta).offset(skip).limit(limit).all()

def create_carta(db: Session, carta: schemas.CartaCreate):
    db_carta = models.Carta(**carta.dict())
    db.add(db_carta)
    db.commit()
    db.refresh(db_carta)
    return db_carta

def get_baralho(db: Session, baralho_id: int):
    return db.query(models.Baralho).filter(models.Baralho.id == baralho_id).first()

def get_baralhos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Baralho).offset(skip).limit(limit).all()

def create_baralho(db: Session, baralho: schemas.BaralhoCreate):
    db_baralho = models.Baralho(nome=baralho.nome, descricao=baralho.descricao)
    db.add(db_baralho)
    db.commit()
    db.refresh(db_baralho)
    for carta_id in baralho.cartas:
        db_carta = db.query(models.Carta).filter(models.Carta.id == carta_id).first()
        db_baralho.cartas.append(db_carta)
    db.commit()
    return db_baralho

def get_habilidade(db: Session, habilidade_id: int):
    return db.query(models.Habilidade).filter(models.Habilidade.id == habilidade_id).first()

def get_habilidades(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Habilidade).offset(skip).limit(limit).all()

def create_habilidade(db: Session, habilidade: schemas.HabilidadeCreate):
    db_habilidade = models.Habilidade(**habilidade.dict())
    db.add(db_habilidade)
    db.commit()
    db.refresh(db_habilidade)
    return db_habilidade

def get_personagem(db: Session, personagem_id: int):
    return db.query(models.Personagem).filter(models.Personagem.id == personagem_id).first()

def get_personagens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Personagem).offset(skip).limit(limit).all()

def create_personagem(db: Session, personagem: schemas.PersonagemCreate):
    db_personagem = models.Personagem(
        pontos_de_vida=personagem.pontos_de_vida,
        nivel=personagem.nivel,
        pontos_de_experiencia=personagem.pontos_de_experiencia,
        jogador_id=personagem.jogador_id,
        modelo_id=personagem.modelo_id  # Ligando ao modelo de personagem
    )
    db.add(db_personagem)
    db.commit()
    db.refresh(db_personagem)
    for habilidade_id in personagem.habilidades:
        db_habilidade = db.query(models.Habilidade).filter(models.Habilidade.id == habilidade_id).first()
        db_personagem.habilidades.append(db_habilidade)
    db.commit()
    return db_personagem

def create_personagem_modelo(db: Session, modelo: schemas.PersonagemModeloCreate):
    db_modelo = models.PersonagemModelo(
        nome=modelo.nome,
        foto=modelo.foto,
        descricao=modelo.descricao
    )
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)

    for habilidade in modelo.habilidades:
        habilidade_id = habilidade["habilidade_id"]
        level = habilidade["level"]
        db.execute(
            models.personagem_habilidade_association.insert().values(
                habilidade_id=habilidade_id,
                personagem_modelo_id=db_modelo.id,
                level=level
            )
        )
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

def get_jogador(db: Session, jogador_id: int):
    return db.query(models.Jogador).filter(models.Jogador.id == jogador_id).first()

def get_jogadores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Jogador).offset(skip).limit(limit).all()

def create_jogador(db: Session, jogador: schemas.JogadorCreate):
    if not jogador.nome:
        raise HTTPException(status_code=400, detail="O nome do jogador não pode ser vazio.")
    
    db_jogador = models.Jogador(**jogador.dict())
    db.add(db_jogador)
    db.commit()
    db.refresh(db_jogador)
    return db_jogador

def get_personagem_modelos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PersonagemModelo).offset(skip).limit(limit).all()


from sqlalchemy.orm import Session
from app import models, schemas

def assign_models_to_player(db: Session, jogador_id: int, modelo_ids: List[int]):
    jogador = db.query(models.Jogador).filter(models.Jogador.id == jogador_id).first()
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador not found")

    for modelo_id in modelo_ids:
        modelo = db.query(models.PersonagemModelo).filter(models.PersonagemModelo.id == modelo_id).first()
        if not modelo:
            raise HTTPException(status_code=404, detail=f"PersonagemModelo with id {modelo_id} not found")

        personagem = models.Personagem(
            pontos_de_vida=3,  # Default values, adjust as needed
            nivel=1,
            pontos_de_experiencia=1,
            jogador_id=jogador_id,
            modelo_id=modelo_id
        )
        db.add(personagem)

    db.commit()
    db.refresh(jogador)
    return jogador

def get_assigned_models(db: Session, jogador_id: int):
    jogador = db.query(models.Jogador).filter(models.Jogador.id == jogador_id).first()
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador not found")

    assigned_models = [personagem.modelo_id for personagem in jogador.personagens]
    return assigned_models

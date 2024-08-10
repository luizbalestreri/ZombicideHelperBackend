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
        nome=personagem.nome,
        pontos_de_vida=personagem.pontos_de_vida,
        nivel=personagem.nivel,
        pontos_de_experiencia=personagem.pontos_de_experiencia,
        jogador_id=personagem.jogador_id
    )
    db.add(db_personagem)
    db.commit()
    db.refresh(db_personagem)
    for habilidade in personagem.habilidades:
        db_habilidade = models.Habilidade(**habilidade.dict(), personagem_id=db_personagem.id)
        db.add(db_habilidade)
    db.commit()
    return db_personagem

def get_jogador(db: Session, jogador_id: int):
    return db.query(models.Jogador).filter(models.Jogador.id == jogador_id).first()

def get_jogadores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Jogador).offset(skip).limit(limit).all()

def create_jogador(db: Session, jogador: schemas.JogadorCreate):
    db_jogador = models.Jogador(**jogador.dict())
    db.add(db_jogador)
    db.commit()
    db.refresh(db_jogador)
    return db_jogador

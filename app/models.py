from typing import Dict, List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

# Association table (no changes here)
personagem_habilidade_association = Table(
    "personagem_habilidade_association",
    Base.metadata,
    Column("habilidade_id", Integer, ForeignKey("habilidades.id")),
    Column("personagem_modelo_id", Integer, ForeignKey("personagem_modelos.id")),
    Column("level", Integer, nullable=False)  # Add the level column
)

class Carta(Base):
    __tablename__ = "cartas"  # Fixed tablename attribute
    id = Column(Integer, primary_key=True, index=True)
    foto = Column(String, index=True)
    tipo = Column(String)

class Baralho(Base):
    __tablename__ = "baralhos"  # Fixed tablename attribute
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    cartas = relationship("Carta", secondary="baralho_cartas")

class BaralhoCarta(Base):
    __tablename__ = "baralho_cartas"  # Fixed tablename attribute
    baralho_id = Column(Integer, ForeignKey("baralhos.id"), primary_key=True)
    carta_id = Column(Integer, ForeignKey("cartas.id"), primary_key=True)

# Moved Habilidade class here to be defined before it's used
class Habilidade(Base):
    __tablename__ = "habilidades"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    personagem_modelos = relationship(
        "PersonagemModelo",
        secondary=personagem_habilidade_association,
        back_populates="habilidades",
        uselist=True,
        primaryjoin="Habilidade.id == personagem_habilidade_association.c.habilidade_id",
        secondaryjoin="PersonagemModelo.id == personagem_habilidade_association.c.personagem_modelo_id",
        viewonly=True
    )
    
class PersonagemModelo(Base):
    __tablename__ = "personagem_modelos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, index=True)
    foto: Mapped[str] = mapped_column(String)
    descricao: Mapped[str] = mapped_column(String)
    personagens = relationship("Personagem", back_populates="modelo")
    habilidades = relationship(
        "Habilidade",
        secondary=personagem_habilidade_association,
        back_populates="personagem_modelos",
        uselist=True,
        primaryjoin="PersonagemModelo.id == personagem_habilidade_association.c.personagem_modelo_id",
        secondaryjoin="Habilidade.id == personagem_habilidade_association.c.habilidade_id",
        viewonly=True
    )

class Personagem(Base):
    __tablename__ = "personagens"
    id = Column(Integer, primary_key=True, index=True)
    pontos_de_vida = Column(Integer)
    nivel = Column(Integer)
    pontos_de_experiencia = Column(Integer)
    jogador_id = Column(Integer, ForeignKey("jogadores.id"))
    modelo_id = Column(Integer, ForeignKey("personagem_modelos.id"))
    modelo = relationship("PersonagemModelo", back_populates="personagens")
    jogador = relationship("Jogador", back_populates="personagens")

class Jogador(Base):     
    __tablename__ = "jogadores"  # Fixed tablename attribute
    id = Column(Integer, primary_key=True, index=True)     
    nome = Column(String, index=True)     
    token = Column(String, unique=True, index=True)     
    personagens = relationship("Personagem", back_populates="jogador")  

# Pydantic models for API responses (moved to the bottom)
class HabilidadeBase(BaseModel):
    nome: str
    descricao: str

class HabilidadeResponse(HabilidadeBase):
    id: int

    class Config:
        orm_mode = True

class PersonagemModeloBase(BaseModel):
    nome: str
    foto: str
    descricao: str

class PersonagemModeloResponse(PersonagemModeloBase):
    id: int
    habilidades: List[Dict[str, int]]  # Lista de dicionários com habilidade_id e level

    class Config:
        orm_mode = True
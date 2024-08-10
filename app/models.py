from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Carta(Base):
    __tablename__ = "cartas"
    id = Column(Integer, primary_key=True, index=True)
    foto = Column(String, index=True)
    tipo = Column(String)

class Baralho(Base):
    __tablename__ = "baralhos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    cartas = relationship("Carta", secondary="baralho_cartas")

class BaralhoCarta(Base):
    __tablename__ = "baralho_cartas"
    baralho_id = Column(Integer, ForeignKey("baralhos.id"), primary_key=True)
    carta_id = Column(Integer, ForeignKey("cartas.id"), primary_key=True)

class Habilidade(Base):
    __tablename__ = "habilidades"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    nivel = Column(Integer)
    personagem_id = Column(Integer, ForeignKey("personagens.id"))
    personagem = relationship("Personagem", back_populates="habilidades")  # Ajuste aqui

class Personagem(Base):
    __tablename__ = "personagens"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    pontos_de_vida = Column(Integer)
    nivel = Column(Integer)
    pontos_de_experiencia = Column(Integer)
    jogador_id = Column(Integer, ForeignKey("jogadores.id"))
    habilidades = relationship("Habilidade", back_populates="personagem")
    jogador = relationship("Jogador", back_populates="personagens")  # Adicione essa linha

class Jogador(Base):
    __tablename__ = "jogadores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    token = Column(String, unique=True, index=True)  # Campo token
    personagens = relationship("Personagem", back_populates="jogador")  # Ajuste aqui

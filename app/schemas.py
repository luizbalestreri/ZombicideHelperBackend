from pydantic import BaseModel
from typing import List, Optional

class CartaBase(BaseModel):
    foto: str
    tipo: str

class CartaCreate(CartaBase):
    pass

class Carta(CartaBase):
    id: int

    class Config:
        orm_mode = True

class BaralhoBase(BaseModel):
    nome: str
    descricao: str

class BaralhoCreate(BaralhoBase):
    cartas: List[int]

class Baralho(BaralhoBase):
    id: int
    cartas: List[Carta]

    class Config:
        orm_mode = True

class HabilidadeBase(BaseModel):
    nome: str
    descricao: str

class HabilidadeCreate(HabilidadeBase):
    pass

class Habilidade(HabilidadeBase):
    id: int

    class Config:
        orm_mode = True

class PersonagemModeloBase(BaseModel):
    nome: str
    foto: str
    descricao: str

class PersonagemModeloResponse(PersonagemModeloBase):
    id: int
    habilidades: List[Habilidade] = []

    class Config:
        orm_mode = True

class PersonagemModeloCreate(PersonagemModeloBase):
    habilidades: List[dict]  # Lista de dicionários com habilidade_id e nivel

class PersonagemModelo(PersonagemModeloBase):
    id: int
    habilidades: List[dict]  # Lista de dicionários com habilidade e nivel

    class Config:
        orm_mode = True

class PersonagemBase(BaseModel):
    pontos_de_vida: int
    nivel: int
    pontos_de_experiencia: int

class PersonagemCreate(PersonagemBase):
    habilidades: List[int]
    jogador_id: int
    modelo_id: int  # Referência ao PersonagemModelo

class Personagem(PersonagemBase):
    id: int
    habilidades: List[int]
    modelo: PersonagemModelo  # Inclui detalhes do modelo

    class Config:
        orm_mode = True

class JogadorBase(BaseModel):
    nome: str
    token: str

class JogadorCreate(JogadorBase):
    pass

class Jogador(JogadorBase):
    id: int
    personagens: List[Personagem]

    class Config:
        orm_mode = True

class LoginData(BaseModel):
    nome: str
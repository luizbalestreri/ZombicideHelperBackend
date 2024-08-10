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
    nivel: int

class HabilidadeCreate(HabilidadeBase):
    pass

class Habilidade(HabilidadeBase):
    id: int
    personagem_id: Optional[int] = None

    class Config:
        orm_mode = True

class PersonagemBase(BaseModel):
    nome: str
    pontos_de_vida: int
    nivel: int
    pontos_de_experiencia: int

class PersonagemCreate(PersonagemBase):
    habilidades: List[HabilidadeCreate]
    jogador_id: int

class Personagem(PersonagemBase):
    id: int
    habilidades: List[Habilidade]

    class Config:
        orm_mode = True

class JogadorBase(BaseModel):
    nome: str
    token: str  # Adicione o campo token

class JogadorCreate(JogadorBase):
    pass

class Jogador(JogadorBase):
    id: int
    personagens: List[Personagem]

    class Config:
        orm_mode = True
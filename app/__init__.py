from fastapi import FastAPI
from .database import engine, Base
from .routers import cartas, baralhos, personagens, jogadores, habilidades

app = FastAPI()

# Incluir rotas
app.include_router(cartas.router)
app.include_router(baralhos.router)
app.include_router(personagens.router)
app.include_router(jogadores.router)
app.include_router(habilidades.router)

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)


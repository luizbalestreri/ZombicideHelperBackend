from fastapi import FastAPI
from .database import engine, Base
from .routers import cartas, baralhos, personagens, jogadores, habilidades, auth

app = FastAPI()

# Incluir rotas
app.include_router(cartas.router)
app.include_router(baralhos.router)
app.include_router(personagens.router)
app.include_router(jogadores.router)
app.include_router(habilidades.router)
app.include_router(auth.router)  # Adicione a rota de autenticação

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Zombicide App - Swagger UI",
    )

@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(
        title="Zombicide App",
        version="1.0.0",
        description="API para gerenciar as cartas do jogo Zombicide",
        routes=app.routes,
    )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import cartas, baralhos, personagens, personagemModelo, jogadores, habilidades, auth

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",  # Add this if you're using Vite's default port
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir rotas
app.include_router(cartas.router)
app.include_router(baralhos.router)
app.include_router(personagemModelo.router)
app.include_router(personagens.router)
app.include_router(jogadores.router)
app.include_router(habilidades.router)
app.include_router(auth.router, prefix="/auth", tags=["auth"])

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the Zombicide Helper API"}

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

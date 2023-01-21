from fastapi import FastAPI
from config.config import metadata, database
from routes.routes import router

app = FastAPI(
    title='CODHAB - Usuários',
    description='API CRUD Usuários para candidatura em emprego - Marconi M Marques'
    )

app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

@app.get('/',summary='Bem vindo', description='@Endpoint raiz ("/") ')
async def get_roof():
    return {'msg': 'API CODHAB - Usuários'}

app.include_router(router, prefix="")




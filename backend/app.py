import os
from fastapi import FastAPI
from controllers import colaboradores_controller
from extensions.database_enum import DataBase
from infra.config import create_database

app = FastAPI()

app.include_router(colaboradores_controller.route, prefix='/api')

@app.get('/')
def index():
    """ Selecionar qual database vai ser utilizado.."""
    tipo_database = os.getenv("TIPO_DATABASE")
    if not tipo_database:
        tipo_database = DataBase.SQLLITE.name

    create_database.CreateDataBase(tipo_database)

    return {"API FastAPI + PostgreSQL!"}

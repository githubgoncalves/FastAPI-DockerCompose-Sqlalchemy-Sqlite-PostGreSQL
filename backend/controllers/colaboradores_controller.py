import os
from fastapi import APIRouter,status
from typing import List
from schemas.colaboradores_schema import ColaboradoresSchema
from fastapi.responses import JSONResponse
from services import colaboradores_service
from extensions.database_enum import DataBase

route = APIRouter()

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLITE.name

service = colaboradores_service.ColaboradoresService(tipo_database)

@route.get('/colaboradores', status_code=status.HTTP_200_OK,response_model=dict)
async def get_alunos():
    app_name = os.getenv("APP_NAME")
    if app_name:
        return JSONResponse(content=f"API de Colaboradores da {app_name} Disponivel!")
    return JSONResponse(content="{API de Colaboradores Disponivel!}")

@route.get('/colaboradores/listar',status_code=status.HTTP_200_OK,response_model=List[ColaboradoresSchema])
async def listar():
   colaboradores_list = service.listar()
   return colaboradores_list

@route.get('/colaboradores/consultar/{nome}',status_code=status.HTTP_200_OK,response_model=List[ColaboradoresSchema])  
async def consultar(nome):
    colaboradores_list = service.consultar(nome)
    return colaboradores_list

@route.post('/colaboradores/incluir',status_code=status.HTTP_200_OK,response_model=str,)  
async def incluir(colaborador: ColaboradoresSchema):
   service.incluir(colaborador)
   return JSONResponse(content="Incluido com Sucesso!")

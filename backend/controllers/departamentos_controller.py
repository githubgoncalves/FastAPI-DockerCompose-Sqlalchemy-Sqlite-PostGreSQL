import os
from fastapi import APIRouter,status
from typing import List
from schemas.colaboradores_schema import DepartamentosSchema
from fastapi.responses import JSONResponse
from services import departamento_service
from extensions.database_enum import DataBase

route = APIRouter()

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLITE.name

service = departamento_service.DepartamentosService(tipo_database)

@route.get('/departamentos', status_code=status.HTTP_200_OK,response_model=dict)
async def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        JSONResponse(content=f"API de Departamentos da {app_name} Disponivel!")
    JSONResponse(content="API de Departamentos Disponivel!")

@route.get('/departamentos/listar',status_code=status.HTTP_200_OK,response_model=List[DepartamentosSchema])
async def listar():
   departamentos_list = service.listar()
   return departamentos_list

@route.get('/departamentos/consultar/{nome}',status_code=status.HTTP_200_OK,response_model=List[DepartamentosSchema])  
async def consultar(nome):
   departamentos_list = service.consultar(nome)
   return departamentos_list

@route.post('/departamentos/incluir',status_code=status.HTTP_200_OK,response_model=str,)  
async def incluir(departamento: DepartamentosSchema):
   service.incluir(departamento)
   return JSONResponse(content="Incluido com Sucesso!")


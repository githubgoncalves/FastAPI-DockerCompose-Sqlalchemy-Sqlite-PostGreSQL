import os
from fastapi import APIRouter,status
from typing import List
from schemas.dependentes_schema import DependentesSchema
from fastapi.responses import JSONResponse
from services import dependentes_service
from extensions.database_enum import DataBase

route = APIRouter()

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLITE.name

service = dependentes_service.DependentesService(tipo_database)

@route.get('/dependentes', status_code=status.HTTP_200_OK,response_model=dict)
async def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        JSONResponse(content=f"API de Dependentes da {app_name} Disponivel!")
    JSONResponse(content="API de Dependentes Disponivel!")

@route.get('/dependentes/listar',status_code=status.HTTP_200_OK,response_model=List[DependentesSchema])
async def listar():
   dependentes_list = service.listar()
   return dependentes_list

@route.get('/dependentes/consultar/{id_colaborador}',status_code=status.HTTP_200_OK,response_model=List[DependentesSchema])  
async def consultar(id_colaborador):
   dependentes_list = service.consultar(id_colaborador)
   return dependentes_list

@route.post('/departamentos/incluir',status_code=status.HTTP_200_OK,response_model=str,)  
async def incluir(dependente: DependentesSchema):
   service.incluir(dependente)
   return JSONResponse(content="Incluido com Sucesso!")


from typing import Optional
from pydantic import BaseModel
from schemas.departamentos_schema import DepartamentosSchema


class ColaboradoresSchema(BaseModel): #serializer
    id_colaborador:int
    nome:str = None
    id_departamento: int
    departamento: Optional[DepartamentosSchema] = None
    have_dependents: bool = False
    
    class Config:
        orm_mode=True


from typing import Optional
from pydantic import BaseModel


class DepartamentosSchema(BaseModel): #serializer
    id_departamento:int = None
    nome:str = None
    
    class Config:
        orm_mode=True

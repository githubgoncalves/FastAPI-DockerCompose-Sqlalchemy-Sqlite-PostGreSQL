from typing import Optional
from pydantic import BaseModel
from schemas.colaboradores_schema import ColaboradoresSchema


class DependentesSchema(BaseModel): #serializer
    id_dependente:Optional[int] = None
    nome: str 
    id_colaborador: int
    colaborador: Optional[ColaboradoresSchema] = None
    
    class Config:
        orm_mode=True

from infra.config.database import Base
from sqlalchemy import String,Integer,Column


class DepartamentosModel(Base):
   """
   Esta classe representa os departamentos
   """
   __tablename__ = 'Departamento'

   id_departamento= Column(Integer,primary_key=True)
   nome = Column(String(255),nullable=False,unique=True)


   def to_dict(self):
        return {
            "id_departamento": self["id_departamento"],
            "nome": self["nome"]
        }


   def __rep__(self):
       return f"Departamento [name={self.nome}]"

   def __eq__(self, other):
       if (
           self.id_departamento == other.id_departamento
           and self.nome == other.nome
           
       ):
           return True
       return False



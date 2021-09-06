from infra.config.database import Base
from sqlalchemy import String,Integer,Column,ForeignKey
from sqlalchemy.orm import relationship
from models.departamentos_model import DepartamentosModel


class ColaboradoresModel(Base):
    """
    Esta classe representa os colaboradores
    """
    __tablename__ = 'Colaborador'

    id_colaborador = Column(Integer,primary_key=True)
    nome = Column(String(255),nullable=False,unique=True)
    id_departamento = Column('id_departamento', Integer, ForeignKey(DepartamentosModel.id_departamento))
    departamento = relationship(DepartamentosModel)

    def __rep__(self):
        return f"Colaborador [name={self.nome}]"

    def __eq__(self, other):
        if (
            self.id_colaborador == other.id_colaborador
            and self.nome == other.nome
            and self.id_departamento == other.id_departamento
        ):
            return True
        return False
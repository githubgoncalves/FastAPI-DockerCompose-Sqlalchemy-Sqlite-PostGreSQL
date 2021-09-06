from infra.config.database import Base
from sqlalchemy import String,Integer,Column,ForeignKey
from models.colaboradores_model import ColaboradoresModel
from sqlalchemy.orm import relationship

class DependentesModel(Base):
    """
    Esta classe representa os dependentes
    """
    __tablename__ = 'Dependente'

    id_dependente= Column(Integer,primary_key=True)
    nome = Column(String(255),nullable=False,unique=True)
    id_colaborador = Column('id_colaborador', Integer, ForeignKey(ColaboradoresModel.id_colaborador))
    colaborador = relationship(ColaboradoresModel)

    def __rep__(self):
        return f"Dependente [name={self.nome}]"

    def __eq__(self, other):
        if (
            self.id_dependente == other.id_dependente
            and self.nome == other.nome
            and self.id_colaborador == other.id_colaborador
        ):
            return True
        return False
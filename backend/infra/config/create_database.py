from .database_config import DbConnectionHandler
from sqlalchemy import MetaData,Table,Column,Integer,String,ForeignKey
from models.colaboradores_model import ColaboradoresModel
from models.departamentos_model import DepartamentosModel
from models.dependentes_model import DependentesModel
from infra.config import database_config

class CreateDataBase():

    def __init__(self,database: str):
    
        self.engine = DbConnectionHandler(database).get_engine()

        metadata = MetaData()

        departamento = Table('departamento', metadata,
            Column('id_departamento', Integer, primary_key=True),
            Column('nome', String(60), nullable=False)
        )

        colaborador = Table('colaborador', metadata,
            Column('id_colaborador', Integer, primary_key=True),
            Column('nome', String(100), nullable=False),
            Column('id_departamento', Integer, ForeignKey("departamento.id_departamento"), nullable=False),
        )

        dependente = Table('dependente', metadata,
            Column('id_dependente', Integer, primary_key=True),
            Column('nome', String(100), nullable=False),
            Column('id_colaborador', Integer, ForeignKey("colaborador.id_colaborador"), nullable=False),
        )

        metadata.create_all(self.engine,checkfirst=True)

        departamento_01 = DepartamentosModel(nome="Tecnologia - TelaVita")
        departamento_02 = DepartamentosModel(nome="RH - TelaVita")
        colaborador_01 = ColaboradoresModel(id_colaborador=1,nome='Daniel Goncalves',id_departamento=1)
        colaborador_02 = ColaboradoresModel(id_colaborador=2,nome='Amanda Cambuim',id_departamento=2)
        dependente = DependentesModel(id_dependente=1,id_colaborador=1,nome='Ayla Santana')

        with database_config.DbConnectionHandler(database) as db_connection:
            print(F"DATABASE: {database}")
            try:
                departamentos = db_connection.session.query(DepartamentosModel).all()
                if len(departamentos) == 0:
                    db_connection.session.add(departamento_01)
                    db_connection.session.commit()
                    db_connection.session.add(departamento_02)
                    db_connection.session.commit()

                colaboradores = db_connection.session.query(ColaboradoresModel).all()
                if len(colaboradores) == 0:
                    db_connection.session.add(colaborador_01)
                    db_connection.session.commit()
                    db_connection.session.add(colaborador_02)
                    db_connection.session.commit()

                dependentes = db_connection.session.query(DependentesModel).all()
                if len(dependentes) == 0:
                    db_connection.session.add(dependente)
                    db_connection.session.commit()
            except:
                raise db_connection.session.rollback()
            finally:
                db_connection.session.close()



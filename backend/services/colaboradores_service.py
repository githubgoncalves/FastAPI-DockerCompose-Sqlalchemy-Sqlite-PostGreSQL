from typing import List
from models.colaboradores_model import ColaboradoresModel
from infra.config import database_config
from schemas.colaboradores_schema import ColaboradoresSchema
from services import dependentes_service


class ColaboradoresService():
    def __init__(self, database: str):
        self.database=database

    def listar(self) -> List[ColaboradoresSchema]:
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                query_data = None
                data = (
                    db_connection.session.query(ColaboradoresModel)
                    .all()
                )

                query_data = [ColaboradoresSchema.from_orm(d) for d in data]

                for colaborador in query_data:
                    service_dependente = dependentes_service.DependentesService(self.database)
                    data_dependete = service_dependente.consultar(colaborador.id_colaborador)
                    qtd_depente = len(data_dependete)
                    if qtd_depente > 0:
                        colaborador.have_dependents = True
                        
                return query_data
            except:
                raise db_connection.session.rollback()
            finally:
                db_connection.session.close()
            return None
        return None

    def consultar(self,nome_colabortador):
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                query_data = None
                data = (
                    db_connection.session.query(ColaboradoresModel)
                    .filter_by(nome=nome_colabortador)
                    .all()
                )
                query_data = [ColaboradoresSchema.from_orm(d) for d in data]
                return query_data
            except:
                raise db_connection.session.rollback()
            finally:
                db_connection.session.close()
            return None
        return None

    def incluir(self,colaborador : ColaboradoresSchema)-> ColaboradoresSchema:
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                novo_colaborador = ColaboradoresModel(nome=colaborador.nome,id_departamento=colaborador.id_departamento)
                db_connection.session.add(novo_colaborador)
                db_connection.session.commit()

                return ColaboradoresSchema(
                    id_colaborador =novo_colaborador.id_colaborador,
                    nome=novo_colaborador.nome,
                    id_departamento=novo_colaborador.id_departamento
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
        return None

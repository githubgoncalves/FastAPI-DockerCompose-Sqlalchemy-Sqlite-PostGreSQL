from typing import List
from models.dependentes_model import DependentesModel
from infra.config import database_config
from schemas.dependentes_schema import DependentesSchema


class DependentesService():
    def __init__(self, database: str):
        self.database=database

    def listar(self) -> DependentesSchema:
        with database_config.DbConnectionHandler(self.database) as db_connection:
                try:
                    query_data = None
                    data = (
                        db_connection.session.query(DependentesModel)
                        .all()
                    )
                    query_data = [DependentesSchema.from_orm(d) for d in data]
                    return query_data
                except:
                    raise db_connection.session.rollback()
                finally:
                    db_connection.session.close()
                return None
        return None

    def consultar(self,id_colaborador) -> DependentesSchema:
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                query_data = None
                data = (
                    db_connection.session.query(DependentesModel)
                    .filter_by(id_colaborador=id_colaborador)
                    .all()
                )
                query_data = [DependentesSchema.from_orm(d) for d in data]
                return query_data
            except:
                raise db_connection.session.rollback()
            finally:
                db_connection.session.close()
            return None
        return None

    def incluir(self,dependente: DependentesSchema) -> DependentesSchema:
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                novo_departamento = DependentesModel(nome=dependente.nome,id_colaborador=dependente.id_colaborador)
                db_connection.session.add(novo_departamento)
                db_connection.session.commit()

                return DependentesSchema(
                    id_dependentes=dependente.id_dependente,
                    id_colaborador=dependente.id_colaborador,
                    nome=dependente.nome
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
        return None

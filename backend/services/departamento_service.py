
from typing import List
from models.departamentos_model import DepartamentosModel
from infra.config import database_config
from schemas.departamentos_schema import DepartamentosSchema


class DepartamentosService():
    def __init__(self, database: str):
        self.database=database

    def listar(self) -> List[DepartamentosSchema]:
        with database_config.DbConnectionHandler(self.database) as db_connection:
                try:
                    query_data = None
                    data = (
                        db_connection.session.query(DepartamentosModel)
                        .all()
                    )

                    query_data = [DepartamentosSchema.from_orm(d) for d in data]

                    return query_data
                except:
                    raise db_connection.session.rollback()
                finally:
                    db_connection.session.close()
                return None
        return None

    def consultar(self,nome_departamento) -> DepartamentosSchema:
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                query_data = None
                data = (
                    db_connection.session.query(DepartamentosModel)
                    .filter_by(nome=nome_departamento)
                    .all()
                )

                query_data = [DepartamentosSchema.from_orm(d) for d in data]

                return query_data
            except:
                raise db_connection.session.rollback()
            finally:
                db_connection.session.close()
            return None
        return None

    def incluir(self,departamento: DepartamentosSchema) -> DepartamentosSchema:
        with database_config.DbConnectionHandler(self.database) as db_connection:
            try:
                novo_departamento = DepartamentosModel(id_departamento=departamento.id_departamento,nome=departamento.nome)
                db_connection.session.add(novo_departamento)
                db_connection.session.commit()

                return DepartamentosSchema(
                    id_colaborador=novo_departamento.id_departamento,
                    nome=novo_departamento.nome
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
        return None

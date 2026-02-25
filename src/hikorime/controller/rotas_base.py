from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from pydantic import BaseModel
from hikorime.service.base_service import BaseService


class RotasBase:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.service = BaseService
        self.router = APIRouter(prefix=f"/{table_name}", tags=[table_name.capitalize()])
        self._routes()

    def _routes(self):
        @self.router.get("/get/{id}")
        def get_by_id(self, id: int):
            """
            Busca pelo o id de.
            """
            result = self.service.get_by_id(id)
            if not result:
                raise HTTPException(
                    status_code=404,
                    detail=f"O com id {id} nao encontrado.",
                )
            return result

        @self.router.get("/search/{column_name}/{value}")
        def get_by_column(self, column_name: str, value: str) -> Dict[str, Any]:
            """
            Busca por uma coluna específica em
            """
            result = self.service.get_by_column_name(column_name, value)
            if not result:
                raise HTTPException(
                    status_code=404,
                    detail=f"O com {column_name} = {value} não encontrado.",
                )
            return result

        @self.router.post("/create")
        def create(self, dados: BaseModel) -> Dict[str, Any]:
            """
            Cria um novo.
            """
            result = self.service.save(dados)
            return {"msg": f"{self.table_name} criado com sucesso", "data": result}

        @self.router.delete("/delete/{id}")
        def delete_by_id(self, id: int) -> Dict[str, Any]:
            """
            Deleta um pelo ID.
            """
            result = self.service.delete_by_id(id)
            if result is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"O de id {id} não encontrado para deletar.",
                )
            return {"msg": f"O de Id {id} deletado com sucesso."}

        # # TODO:
        # @self.router.patch("/{id}")
        # def update_voo(self, id: int, voo: VooUpdateRequest) -> Dict[str, Any]:
        #     """
        #     Atualiza os dados de uma ou mais linhas.
        #     """
        #     voo_data = voo.dict(
        #         exclude_unset=True
        #     )  # Exclui os campos não enviados no update
        #     result = self.service.put_in_table(id, voo_data)
        #     if result is None:
        #         raise HTTPException(
        #             status_code=404,
        #             detail=f"Voo com ID {id} não encontrado para atualizar.",
        #         )
        #     return {"msg": f"Voo com ID {id} atualizado com sucesso.", "data": result}

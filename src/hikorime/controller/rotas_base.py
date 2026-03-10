from typing import List, Type, TypeVar

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from hikorime.service.base_service import BaseService

# Tipo genérico que deve ser uma subclasse de BaseModel
SchemaType = TypeVar("SchemaType", bound=BaseModel)


# pyright: reportInvalidTypeForm=false
def create_generic_router(service: BaseService, schema: Type[SchemaType]) -> APIRouter:
    """
    Cria um APIRouter com rotas CRUD padrao para uma entidade especifica.

    Args:
        table_name: O nome da entidade (usado no prefixo da URL e tags).
        schema: A classe Pydantic (BaseModel) usada para validaçao.
        service: A instancia do servico usado.

    Returns:
        APIRouter: Um roteador configurado e pronto para ser usado em outros controllers.
    """

    table_name = service.table_name()

    router = APIRouter(prefix=f"/{table_name}", tags=[table_name.capitalize()])

    @router.get("/", response_model=List[schema])
    def get_all():
        """Retorna todos os registros da entidade."""
        return service.get_all() # TODO: ????

    @router.get("/{id}", response_model=schema)
    def get_by_id(id: int):
        """Busca um registro específico pelo ID."""
        result = service.get_by_id(id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{table_name.capitalize()} com ID {id} não encontrado.",
            )
        return result

    @router.post("/", response_model=schema, status_code=status.HTTP_201_CREATED)
    def create(dados: schema):
        """Cria uma nova entidade baseada no esquema fornecido."""
        try:
            return service.save(dados)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Erro ao criar {table_name}: {str(e)}",
            )

    @router.patch("/{id}", response_model=schema)
    def update(id: int, dados: schema):
        """
        Atualiza parcialmente uma entidade pelo ID.
        Campos nao enviados no JSON não serao alterados.
        """
        # Extrai apenas os campos que o usuário realmente enviou
        update_data = dados.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nenhum dado fornecido para atualização.",
            )

        result = service.update_column(id, update_data)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"ID {id} não encontrado para atualização.",
            )
        return result

    @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete(id: int):
        """Remove um registro permanentemente pelo ID."""
        success = service.delete_by_id(id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Não foi possível deletar: ID {id} não encontrado.",
            )
        return None

    return router

from datetime import date

from pydantic import BaseModel, EmailStr, Field

from hikorime.models.enums.tipo_usuario import TipoUsuario


class UsuarioBase(BaseModel):
    #modelo de entrada de dados de usuario - parte de cadastro de novo usuario
    nome: str
    #data_nascimento: date
    # TODO: ADICIONAR DATA DE NASCIMENTO
    cpf: str = Field(..., min_length=11, max_length=11)
    tipo: TipoUsuario
    email: EmailStr
    senha: str


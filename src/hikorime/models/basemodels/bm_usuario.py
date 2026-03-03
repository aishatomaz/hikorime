from pydantic import BaseModel, EmailStr, Field

from hikorime.models.enums.tipo_usuario import TipoUsuario


class UsuarioBase(BaseModel):
    #modelo de entrada de dados de usuario - parte de cadastro de novo usuario
    nome: str
    email: EmailStr
    cpf: str = Field(..., min_length=11, max_length=11)
    senha: str
    tipo: TipoUsuario

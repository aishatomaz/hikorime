from pydantic import BaseModel, EmailStr, Field

from hikorime.models.enums.tipo_usuario import TipoUsuario


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    cpf: str = Field(..., min_length=11, max_length=11)
    senha: str
    tipo: TipoUsuario

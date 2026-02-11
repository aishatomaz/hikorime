from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum


class TipoUsuario(str, Enum):
    PASSAGEIRO = "passageiro"
    FUNCIONARIO = "funcionario"


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    cpf: str = Field(..., min_length=11, max_length=11)


class UsuarioCreate(UsuarioBase):
    senha: str
    tipo: TipoUsuario


class PassageiroCreate(UsuarioCreate):
    tipo: TipoUsuario = TipoUsuario.PASSAGEIRO
    passaporte: Optional[str] = None


class FuncionarioCreate(UsuarioCreate):
    tipo: TipoUsuario = TipoUsuario.FUNCIONARIO
    cargo: str
    matricula: str


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


class UsuarioResponse(UsuarioBase):
    id: int
    tipo: TipoUsuario

    class Config:
        from_attributes = True

from datetime import date

from pydantic import BaseModel, EmailStr, Field

from hikorime.models.enums.tipo_usuario import TipoUsuario


class UsuarioBase(BaseModel):
    """
    Modelo base para o usuário, utilizado para cadastro e autenticação.

    Args:
        nome (str): O nome completo do usuário.
        data_nascimento (date): A data de nascimento do usuário.
        cpf (str): O CPF do usuário, deve conter exatamente 11 caracteres.
        tipo_usuario (TipoUsuario): O tipo de usuário, definido pelo enum TipoUsuario.
        email (EmailStr): O endereço de email do usuário, validado como um email válido.
        senha (str): A senha do usuário, armazenada em formato hash para segurança.
    
    Returns:
        UsuarioBase: Um objeto do tipo UsuarioBase contendo os dados do usuário.
    """

    # modelo de entrada de dados de usuario - parte de cadastro de novo usuario
    nome: str
    data_nascimento: date
    cpf: str = Field(..., min_length=11, max_length=11)
    tipo_usuario: TipoUsuario
    email: EmailStr
    senha: str


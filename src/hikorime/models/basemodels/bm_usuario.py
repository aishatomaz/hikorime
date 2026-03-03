<<<<<<< HEAD
from pydantic import EmailStr, Field, validator
from hikorime.models.enums.tipo_usuario import TipoUsuario
from hikorime.models.basemodels.bm_login import PasswordBase

class UsuarioBase(PasswordBase):
 
    """
    Modelo de entrada de dados de usuário - parte de cadastro de novo usuário.
    Herda a validação de senha de PasswordBase.
    """
    
    nome: str
    email: EmailStr
    cpf: str = Field(..., min_length=11, max_length=11)
    tipo: TipoUsuario

    @validator('cpf')
    def validate_cpf(cls, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise ValueError('CPF deve ter 11 dígitos.')

        if cpf == cpf[0] * 11:
            raise ValueError('CPF inválido.')

        for i in range(9, 11):
            soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
            digito = 11 - (soma % 11)
            if digito > 9:
                digito = 0
            if int(cpf[i]) != digito:
                raise ValueError('CPF inválido.')
        return cpf
=======
from pydantic import BaseModel, EmailStr, Field

from hikorime.models.enums.tipo_usuario import TipoUsuario


class UsuarioBase(BaseModel):
    #modelo de entrada de dados de usuario - parte de cadastro de novo usuario
    nome: str
    email: EmailStr
    cpf: str = Field(..., min_length=11, max_length=11)
    senha: str
    tipo: TipoUsuario
>>>>>>> ui_test

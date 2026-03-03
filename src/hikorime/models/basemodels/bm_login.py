<<<<<<< HEAD
from pydantic import EmailStr, BaseModel, validator

class PasswordBase(BaseModel):
    """
    Classe base para validação de senha robusta.
    """
    senha: str

    @validator('senha')
    def validate_senha_strength(cls, senha):
        if len(senha) < 8:
            raise ValueError('A senha deve ter no mínimo 8 caracteres.')
        if not any(char.isupper() for char in senha):
            raise ValueError('A senha deve conter pelo menos uma letra maiúscula.')
        if not any(char.islower() for char in senha):
            raise ValueError('A senha deve conter pelo menos uma letra minúscula.')
        if not any(char.isdigit() for char in senha):
            raise ValueError('A senha deve conter pelo menos um número.')
        if not any(not char.isalnum() for char in senha):
            raise ValueError('A senha deve conter pelo menos um caractere especial.')
        return senha

class login_request(PasswordBase):
    """
    Formato de entrada para login de qualquer usuário.
    """
    email: EmailStr
=======
from pydantic import EmailStr, BaseModel


class LoginRequest(BaseModel):
    # formato de entrada para login de qualquer usuario
    email: EmailStr
    senha: str

>>>>>>> ui_test

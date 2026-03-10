from pydantic import EmailStr, BaseModel


class LoginRequest(BaseModel):
    """
    Modelo de dados para a requisição de login.
    
    Args: 
        email (EmailStr): O endereço de email do usuário.
        senha (str): A senha do usuário.
    
    Returns:
        LoginRequest: Um objeto contendo os dados de login do usuário.
    """
    # formato de entrada para login de qualquer usuario
    email: EmailStr
    senha: str


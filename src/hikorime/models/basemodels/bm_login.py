from pydantic import EmailStr, BaseModel


class LoginRequest(BaseModel):
    # formato de entrada para login de qualquer usuario
    email: EmailStr
    senha: str

login_request = LoginRequest
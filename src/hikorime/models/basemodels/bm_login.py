from pydantic import EmailStr, BaseModel, Field

class login_request():
    #formato de entrada para login de qualquer usuario
    email: EmailStr
    senha: str
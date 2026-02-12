
from pydantic import EmailStr


class login_request():

    # TODO: fazer hash da senha
    email: EmailStr
    senha: str
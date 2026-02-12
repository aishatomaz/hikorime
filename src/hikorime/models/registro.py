from pydantic import BaseModel, EmailStr

# colocado os atributos em base_usuario
# class UsuarioCreate(UsuarioBase):


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


#class UsuarioResponse(UsuarioBase):
#    id: int
#    tipo: TipoUsuario
#
#    class Config:
#        from_attributes = True

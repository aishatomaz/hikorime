from hikorime.models.enums.tipo_usuario import TipoUsuario
from hikorime.models.base_usuario import UsuarioBase


class Funcionario(UsuarioBase):
    tipo: TipoUsuario = TipoUsuario.FUNCIONARIO
    cargo: str
    matricula: str

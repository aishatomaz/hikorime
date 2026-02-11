from hikorime.models.enums.tipo_usuario import TipoUsuario
from hikorime.models.usuario_base import UsuarioBase


class Funcionario(UsuarioBase):
    tipo: TipoUsuario = TipoUsuario.FUNCIONARIO
    cargo: str
    matricula: str

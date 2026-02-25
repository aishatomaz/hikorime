from hikorime.models.enums.tipo_usuario import TipoUsuario
from hikorime.models.basemodels.bm_usuario import UsuarioBase


class Funcionario(UsuarioBase):
    #base de entrada para cadastro de funcionario solicitando dados especificos do cargo
    tipo: TipoUsuario = TipoUsuario.FUNCIONARIO
    cargo: str
    matricula: str

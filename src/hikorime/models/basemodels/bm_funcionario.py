from hikorime.models.enums.tipo_usuario import TipoUsuario
from hikorime.models.basemodels.bm_usuario import UsuarioBase


class Funcionario(UsuarioBase):
    """
    Modelo de dados para um funcionário, herda os campos do modelo de usuário e adiciona campos específicos para funcionários.

    Args: 
        UsuarioBase: Modelo base de usuário que inclui campos comuns a todos os tipos de usuários, como nome, email, cargo, e etc.
    Returns:
        Funcionario: Um objeto do tipo Funcionario com os campos específicos para um funcionário, como cargo e matrícula.
    """
    # base de entrada para cadastro de funcionario solicitando dados especificos do cargo
    tipo_usuario: TipoUsuario = TipoUsuario.FUNCIONARIO
    cargo: str
    matricula: str

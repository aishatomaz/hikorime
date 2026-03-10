from typing import Optional

from hikorime.models.basemodels.bm_usuario import UsuarioBase
from hikorime.models.enums.tipo_passaporte import TipoPassaporte
from hikorime.models.enums.tipo_usuario import TipoUsuario


class Passageiro(UsuarioBase):
    """
    Modelo de Passageiro, herda de UsuarioBase, possui os seguintes campos adicionais:
     - tipo_usuario: TipoUsuario (definido como PASSAGEIRO)
     - codigo_passaporte: str (código do passaporte do passageiro)
     - tipo_passaporte: TipoPassaporte (tipo do passaporte do passageiro)   

     Args: 
        UsuarioBase: herda os campos de UsuarioBase (id, nome, email, senha, data_criacao)
    
    Returns:
        Passageiro: objeto do tipo Passageiro com os campos definidos
    """
    # base para autenticação de passageiro - passaporte solicitado para realizar cadasto
    tipo_usuario: TipoUsuario = TipoUsuario.PASSAGEIRO
    codigo_passaporte: str
    tipo_passaporte: TipoPassaporte
    
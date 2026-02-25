from typing import Optional
from hikorime.models.basemodels.bm_usuario import UsuarioBase
from hikorime.models.enums.tipo_usuario import TipoUsuario


class Passageiro(UsuarioBase):
    #base para autenticação de passageiro - passaporte solicitado para realizar cadasto
    tipo: TipoUsuario = TipoUsuario.PASSAGEIRO
    passaporte: Optional[str] = None

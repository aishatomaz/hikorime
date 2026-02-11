from typing import Optional
from hikorime.models.usuario_base import UsuarioBase
from hikorime.models.enums.tipo_usuario import TipoUsuario


class Passageiro(UsuarioBase):
    tipo: TipoUsuario = TipoUsuario.PASSAGEIRO
    passaporte: Optional[str] = None

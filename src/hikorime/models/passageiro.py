from typing import Optional
from hikorime.models.base_usuario import UsuarioBase
from hikorime.models.enums.tipo_usuario import TipoUsuario


class Passageiro(UsuarioBase):
    tipo: TipoUsuario = TipoUsuario.PASSAGEIRO
    passaporte: Optional[str] = None

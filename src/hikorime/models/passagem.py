'''...'''

class Passagem:
    def __init__(self, assento, valor_final, notificacao: NotificacaoCompra):
        self.assento = assento
        self.valor_final = valor_final
        self.notificacao = notificacao

    @property
    def assento(self):
        return self._assento
    
    @assento.setter
    def assento(self, assento_valido):
        if not isinstance(assento_valido, int):
            raise ValueError("Número de assento inválido")
        else:
            self._assento = assento_valido
    
    def verificar_disponibilidade_assento(self):
        return
    
    def escolher_assento(self):
        return
    

from datetime import date
from hikorime.models.compra import Compra
from hikorime.models.pagamento import Pagamento
from hikorime.models.passagem import Passagem

'''Após comprar uma passagem, o passageiro deve receber a notificação informando sobre a passagem, o voo e a compra.'''
class NotificationModel(): 
    def __init__(self, passagem: Passagem, compra: Compra, voo: voo, tipo_pagamento: Pagamento,  prox_partida = False,):
        
        self.passagem = passagem
        self.compra = compra
        self.voo = voo
        self.prox_partida = prox_partida
        self.tipo_pagamento = tipo_pagamento
    
    def criarPassagem(self, nome_completo: str, companhia_aerea: str, numero_voo: int, data_voo: date) :
         

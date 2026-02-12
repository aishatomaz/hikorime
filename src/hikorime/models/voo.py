from datetime import datetime

class Voo:
    def __init__(self, data_hora_partida: datetime, data_hora_chegada: datetime, data_hora_chegada_prevista: datetime, local_origem: str, local_destino: str, assentos_ocupados: int):
        self.data_hora_partida = data_hora_partida
        self.data_hora_chegada = data_hora_chegada
        self.data_hora_chegada_prevista = data_hora_chegada_prevista
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.assentos_ocupados = assentos_ocupados

    @property
    def data_hora_partida(self):
        return self.__data_hora_partida

    @data_hora_partida.setter
    def data_hora_partida(self, data_hora_partida_valida):
        if not isinstance(data_hora_partida_valida, datetime):
            raise ValueError("A data de partida deve ser do tipo date.")
        self.__data_hora_partida = data_hora_partida_valida

    @property
    def data_hora_chegada(self):
        return self.__data_hora_chegada
    
    @data_hora_chegada.setter
    def data_hora_chegada(self, data_hora_chegada_valida):
        if not isinstance(data_hora_chegada_valida, datetime):
            raise ValueError("A data e hora de chegada deve ser do tipo datetime.")
        self.__data_hora_chegada = data_hora_chegada_valida

    @property
    def data_hora_chegada_prevista(self):
        return self.__data_hora_chegada_prevista
    
    @data_hora_chegada_prevista.setter
    def data_hora_chegada_prevista(self, data_hora_chegada_prevista_valida):

        if not isinstance(data_hora_chegada_prevista_valida, datetime):
            raise ValueError("A data e hora de chegada previsto deve ser do tipo datetime.")
        self.__data_hora_chegada_prevista = data_hora_chegada_prevista_valida

    @property
    def local_origem(self):
        return self.__local_origem

    @local_origem.setter
    def local_origem(self, local_origem_valida):
        if not isinstance(local_origem_valida, str):
            raise ValueError("O local de origem deve ser do tipo str.")

        self.__local_origem = local_origem_valida    
        
    @property
    def assentos_ocupados(self):
        return self.__assentos_ocupados

    @assentos_ocupados.setter
    def assentos_ocupados(self, assentos_ocupados_valida):
        if not isinstance(assentos_ocupados_valida, int):
            raise ValueError("A quantidade de passageiros deve ser do tipo int.")
        
        if assentos_ocupados_valida <= 0:
            raise ValueError("A quantidade de passageiros deve ser maior que zero.")
        self.__assentos_ocupados = assentos_ocupados_valida

    @property
    def local_destino(self):
        return self.__local_destino

    @local_destino.setter
    def local_destino(self, local_destino_valida):
        if not isinstance(local_destino_valida, str):
            raise ValueError("O local de destino deve ser do tipo str.")
        self.__local_destino = local_destino_valida
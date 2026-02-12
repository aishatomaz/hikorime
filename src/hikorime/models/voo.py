from datetime import (
    date,
    datetime,
)


class Voo:
    def __init__(self, data_saida: date, horario_chegada_previsto: datetime, horario_saida: datetime, local_origem: str, local_destino: str, qtd_passageiros: int):
        self.data_saida = data_saida
        self.horario_chegada_previsto = horario_chegada_previsto
        self.horario_saida = horario_saida
        self.local_origem = local_origem = local_origem
        self.local_destino = local_destino = local_destino
        self.qtd_passageiros = qtd_passageiros

    @property
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, value):
        self.__data_saida = value

    @property
    def horario_chegada_previsto(self):
        return self.__horario_chegada_previsto
    
    @horario_chegada_previsto.setter
    def horario_chegada_previsto(self, horario_chegada_previsto_valida):

        if not isinstance(horario_chegada_previsto_valida, datetime):
            raise ValueError("O horário de chegada previsto deve ser do tipo datetime.")
        self.__horario_chegada_previsto = horario_chegada_previsto_valida

    @property
    def horario_saida(self):
        return self.__horario_saida
    
    @horario_saida.setter
    def horario_saida(self, value):
        self.__horario_saida = value

    @property
    def local_origem(self):
        return self.__local_origem

    @local_origem.setter
    def local_origem(self, local_origem_valida):
        if not isinstance(local_origem_valida, str):
            raise ValueError("O local de origem deve ser do tipo str.")

        self.__local_origem = local_origem_valida    
        
    @property
    def qdt_passageiros(self):
        return self.__qtd_passageiros

    @qdt_passageiros.setter
    def qtd_passageiros(self, qtd_passageiros_valida):
        if not isinstance(qtd_passageiros_valida, int):
            raise ValueError("A quantidade de passageiros deve ser do tipo int.")
        self.__qtd_passageiros = qtd_passageiros_valida

    @property
    def local_destino(self):
        return self.__local_destino

    @local_destino.setter
    def local_destino(self, local_destino_valida):
        if not isinstance(local_destino_valida, str):
            raise ValueError("O local de destino deve ser do tipo str.")
        self.__local_destino = local_destino_valida
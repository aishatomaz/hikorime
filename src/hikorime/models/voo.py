from datetime import datetime

class Voo:
    def __init__(self, data_hora_partida: datetime, data_hora_chegada: datetime,
            local_origem: str, local_destino: str, assentos_ocupados: int, valor_passagens: float):
        self.data_hora_partida = data_hora_partida
        self.data_hora_chegada = data_hora_chegada
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.assentos_ocupados = assentos_ocupados
        self.valor_passagens = valor_passagens

    @property
    def data_hora_partida(self):
        return self.__data_hora_partida

    @data_hora_partida.setter
    def data_hora_partida(self, data_hora_partida_valida):
        if not isinstance(data_hora_partida_valida, datetime):
            raise TypeError("data_hora_partida deve ser um objeto datetime")
        self.__data_hora_partida = data_hora_partida_valida

    @property
    def data_hora_chegada(self):
        return self.__data_hora_chegada
    
    @data_hora_chegada.setter
    def data_hora_chegada(self, data_hora_chegada_valida):
        if not isinstance(data_hora_chegada_valida, datetime):
            raise TypeError("data_hora_chegada deve ser um objeto datetime")
        if data_hora_chegada_valida <= self.data_hora_partida:
            raise ValueError("data_hora_chegada deve ser depois da partida")
        self.__data_hora_chegada = data_hora_chegada_valida

    
    @property
    def local_origem(self):
        return self.__local_origem

    @local_origem.setter
    def local_origem(self, local_origem_valida):
        try:
            str(local_origem_valida)
        except ValueError:  
            raise ValueError("local deve ser string")
        
        if not local_origem_valida:
                raise ValueError("O local de origem não pode ser vazio.")

        self.__local_origem = local_origem_valida    
        
    @property
    def assentos_ocupados(self):
        return self.__assentos_ocupados

    @assentos_ocupados.setter
    def assentos_ocupados(self, assentos_ocupados_valida):
        try:
            str(assentos_ocupados_valida)
        except ValueError:  
            raise ValueError("Os assentos devem ser representados por valor numerico")
        
        if assentos_ocupados_valida <= 0:
            raise ValueError("A quantidade de assentos ocupados deve ser maior que zero.")
        self.__assentos_ocupados = assentos_ocupados_valida

    @property
    def local_destino(self):
        return self.__local_destino

    @local_destino.setter
    def local_destino(self, local_destino_valida):
        try:
            str(local_destino_valida)
        except ValueError:  
            raise ValueError("local deve ser string")
        
        if not local_destino_valida:
            raise ValueError("O local de destino não pode ser vazio.")
        self.__local_destino = local_destino_valida

    @property
    def valor_passagens(self):
        return self.__valor_passagens
    @valor_passagens.setter
    def valor_passagens(self, valor_valido):
        try:
            float(valor_valido)
        except ValueError:  
            raise ValueError("valor da passagem ser ser numerico")
        if not valor_valido or valor_valido == 0:
            raise ValueError("valor não pode ser nulo.")
        else:
            self.__valor_passagens = valor_valido
        
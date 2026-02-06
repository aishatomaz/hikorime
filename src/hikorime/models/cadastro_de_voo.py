from datetime import date, time
from statusvoo import StatusVoo
from repository.repository_connection import RepositoryConnection
from service.const_voo import ConstantesVoo

const = ConstantesVoo()

class CadastrarVoo:
    # recolhe dados do voo para o banco de dados, comissário deve preencher
    def __init__(
        self,
        data_saida,
        data_cheg,
        hora_saida,
        hora_chega,
        local_saida,
        destino,
        id_piloto,
        aviao,
        quant_vagas,
        status_voo=StatusVoo,
    ):
        self.data_saida = data_saida
        self.data_cheg = data_cheg
        self.hora_saida = hora_saida
        self.hora_chega = hora_chega
        self.local_saida = local_saida
        self.destino = destino
        self.piloto = id_piloto
        self.aviao = aviao
        self.quant_vagas = quant_vagas
        self.status_voo = status_voo

    # encapsulamento dos atributos
    @property
    # para datas
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, data_valida):
        if not isinstance(data_valida, date):
            raise ValueError("Data inválida")
        else:
            self.__data_saida = data_valida

    @property
    def data_chega(self):
        return self.__data_chega

    @data_chega.setter
    def data_chega(self, data_vali_chegada):
        if not isinstance(data_vali_chegada, date):
            raise ValueError("Data inválida")
        else:
            self.__data_chega = data_vali_chegada

    @property
    # para horarios
    def hora_saida(self):
        return self.__hora_saida

    @hora_saida.setter
    def hora_saida(self, hora_valida):
        if not isinstance(hora_valida, time):
            raise ValueError("Hora inválida")
        else:
            self.__hora_saida = hora_valida

    @property
    def hora_chega(self):
        return self.__hora_chega

    @hora_chega.setter
    def hora_chega(self, hora_vali_chegada):
        if not isinstance(hora_vali_chegada, time):
            raise ValueError("Hora inválida")
        else:
            self.__hora_chega = hora_vali_chegada

    @property
    # para locais
    def local_saida(self):
        return self.__local_saida

    @local_saida.setter
    def local_saida(self, local_valido):

        if not isinstance(local_valido, str) or len(local_valido < const.qtd_min_caracteres):

            raise ValueError("Por favor, imforme um local válido.")
        else:
            self.__local_saida = local_valido

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino_valido):
        if not isinstance(destino_valido, str) or len(self.__destino < const.qtd_min_caracteres):
            raise ValueError("Destino inválido")
        else:
            self.__destino = destino_valido

    @property
    # para piloto
    def id_piloto(self):
        return self.__piloto

    @id_piloto.setter
    def id_piloto(self, id_valido):
        if not isinstance(id_valido, int):
            raise ValueError("O id do piloto deve ser um valor numérico inteiro")
        else:
            self.__piloto = id_valido

    @property
    # para aviao
    def aviao(self):
        return self.__aviao

    @aviao.setter
    def aviao(self, aviao_valido):
        if not isinstance(aviao_valido, int):
            raise ValueError("O avião não pode ser identificado")
        else:
            self.__aviao = aviao_valido

    @property
    # para quantidade de vagas
    def quant_vagas(self):
        return self.__quant_vagas

    @quant_vagas.setter
    def quant_vagas(self, quant_valida):
        if not isinstance(quant_valida, int):
            raise ValueError("Quantidade de vagas deve ser um valor inteiro.")
        elif quant_valida > ConstantesVoo.qtd_max_passageiros or quant_valida <= 0:
            raise ValueError("Quantidade inválida")
        else:
            self.__quant_vagas = quant_valida

    def cadastrar_voo(self):
        # conectar ao banco
        self.conectar.query()

        # salvar os dados na tabela de voos

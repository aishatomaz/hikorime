from hikorime.cli.utils import parse_date, parse_time
from hikorime.service.cadastro_voo import CadastroVooService
from hikorime.models.enums.status_voo import StatusVoo
from hikorime.schemas.voo import VooModelo


class ComissarioRotasCLI:
    def __init__(self):
        self.service = CadastroVooService()

    def cadastrar_voo(self):
        print("\n CADASTRO DE VOO ")

        dados = VooModelo(
            data_saida=parse_date(input("Data saída (YYYY-MM-DD): ")),
            data_cheg=parse_date(input("Data chegada (YYYY-MM-DD): ")),
            hora_saida=parse_time(input("Hora saída (HH:MM): ")),
            hora_chega=parse_time(input("Hora chegada (HH:MM): ")),
            local_saida=input("Local saída: "),
            destino=input("Destino: "),
            id_piloto=int(input("ID do piloto: ")),
            aviao=input("Avião: "),
            quant_vagas=int(input("Quantidade de vagas: ")),
        )

        self.service.save(**dados.model_dump(), status_voo=StatusVoo.DISPONIVEL)

        print("✔ Voo cadastrado com sucesso!")

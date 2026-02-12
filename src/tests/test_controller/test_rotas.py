from datetime import date, time
from hikorime.controller.rotas_comissario import cadastro_voo


class TesteRotas:
    cadastro_rota = {
        data_saida: "22/02/2026",
        data_cheg: "22/03/2026",
        "20:22": hora_saida,
        "21:25": hora_chega,
        "guarulhos": local_saida,
        "sergipe": destino,
        "1": id_piloto,
        "an - 096": aviao,
        "74": quant_vagas,
    }

    def test_cadastro_voo(self):
        voo = cadastro_voo()

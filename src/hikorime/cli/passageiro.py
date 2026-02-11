from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.passagem_service import PassagemService
from hikorime.service.visualizacao_de_voo import VisualizarVoos


class PassageiroRotasCLI:
    def comprar_passagem(self):
        print("\n COMPRA DE PASSAGEM ")

        dados = {
            "assento": int(input("Assento: ")),
            "id_voo": int(input("ID do voo: ")),
            "id_passageiro": int(input("ID do passageiro: ")),
            "valor_pago": float(input("Valor pago: ")),
        }

        repo = RepositoryQuerys(table_name="passagens_vendidas")
        repo.save(**dados)

        print("✔ Compra realizada com sucesso!")

    def ver_minhas_passagens(self):
        id_passageiro = int(input("ID do passageiro: "))

        service = PassagemService()
        passagens = service.get_by_passageiro(id_passageiro)

        if not passagens:
            print("Nenhuma passagem encontrada.")
            return

        print("\n MINHAS PASSAGENS ")

        for p in passagens:
            print(
                f"""
                     Passagem #{p["id"]}
                     Voo: {p["local_saida"]} → {p["destino"]}
                     Data: {p["data_saida"]} às {p["hora_saida"]}
                     Assento: {p["assento"]}
                     Valor pago: R$ {p["valor_pago"]}
                     Comprada em: {p["data_compra"]}
                 """
            )

    def visualizar_voos(self):
        print("Não implementado")

    #    voos = VisualizarVoos().get_all()
    #    # TODO: confirmar com o criador original
    #
    #    if not voos:
    #        print("Nenhum voo encontrado.")
    #        return
    #
    #    for voo in voos:
    #        print(dict(voo))

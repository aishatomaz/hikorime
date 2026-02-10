from hikorime.cli.registro import RegistroRotas
from hikorime.cli.comissario import ComissarioRotasCLI
from hikorime.cli.passageiro import PassageiroRotasCLI
from hikorime.cli.menus import Menus
from fastapi import HTTPException


class RegistroOpcoes:
    def __init__(self):
        self.registro = RegistroRotas()
        self.comissario = ComissarioRotasCLI()
        self.passageiro = PassageiroRotasCLI()

    def executar(self):
        while True:
            opcao = Menus().menu_iniciar()

            try:
                match opcao:
                    case "1":
                        self.registro.login()
                    case "2":
                        self.registro.registrar_passageiro()
                    case "3":
                        self.registro.registrar_funcionario()
                    case "4":
                        self.comissario.cadastrar_voo()
                    #case "5":
                    #    self.passageiro.comprar_passagem()
                    #case "6":
                    #    self.passageiro.ver_minhas_passagens()
                    #case "7":
                    #    self.passageiro.visualizar_voos()
                    case "0":
                        print("Saindo...")
                        break
                    case _:
                        print("Opção inválida")

            except HTTPException as e:
                print(e.detail)
            except Exception as e:
                print("Erro inesperado:", e)

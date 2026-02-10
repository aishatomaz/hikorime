from hikorime.cli.rotas import RegistroRotas
from hikorime.cli.menus import Menus
from fastapi import HTTPException


class RegistroOpcoes:
    def __init__(self):
        self.rotas = RegistroRotas()

    def executar(self):
        while True:
            opcao = Menus().menu_iniciar()

            try:
                if opcao == "1":
                    self.rotas.login()

                elif opcao == "2":
                    self.rotas.registrar_passageiro()

                elif opcao == "3":
                    self.rotas.registrar_funcionario()

                elif opcao == "0":
                    print("Saindo...")
                    break

                else:
                    print("Opção inválida")

            except HTTPException as e:
                # reaproveita erro do service
                print(f"{e.detail}")

            except Exception as e:
                print("Erro inesperado: ", e)

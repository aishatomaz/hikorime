from hikorime.registro.service import RegistroService
from hikorime.registro.modelos import (
    PassageiroCreate,
    FuncionarioCreate,
    LoginRequest,
)
# Cada calsse deve ser separado por um arquivo, penso que fica melhor, discutir na proxima reuniao isso.


class RegistroRotas:
    def __init__(self):
        self.service = RegistroService()

    def login(self):
        print("\n LOGIN ")
        email = input("Email: ")
        senha = input("Senha: ")

        dados = LoginRequest(email=email, senha=senha)

        resultado = self.service.login(dados)
        print("Resultado: ", resultado["message"])
        print("Usuário:", resultado["usuario"])

    def registrar_passageiro(self):
        print("\n CADASTRO DE PASSAGEIRO ")
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF (11 dígitos): ")
        senha = input("Senha: ")
        passaporte = input("Passaporte (opcional): ")

        dados = PassageiroCreate(
            nome=nome,
            email=email,
            cpf=cpf,
            senha=senha,
            passaporte=passaporte,
        )

        resultado = self.service.registrar_passageiro(dados)
        print("resultado: ", resultado["message"])
        print("ID:", resultado["id"])

    def registrar_funcionario(self):
        print("\nCADASTRO DE FUNCIONÁRIO")
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF (11 dígitos): ")
        senha = input("Senha: ")
        cargo = input("Cargo: ")
        matricula = input("Matrícula: ")

        dados = FuncionarioCreate(
            nome=nome,
            email=email,
            cpf=cpf,
            senha=senha,
            cargo=cargo,
            matricula=matricula,
        )

        resultado = self.service.registrar_funcionario(dados)
        print("Resultado: ", resultado["message"])
        print("ID:", resultado["id"])

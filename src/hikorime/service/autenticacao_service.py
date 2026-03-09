from hikorime.models.basemodels.bm_funcionario import Funcionario
from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.models.basemodels.bm_login import LoginRequest
from hikorime.repository.repository_querys import RepositoryQuerys
from fastapi import HTTPException, status, Request


class AutenticacaoService:
    def __init__(self):
        self.repo_usuario = RepositoryQuerys("usuarios")
        self.repo_passageiro = RepositoryQuerys("passageiros")
        self.repo_funcionario = RepositoryQuerys("funcionarios")


    def get_current_user(self, request: Request) -> dict:
        """
        Retorna o usuário, se existir. Necessário para mantê-lo
        conectado no sistema.
        """
        return request.session.get("user")

    def registrar_passageiro(self, dados: Passageiro):
        # Verificar se usuário já existe
        existente = self.repo_usuario.get_by_column_name("email", dados.email)
        if existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado"
            )

        # Salvar na tabela de usuários
        id_usuario:int = self.repo_usuario.save(
            nome=dados.nome,
            email=dados.email,
            cpf=dados.cpf,
            senha=dados.senha,
            tipo_usuario=dados.tipo_usuario.value,
            data_nascimento=dados.data_nascimento,
        )

        # Salvar na tabela de passageiros
        self.repo_passageiro.save(id_usuario=id_usuario, codigo_passaporte=dados.codigo_passaporte, tipo_passaporte=dados.tipo_passaporte.value)
        
        return {
            "message": "Passageiro registrado com sucesso",
            "usuario": {
                "id_usuario": id_usuario,
                "nome": dados.nome,
                "email": dados.email,
                "tipo_usuario":dados.tipo_usuario.value,
            }
        }

    def registrar_funcionario(self, dados: Funcionario):
        # Verificar se usuário já existe
        existente = self.repo_usuario.get_by_column_name("email", dados.email)
        if existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado"
            )

        # Salvar na tabela de usuários
        id_usuario = self.repo_usuario.save(
            nome=dados.nome,
            email=dados.email,
            cpf=dados.cpf,
            senha=dados.senha,
            tipo_usuario=dados.tipo_usuario.value,
            data_nascimento=dados.data_nascimento,
        )

        # Salvar na tabela de funcionários
        self.repo_funcionario.save(
            id_usuario=id_usuario, cargo=dados.cargo, matricula=dados.matricula
        )

        return {
            "message": "Funcionário registrado com sucesso",
            "usuario": {
                "id_usuario": id_usuario,
                "nome": dados.nome,
                "email": dados.email,
                "tipo_usuario":dados.tipo_usuario.value,
            }
        }
        
    def login(self, credentials: LoginRequest):
        usuarios = self.repo_usuario.get_by_column_name("email", credentials.email)

        if not usuarios:
            #ao tentar acessar login que não existe deve ser lançada a exceção de credencias inválidas
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        user = usuarios[0]

        if user["senha"] != credentials.senha:
            raise HTTPException(status_code=401, detail="Senha Incorreta!")

        return {
            "message": "Login realizado com sucesso",
            "usuario": {
                "id_usuario": user["id_usuario"],
                "nome": user["nome"],
                "email": user["email"],
                "tipo_usuario": user["tipo_usuario"],
            },
        }

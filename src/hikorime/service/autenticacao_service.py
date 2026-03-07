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
        result = self.repo_usuario.save(
            nome=dados.nome,
            email=dados.email,
            cpf=dados.cpf,
            senha=dados.senha,
            tipo=dados.tipo.value,
        )

        usuario_id = result["id"]

        # Salvar na tabela de passageiros
        self.repo_passageiro.save(usuario_id=usuario_id, passaporte=dados.passaporte)
        
        return {
            "message": "Passageiro registrado com sucesso",
            "usuario": {
                "id": usuario_id,
                "nome": dados.nome,
                "email": dados.email,
                "tipo":dados.tipo.value,
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
        usuario_id = self.repo_usuario.save(
            nome=dados.nome,
            email=dados.email,
            cpf=dados.cpf,
            senha=dados.senha,
            tipo=dados.tipo.value,
        )

        # Salvar na tabela de funcionários
        self.repo_funcionario.save(
            usuario_id=usuario_id, cargo=dados.cargo, matricula=dados.matricula
        )

        return {
            "message": "Funcionário registrado com sucesso",
            "usuario": {
                "id": usuario_id,
                "nome": dados.nome,
                "email": dados.email,
                "tipo":dados.tipo.value,
            }
        }
        
    def login(self, credentials: LoginRequest):
        usuarios = self.repo_usuario.get_by_column_name("email", credentials.email)

        if not usuarios:
            #ao tentar acessar login que nao existe deve ser lançada a exceção de credencias inválidas
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        user = usuarios[0]

        if user["senha"] != credentials.senha:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        return {
            "message": "Login realizado com sucesso",
            "usuario": {
                "id": user["id"],
                "nome": user["nome"],
                "email": user["email"],
                "tipo": user["tipo"],
            },
        }
    
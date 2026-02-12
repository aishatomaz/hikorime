from hikorime.models.funcionario import Funcionario
from hikorime.models.passageiro import Passageiro
from hikorime.models.registro import LoginRequest
from hikorime.repository.repository_querys import RepositoryQuerys
from fastapi import HTTPException, status

class Autenticacao:
    def __init__(self):
        self.repo_usuario = RepositoryQuerys("usuarios")
        self.repo_passageiro = RepositoryQuerys("passageiros")
        self.repo_funcionario = RepositoryQuerys("funcionarios")

    def registrar_passageiro(self, dados: Passageiro):
        # Verificar se usuário já existe
        existente = self.repo_usuario.get_by_column_name("email", dados.email)
        if existente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado")
        
        # Salvar na tabela de usuários
        usuario_id = self.repo_usuario.save(
            nome=dados.nome,
            email=dados.email,
            cpf=dados.cpf,
            senha=dados.senha, # Em produção, usar hash de senha
            tipo=dados.tipo.value
        )
        
        # Salvar na tabela de passageiros
        self.repo_passageiro.save(
            usuario_id=usuario_id,
            passaporte=dados.passaporte
        )
        
        return {"message": "Passageiro registrado com sucesso", "id": usuario_id}

    def registrar_funcionario(self, dados: Funcionario):
        # Verificar se usuário já existe
        existente = self.repo_usuario.get_by_column_name("email", dados.email)
        if existente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado")
        
        # Salvar na tabela de usuários
        usuario_id = self.repo_usuario.save(
            nome=dados.nome,
            email=dados.email,
            cpf=dados.cpf,
            senha=dados.senha,
            tipo=dados.tipo.value
        )
        
        # Salvar na tabela de funcionários
        self.repo_funcionario.save(
            usuario_id=usuario_id,
            cargo=dados.cargo,
            matricula=dados.matricula
        )
        
        return {"message": "Funcionário registrado com sucesso", "id": usuario_id}

    def login(self, credentials: LoginRequest):
        usuario = self.repo_usuario.get_by_column_name("email", credentials.email)
        
        if not usuario:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
        
        # A query retorna uma lista de resultados
        user_data = usuario[0] if isinstance(usuario, list) and len(usuario) > 0 else None
        
        if not user_data or user_data.get("senha") != credentials.senha:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
            
        return {
            "message": "Login realizado com sucesso",
            "usuario": {
                "id": user_data.get("id"),
                "nome": user_data.get("nome"),
                "tipo": user_data.get("tipo")
            }
        }

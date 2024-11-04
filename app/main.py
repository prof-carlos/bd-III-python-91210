from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def listar_

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados do usuário.
    print("\nAdicionando usuário: ")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)
    service.listar_todos_usuarios()

    # Atualizando dados do usuário.
    print("\nAtualizando usuário: ")
    service.atualizar_usuario()
    service.listar_todos_usuarios()

    # Excluindo dados do usuário.
    print("\nExcluindo usuário: ")
    service.excluir_usuario()
    service.listar_todos_usuarios()

    # Pesquisar apenas um usuário no banco de dados.
    print("\nPesquisar usuário: ")  
    email_usuario = input("Informe o e-mail do usuário: ")
    service.pesquisar_usuario_por_email(email_usuario)
    

if __name__ == "__main__":
    os.system("cls || clear")
    main()

    

from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(
                email=usuario.email
            )

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        lista_usuarios =  self.repository.listar_usuarios()
        print("\nListando usuários cadastrados: ")
        for usuario in lista_usuarios:
            print(f"Nome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha}\n\n")

    def atualizar_usuario(self):
        try:
            print("\nAtualizando os dados de um usuário.")

            email_usuario = input("Informe o e-mail do usuário: ")

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email=email_usuario)

            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite seu nome: ")
                usuario_cadastrado.email = input("Digite seu e-mail: ")
                usuario_cadastrado.senha = input("Digite sua senha: ")
                self.repository.atualizar_usuario(usuario_cadastrado)
                print("Usuário atualizado com sucesso!.")
            else:
                print("Usuário não encontrado.")

        except TypeError as erro:
            print(f"Erro ao atuzalizar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


    def excluir_usuario(self):
        try:
            print("\nExcluir os dados de um usuário.")

            email_usuario = input("Informe o e-mail do usuário: ")

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email=email_usuario)

            if usuario_cadastrado:
                senha = input("Informe a senha do usuário: ")

                if senha == usuario_cadastrado.senha:
                    self.repository.excluir_usuario(usuario_cadastrado)
                    print("Usuário excluído com sucesso!.")
                else:
                    print("Senha incorreta.")
            else:
                print("Usuário não encontrado.")

        except TypeError as erro:
            print(f"Erro ao atuzalizar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

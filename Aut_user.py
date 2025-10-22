"""Mecanismo de login e logout que confirma a identidade do usuário.
Isso impede o acesso de pessoas autorizadas."""
from cadastro_users import CadastroUsuarios
class AutenticacaoUsuarios:
    def __init__(self):
        self.cadastro = CadastroUsuarios()
        self.usuario_logado = None

    def login(self, nome, senha):
        if self.cadastro.autenticar_usuario(nome, senha):
            self.usuario_logado = nome
            print(f"Usuário {nome} logado com sucesso.")
        else:
            print("Falha no login.")

    def logout(self):
        if self.usuario_logado:
            print(f"Usuário {self.usuario_logado} deslogado com sucesso.")
            self.usuario_logado = None
        else:
            print("Nenhum usuário está logado.")
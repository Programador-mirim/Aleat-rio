"""Cada usuario tera login e senha unicos.
Isso garante que cada usuario tenha acesso apenas as suas informacoes.
O cadastro tambem define o perfil de cada usuario(adiministrador, tecnico e operador), O que determina as permições de acesso."""
class CadastroUsuarios:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, nome, senha, perfil):
        if nome not in self.usuarios:
            self.usuarios[nome] = {'senha': senha, 'perfil': perfil}
            print(f"Usuário {nome} cadastrado com sucesso.")
        else:
            print(f"Usuário {nome} já está cadastrado.")

    def autenticar_usuario(self, nome, senha):
        if nome in self.usuarios and self.usuarios[nome]['senha'] == senha:
            print(f"Usuário {nome} autenticado com sucesso.")
            return True
        else:
            print("Nome de usuário ou senha incorretos.")
            return False

    def listar_usuarios(self):
        if self.usuarios:
            print("Usuários cadastrados:")
            for usuario, info in self.usuarios.items():
                print(f"{usuario} - Perfil: {info['perfil']}")
        else:
            print("Nenhum usuário cadastrado.")
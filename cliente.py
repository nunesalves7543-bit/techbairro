# CLIENTE - TechBairro Aula 21

class Cliente:

    def __init__(self, nome, telefone, email, endereco):
        self.id = None
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome} - {self.telefone} - {self.email} - {self.endereco}"
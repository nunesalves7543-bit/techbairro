import sqlite3
from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente

class ValidadorCliente:

    def validar(self, cliente):
        vazios = []

        if cliente.nome == "":
            vazios.append("Nome")

        if cliente.telefone == "":
            vazios.append("Telefone")

        if cliente.email == "":
            vazios.append("E-mail")

        if cliente.endereco == "":
            vazios.append("Endereço")

        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido."

        return None

    def email_parece_valido(self, email):
        if "@" not in email:
            return False

        partes = email.split("@")

        if len(partes) != 2:
            return False

        if partes[0] == "" or "." not in partes[1]:
            return False

        if partes[1].startswith(".") or partes[1].endswith("."):
            return False

        return True
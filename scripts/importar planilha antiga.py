
import sys
import os
import csv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cliente import Cliente
from validacao import ValidadorCliente
from banco import GerenciadorClientes

CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "techbairro.db"
)

CAMINHO_PLANILHA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "clientes.csv"
)

gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()

importados = 0
recusados = 0

with open(CAMINHO_PLANILHA, "r", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for linha in leitor:
        cliente = Cliente(
            linha["nome"],
            linha["telefone"],
            linha["email"],
            linha["endereco"]
        )

        erro = validador.validar(cliente)

        if erro:
            print(f"Recusado: {cliente.nome} - {erro}")
            recusados += 1
        else:
            gerenciador.cadastrar(cliente)
            print(f"Importado: {cliente.nome}")
            importados += 1

print("\nResumo da importação")
print("Importados:", importados)
print("Recusados:", recusados)

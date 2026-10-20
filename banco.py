# BANCO - TechBairro Aula 21

import sqlite3
from cliente import Cliente


class GerenciadorClientes:

    def __init__(self, caminho_banco):
        self.conexao = sqlite3.connect(caminho_banco)
        self.criar_tabela()

    def criar_tabela(self):
        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                endereco TEXT
            )
        """)
        self.conexao.commit()

    def cadastrar(self, cliente):
        self.conexao.execute("""
            INSERT INTO clientes (nome, telefone, email, endereco)
            VALUES (?, ?, ?, ?)
        """, (
            cliente.nome,
            cliente.telefone,
            cliente.email,
            cliente.endereco
        ))
        self.conexao.commit()

    def listar(self):
        cursor = self.conexao.execute("""
            SELECT id, nome, telefone, email, endereco
            FROM clientes
            ORDER BY nome
        """)

        clientes = []

        for linha in cursor.fetchall():
            cliente = Cliente(
                linha[1],
                linha[2],
                linha[3],
                linha[4]
            )
            cliente.id = linha[0]
            clientes.append(cliente)

        return clientes

    def editar(self, id, cliente):
        self.conexao.execute("""
            UPDATE clientes
            SET nome=?, telefone=?, email=?, endereco=?
            WHERE id=?
        """, (
            cliente.nome,
            cliente.telefone,
            cliente.email,
            cliente.endereco,
            id
        ))
        self.conexao.commit()

    def excluir(self, id):
        self.conexao.execute(
            "DELETE FROM clientes WHERE id=?",
            (id,)
        )
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()
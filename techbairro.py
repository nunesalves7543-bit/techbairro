import tkinter as tk
from tkinter import messagebox
import sqlite3
from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente

VERSAO = "3.3.1"
BANCO = "techbairro.db"


class Cliente:
    def __init__(self, id, nome, telefone, email, endereco):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class GerenciadorClientes:
    def __init__(self):
        with sqlite3.connect(BANCO) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    endereco TEXT NOT NULL
                )
            """)

    def listar(self):
        with sqlite3.connect(BANCO) as conexao:
            linhas = conexao.execute(
                "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY id"
            ).fetchall()
        return [Cliente(*linha) for linha in linhas]

    def cadastrar(self, cliente):
        with sqlite3.connect(BANCO) as conexao:
            conexao.execute(
                "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
                (cliente.nome, cliente.telefone, cliente.email, cliente.endereco)
            )

    def atualizar(self, id_cliente, cliente):
        with sqlite3.connect(BANCO) as conexao:
            cursor = conexao.execute(
                """UPDATE clientes SET nome=?, telefone=?, email=?, endereco=?
                   WHERE id=?""",
                (cliente.nome, cliente.telefone, cliente.email, cliente.endereco, id_cliente)
            )
            return cursor.rowcount > 0

    def remover(self, id_cliente):
        with sqlite3.connect(BANCO) as conexao:
            cursor = conexao.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
            return cursor.rowcount > 0


gerenciador = GerenciadorClientes()
id_em_edicao = None
campos = {}
consultas = []


def criar_cliente_dos_campos():
    return Cliente(None, campos["Nome"].get().strip(),
                   campos["Telefone"].get().strip(),
                   campos["E-mail"].get().strip(),
                   campos["Endereço"].get().strip())


def limpar_campos():
    global id_em_edicao
    for campo in campos.values():
        campo.delete(0, tk.END)
    id_em_edicao = None
    botao_salvar.config(text="Salvar")
    entrada_nome.focus()


def cancelar():
    estava_editando = id_em_edicao is not None
    limpar_campos()
    if estava_editando:
        status.config(text="Edição cancelada. Nada foi alterado.", fg="gray")
    else:
        status.config(text="Formulário limpo", fg="gray")


def salvar():
    global id_em_edicao
    cliente = criar_cliente_dos_campos()
    if not all([cliente.nome, cliente.telefone, cliente.email, cliente.endereco]):
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return
    if not cliente.telefone.isdigit():
        messagebox.showwarning("Atenção", "O telefone deve conter apenas números.")
        return
    if "@" not in cliente.email or "." not in cliente.email.split("@")[-1]:
        messagebox.showwarning("Atenção", "Digite um e-mail válido.")
        return

    try:
        if id_em_edicao is None:
            gerenciador.cadastrar(cliente)
            status.config(text=f"Cliente '{cliente.nome}' cadastrado com sucesso!", fg="green")
        else:
            alterou = gerenciador.atualizar(id_em_edicao, cliente)
            if not alterou:
                status.config(text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.", fg="red")
                limpar_campos()
                atualizar_todas_consultas()
                return
            status.config(text=f"Cliente '{cliente.nome}' atualizado com sucesso!", fg="green")
        limpar_campos()
        atualizar_todas_consultas()
    except sqlite3.Error as erro:
        messagebox.showerror("Erro no banco", f"Não foi possível salvar o cliente.\n{erro}")


def atualizar_todas_consultas():
    for janela, lista, clientes_na_tela in consultas[:]:
        if janela.winfo_exists():
            atualizar_lista(lista, clientes_na_tela)
        else:
            consultas.remove((janela, lista, clientes_na_tela))


def atualizar_lista(lista, clientes_na_tela):
    lista.delete(0, tk.END)
    clientes_na_tela.clear()
    clientes = gerenciador.listar()
    if not clientes:
        lista.insert(tk.END, "Nenhum cliente cadastrado")
        return
    for cliente in clientes:
        lista.insert(tk.END, f"{cliente.nome} | {cliente.telefone} | {cliente.email}")
        clientes_na_tela.append(cliente)


def abrir_consulta():
    janela = tk.Toplevel(root)
    janela.title("Consulta de clientes")
    janela.geometry("600x350")
    lista = tk.Listbox(janela, width=85, height=13)
    lista.pack(padx=10, pady=10, fill="both", expand=True)
    botoes = tk.Frame(janela)
    botoes.pack(pady=5)
    clientes_na_tela = []
    consultas.append((janela, lista, clientes_na_tela))

    def cliente_selecionado(acao):
        selecionado = lista.curselection()
        if not selecionado or selecionado[0] >= len(clientes_na_tela):
            messagebox.showwarning("Atenção", f"Selecione um cliente antes de {acao}.")
            return None
        return clientes_na_tela[selecionado[0]]

    def editar_cliente(evento=None):
        cliente = cliente_selecionado("editar")
        if cliente is None:
            return
        preencher_formulario(cliente)

    def excluir_cliente(evento=None):
        cliente = cliente_selecionado("excluir")
        if cliente is None:
            return
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Excluir este cliente?\n\nNome: {cliente.nome}\nTelefone: {cliente.telefone}\nE-mail: {cliente.email}"
        )
        if confirmar:
            try:
                removeu = gerenciador.remover(cliente.id)
            except sqlite3.Error as erro:
                messagebox.showerror("Erro no banco", f"Não foi possível excluir o cliente.\n{erro}")
                return
            if not removeu:
                messagebox.showwarning(
                    "Cliente não encontrado",
                    f"{cliente.nome} já não está mais no banco.\nA lista será atualizada."
                )
            atualizar_todas_consultas()

    tk.Button(botoes, text="Editar selecionado", command=editar_cliente).pack(side="left", padx=5)
    tk.Button(botoes, text="Excluir selecionado", command=excluir_cliente).pack(side="left", padx=5)
    lista.bind("<Double-Button-1>", lambda evento: editar_cliente())
    lista.bind("<Delete>", lambda evento: excluir_cliente())
    atualizar_lista(lista, clientes_na_tela)


def preencher_formulario(cliente):
    global id_em_edicao
    id_em_edicao = cliente.id
    for nome, valor in [
        ("Nome", cliente.nome), ("Telefone", cliente.telefone),
        ("E-mail", cliente.email), ("Endereço", cliente.endereco)
    ]:
        campos[nome].delete(0, tk.END)
        campos[nome].insert(0, valor)
    status.config(text=f"Editando cliente: {cliente.nome}", fg="blue")
    botao_salvar.config(text="Salvar edição")


root = tk.Tk()
root.title(f"TechBairro — Cadastro de Cliente | v{VERSAO}")
root.geometry("480x370")
tk.Label(root, text="TechBairro — Cadastro de Cliente", font=("Arial", 14, "bold")).pack(pady=10)

formulario = tk.Frame(root)
formulario.pack(padx=15, pady=5)
for linha, nome in enumerate(["Nome", "Telefone", "E-mail", "Endereço"]):
    tk.Label(formulario, text=nome).grid(row=linha, column=0, sticky="w", padx=5, pady=5)
    entrada = tk.Entry(formulario, width=35)
    entrada.grid(row=linha, column=1, padx=5, pady=5)
    campos[nome] = entrada
entrada_nome = campos["Nome"]

botoes = tk.Frame(root)
botoes.pack(pady=8)
botao_salvar = tk.Button(botoes, text="Salvar", width=13, command=salvar)
botao_salvar.grid(row=0, column=0, padx=5)
tk.Button(botoes, text="Cancelar", width=13, command=cancelar).grid(row=0, column=1, padx=5)
tk.Button(botoes, text="Consultar clientes", command=abrir_consulta).grid(row=0, column=2, padx=5)

status = tk.Label(root, text="Pronto", fg="gray")
status.pack(pady=8)
tk.Label(root, text=f"Versão {VERSAO}").pack(side="bottom", pady=5)

root.mainloop()


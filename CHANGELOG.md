# Changelog da TechBairro

## v3.3.2 (Aula 27)
### Adicionado
- README com requisitos, instalação e configuração do banco.
- Arquivo requirements.txt.
- Manual de uso em docs/manual_de_uso.md.
- Registro de testes em docs/registro_de_testes.md.

## v3.3.1 (Aula 24)

### Alterado
- Atualizadas as instruções de execução para corresponder à versão 3.3.1.
- Adicionada a seção sobre como consultar o histórico do Git.
- Configurado o `.gitignore` para manter bancos de dados, caches, arquivos compilados e pacotes fora do repositório.
- Organizados os arquivos de documentação e o script auxiliar de empacotamento.


## v3.3.0 (Aula 18)

### Alterado
- O número da versão passou a ficar em um único lugar no arquivo techbairro.py.

### Adicionado
- Script scripts/gerar_pacote.py, que cria o pacote ZIP da versão para publicação.
- Arquivo COMO_EXECUTAR.txt, com as instruções para executar o sistema.

## v3.2 (Aula 16)

### Alterado

* O banco agora é aberto pelo caminho completo usando `os.path` e `__file__`, sempre na pasta do projeto, não importa de onde o programa seja executado.

### Adicionado

* Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

## v3.1 (Aula 15)

### Corrigido

* Corrigido o cadastro de clientes.
* Corrigida a atualização dos dados dos clientes.
* Corrigida a exclusão de clientes.
* Corrigido o problema de atualização que não estava fazendo o commit no banco.
* Corrigida a validação de e-mail para aceitar somente formatos válidos.

## v3.0 (Aula 14)

### Alterado

* O GerenciadorClientes deixou de guardar os clientes em uma lista em memória e passou a gravar os dados no banco SQLite `techbairro.db`.
* Os métodos de cadastro, listagem, atualização e exclusão passaram a utilizar comandos SQL.
* Os clientes passaram a continuar salvos mesmo depois de fechar o programa.

### Adicionado

* Banco de dados SQLite `techbairro.db`.
* Persistência dos clientes no banco de dados.

## v2.0 (Aulas 11 e 12)

### Adicionado

* Foram criadas as classes `Cliente` e `GerenciadorClientes`.
* Foi adicionada a tela de Consulta com Listbox e Scrollbar.
* Foram adicionadas as funções de edição e exclusão de clientes.

## Antes da v2.0 (Aulas 5 a 10)

* Foram criadas as telas de cadastro e consulta, os eventos dos botões e o armazenamento dos clientes.
* Foram adicionadas as validações dos campos de nome, telefone, e-mail e endereço.
+
=======
## v3.3.2 (Aula 21)

- Separada a classe Cliente no arquivo cliente.py.
- Separada a classe GerenciadorClientes no arquivo banco.py.
- Criada a classe ValidadorCliente no arquivo validacao.py.
- Criados testes automáticos das regras de validação.
- Mantido o comportamento esperado para o usuário.

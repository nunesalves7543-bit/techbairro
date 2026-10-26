# TechBairro

Sistema de cadastro de clientes desenvolvido em Python para uma associação de moradores, como projeto do curso Técnico em Desenvolvimento de Sistemas do Senac DF.

## Sobre o projeto

A TechBairro foi criada para facilitar a organização das informações dos clientes da associação de moradores. O sistema permite armazenar e consultar os dados de maneira organizada, utilizando um banco de dados SQLite.

## Funcionalidades

- Cadastrar clientes.
- Consultar clientes cadastrados.
- Editar informações dos clientes.
- Excluir clientes.
- Armazenar os dados em um banco de dados SQLite.
- Validar informações preenchidas nos campos, conforme as regras implementadas no sistema.

## Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Tkinter:** biblioteca utilizada para criar as telas do sistema.
- **SQLite:** banco de dados utilizado para armazenar as informações.
- **Git e GitHub:** ferramentas utilizadas para versionar e compartilhar o código-fonte.

## Requisitos

Para executar o projeto, é necessário ter:

- Python instalado no computador.
- Os arquivos do projeto TechBairro.
- Um terminal ou o Visual Studio Code.

O Tkinter geralmente acompanha as instalações padrão do Python para Windows. Caso não esteja disponível, será necessário verificar a instalação da biblioteca.

## Como executar

1. Baixe ou clone o repositório do projeto.
2. Abra a pasta `TechBairro` no Visual Studio Code.
3. Abra o terminal.
4. Execute o comando:

bash
python techbairro.py


No Windows, se o comando anterior não funcionar, tente:

bash
py techbairro.py


5. Aguarde a abertura da janela do sistema.

## Estrutura do projeto

A estrutura pode conter os seguintes arquivos e pastas:

text 
TechBairro/
├── techbairro.py
├── banco.py
├── cliente.py
├── CHANGELOG.md
├── COMO_EXECUTAR.txt
├── requirements.txt
├── .gitignore
└── docs/
    └── manual_de_uso.md


**Observação:** a estrutura acima é um exemplo. Ajuste os nomes conforme os arquivos que realmente existem na sua pasta.

## Banco de dados

O projeto utiliza SQLite para armazenar os dados dos clientes. O arquivo do banco de dados pode ser criado automaticamente quando o programa é executado.

Não publique bancos de dados que contenham informações pessoais reais no GitHub.

## Documentação

O manual de uso está disponível no arquivo `docs/manual_de_uso.md`. Ele explica como utilizar as principais funções do sistema.

O histórico das alterações do projeto pode ser consultado no arquivo `CHANGELOG.md`.

## Segurança

As informações dos clientes devem ser utilizadas somente para a finalidade autorizada. O banco de dados deve ser protegido, e cópias de segurança devem ser armazenadas em local seguro.

## Autor

Projeto acadêmico desenvolvido para o curso Técnico em Desenvolvimento de Sistemas – Senac DF.

# Manual de Uso – TechBairro

## 1. Sobre o sistema

A TechBairro é um sistema desenvolvido em Python para ajudar a associação de moradores a organizar o cadastro de seus clientes. O sistema permite cadastrar, consultar, editar e excluir informações dos clientes.

## 2. Como iniciar o sistema

1. Abra a pasta do projeto TechBairro no computador.
2. Abra o Visual Studio Code.
3. Abra o terminal do VS Code.
4. Execute o programa com o comando:

bash
python techbairro.py


5. Aguarde a abertura da janela do sistema.

**Observação:** o Python deve estar instalado no computador. Caso o comando acima não funcione, tente `py techbairro.py`, se estiver usando Windows.

## 3. Como cadastrar um cliente

1. Abra a tela de cadastro de clientes.
2. Preencha o campo Nome.
3. Informe o Telefone.
4. Digite o E-mail.
5. Preencha o Endereço.
6. Clique no botão **Salvar**.
7. Confira se o cadastro foi realizado corretamente.

Todos os campos devem ser preenchidos. O telefone deve conter números e o e-mail deve ter um formato válido.

## 4. Como consultar clientes

1. Abra a opção de consulta de clientes.
2. Visualize a lista de clientes cadastrados.
3. Se o sistema possuir pesquisa por nome, digite o nome desejado no campo de busca.
4. Confira as informações apresentadas na tela.

## 5. Como editar um cliente

1. Abra a tela de consulta.
2. Selecione o cliente que deseja alterar.
3. Clique na opção de edição, caso esteja disponível.
4. Modifique as informações necessárias.
5. Salve as alterações.

## 6. Como excluir um cliente

1. Abra a tela de consulta.
2. Selecione o cliente que deseja excluir.
3. Clique na opção **Excluir**.
4. Confirme a exclusão, se o sistema solicitar.
5. Confira se o cliente deixou de aparecer na lista.

**Atenção:** confira os dados antes de excluir um cadastro.

## 7. Armazenamento dos dados

A TechBairro utiliza um banco de dados SQLite para armazenar as informações dos clientes. O arquivo do banco pode ser criado automaticamente pelo sistema.

Não exclua nem altere o banco de dados manualmente, pois isso pode causar perda de informações.

## 8. Cuidados com as informações

- Utilize os dados dos clientes somente para a finalidade autorizada.
- Não compartilhe informações pessoais sem autorização.
- Faça cópias de segurança do banco de dados em um local protegido.
- Não publique o arquivo `techbairro.db` no GitHub se ele contiver dados reais de clientes.

## 9. Solução de problemas

**O programa não abre:** confira se o Python está instalado e se o terminal está na pasta correta do projeto.

**O cadastro não é salvo:** verifique se todos os campos foram preenchidos corretamente e se o banco de dados está funcionando.

**O sistema apresenta um erro:** leia a mensagem exibida no terminal e procure ajuda para identificar o problema.

## 10. Conclusão

A TechBairro facilita a organização dos cadastros de clientes da associação de moradores. Seguindo as orientações deste manual, o usuário poderá utilizar as funções disponíveis de maneira mais organizada e segura.

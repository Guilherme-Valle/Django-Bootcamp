# Bootcamp para criação de projeto web com Django #

Passos efetuados no bootcamp:

1) Criação de virtual env, instalação do django e da biblioteca 
psycopg2, para conexão do banco de dados postgresql com o Python.

2) Criação do projeto com o comando django-admin startproject sistema_bootcamp

3) Testar colocar o projeto para rodar: python manage.py runserver

4) Criar app: python manage.py startapp appEstoque

5) Adicionar app na lista INSTALED_APPS de settings.py

5) Configurar banco de dados na pasta settings.py, variável DATABASES.

6) Configurar rotas do sistemas:
   a) Criar a rota raiz para o app, dentro da pasta urls.py de sistema_bootcamp 
      "apontar" para o appEstoque.
   b) Criar o arquivo urls.py em appEstoque e definir rotas
   c) Dentro do arquivo views (que é o controller do Django) definir as funções 
      correspondentes às views a serem renderizadas nas urls.

7) Criar banco de dados no Postgresql e rodar o runserver. Basta checar os paths
   configurados no urls.py do AppEstoque para testar as páginas rodando.


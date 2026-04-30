Sistema de Gestão de Usuários
Desenvolvido por Henrique de O. Molinari · RA: 25001176

Sobre
Sistema de cadastro de usuários com arquitetura MVC + Service + Repository, persistência em SQLite e interface web com Flask.

Estrutura
project/
 ├── controller/
 ├── service/
 ├── repository/
 ├── model/
 ├── view/
 ├── db/
 ├── templates/
 ├── app.py       # Web
 └── main.py      # CLI

Como rodar
Instalar dependência:
bashpip install flask
Interface web:
bashpython app.py
Acesse: http://localhost:5000
Interface CLI:
bashpython main.py

Tecnologias

Python 3
SQLite
Flask

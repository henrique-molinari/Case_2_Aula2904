```markdown
# 🚀 Sistema de Gestão de Usuários

Este é um sistema robusto de cadastro de usuários, focado em boas práticas de desenvolvimento e organização de código. O projeto utiliza uma arquitetura multicamadas para garantir a separação de responsabilidades e facilitar a manutenção.

## 👤 Autor
* **Henrique de O. Molinari**
* **RA:** 25001176

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Framework Web:** Flask
* **Banco de Dados:** SQLite
* **Arquitetura:** MVC + Service + Repository (POO)

---

## 🏗️ Estrutura do Projeto
A organização segue os princípios de **Orientação a Objetos**, onde cada classe reside em seu próprio arquivo dentro de pastas específicas:

```text
project/
 ├── controller/  # Lógica de controle e rotas
 ├── service/     # Regras de negócio
 ├── repository/  # Comunicação com o banco de dados
 ├── model/       # Definição das classes de entidade
 ├── view/        # Componentes de visualização (CLI)
 ├── db/          # Scripts e arquivos do banco SQLite
 ├── templates/   # Arquivos HTML (Flask)
 ├── app.py       # Ponto de entrada da interface Web
 └── main.py      # Ponto de entrada da interface CLI
```

---

## 🚀 Como Executar

### 1. Instalação de Dependências
Certifique-se de ter o Python instalado e execute o comando abaixo para instalar o Flask:
```bash
pip install flask
```

### 2. Interface Web
Para iniciar o servidor web e acessar a interface via navegador:
```bash
python app.py
```
Acesse em: [http://localhost:5000](http://localhost:5000)

### 3. Interface de Linha de Comando (CLI)
Para interagir com o sistema diretamente pelo terminal:
```bash
python main.py
```

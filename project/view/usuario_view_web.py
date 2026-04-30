from flask import Flask, request, render_template

class UsuarioViewWeb:

    def __init__(self, controller):
        self.controller = controller
        self.app = Flask(__name__, template_folder="../templates")
        self._registrar_rotas()

    def _registrar_rotas(self):

        @self.app.route("/")
        def index():
            usuarios = self.controller.service.listar_usuarios()
            return render_template("usuarios.html", usuarios=usuarios)

        @self.app.route("/criar", methods=["POST"])
        def criar():
            nome = request.form["nome"]
            email = request.form["email"]
            mensagem, erro = None, None
            try:
                self.controller.service.criar_usuario(nome, email)
                mensagem = "Usuário criado com sucesso!"
            except ValueError as e:
                erro = str(e)
            usuarios = self.controller.service.listar_usuarios()
            return render_template("usuarios.html", usuarios=usuarios, mensagem=mensagem, erro=erro)

    def run(self):
        self.app.run(debug=True)
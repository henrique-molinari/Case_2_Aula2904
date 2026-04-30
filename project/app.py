from service.usuario_service import UsuarioService
from controller.usuario_controller import UsuarioController
from view.usuario_view_web import UsuarioViewWeb

def main():
    service = UsuarioService()
    controller = UsuarioController(view=None)
    view_web = UsuarioViewWeb(controller)
    view_web.run()

if __name__ == "__main__":
    main()
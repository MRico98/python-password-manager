from src.ui.main_window import MainWindow

class MainController:
    def __init__(self):
        self.app = MainWindow()
        self._setup_handlers()

    def _setup_handlers(self):
        self.app.set_add_password_handler(self._add_password)
        self.app.set_view_passwords_handler(self._view_passwords)

    def _add_password(self):
        print("Abriendo ventana para agregar contraseña...")

    def _view_passwords(self):
        print("Abriendo lista de contraseñas...")

    def run(self):
        self.app.run()
from src.ui.main_window import MainWindow
from src.ui.add_password_window import AddPasswordWindow

class MainController:
    def __init__(self):
        self.app = MainWindow()
        self._setup_handlers()

    def _setup_handlers(self):
        self.app.set_add_password_handler(self._add_password)
        self.app.set_view_passwords_handler(self._view_passwords)

    def _add_password(self):
        self.add_password_window = AddPasswordWindow(self.app)

    def _view_passwords(self):
        print("Abriendo lista de contraseñas...")

    def run(self):
        self.app.run()
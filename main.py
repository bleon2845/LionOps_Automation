import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow

from modules.save_pdf import SavePDFController
from modules.create_orders import CreateOrdersController

from integrations.sap.sap_gui import SapGUI
from integrations.sap.facade import SapFacade 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SAP instance
        self.sap_gui = SapGUI()
        self.sap = SapFacade(self.sap_gui)

        # Modules
        self.save_pdf = SavePDFController(self)
        self.create_orders = CreateOrdersController(self)

        # Connections
        self._connect_navigation()

    #-------------- Navigation between pages --------------
    def _connect_navigation(self):
        self.ui.actionPrint_PDF.triggered.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_savepdf))
        self.ui.actionCreate_Orders.triggered.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_createorders))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

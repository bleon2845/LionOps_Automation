from PySide6.QtWidgets import QMessageBox, QLineEdit, QFileDialog, QTableWidgetItem
from PySide6.QtCore import QObject
import pandas as pd
import os


class CreateOrdersControllerMB21(QObject):
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui
        self.sap = main_window.sap

        self.connect_signals()

    #--------------- Button Page ------------------#
    def connect_signals(self):
        self.ui.btn_openMB21.clicked.connect(self.open_filecreation) # button to open file dialog
        self.ui.btn_creationMB21.clicked.connect(self.creation_clicked) # button for creation of documents

    #------------------- Get Line Edit Text ------------------#
    def _get_line_text(self, name: str) -> str: #Obtener nombres de lineEdit en gui
        edit = self.main_window.findChild(QLineEdit, name)
        return edit.text().strip() if edit else ""

    #------------------- SAP Login ------------------#
    #def login_sap(self, user_field: str, pass_field: str, btn):
    #    username = self._get_line_text(user_field) # Get user with def
    #    password = self._get_line_text(pass_field) # Get user with def
#
    #    if not username or not password:# Check if user or password are empty
    #        QMessageBox.warning(
    #            self.main_window,
    #            "Missing Data",
    #            "Please enter both USER and PASSWORD before logging in."
    #        )
    #        return
#
    #    btn.setEnabled(False)
#
    #    try:
    #        ok = self.sap.login(username, password,system_name="EPA [ANDINA_COPA]")
    #        if ok:
    #            QMessageBox.information(self.main_window, "SAP Login", "Login successfully.")
    #    except Exception as e:
    #        QMessageBox.critical(self.main_window, "SAP Login", f"Session unsuccessfull:\n{e}")
    #    finally:
    #        btn.setEnabled(True)
#
    #    edit_user = self.main_window.findChild(QLineEdit, user_field)
    #    edit_pass = self.main_window.findChild(QLineEdit, pass_field)
#
    #    if edit_user:
    #        edit_user.clear()
    #    if edit_pass:
    #        edit_pass.clear()

    #--------------- CREATION ORDERS -----------------#

    def open_filecreationMB21(self):
        file_path_creation, _ = QFileDialog.getOpenFileName(self.main_window, "Select File","","Excel Files (*.xlsx *.xls)")

        if not file_path_creation:
            return

        self.file_path_creation = file_path_creation
        self.ui.txt_filecreationMB21.setText(file_path_creation)
        self.load_excel_creationMB21(file_path_creation, sheet_name='Creation')

    def load_excel_creationMB21(self, file_path_creation: str, sheet_name: str='Creation'):
        try:
            df = pd.read_excel(file_path_creation, sheet_name=sheet_name, dtype=str)
        except FileNotFoundError:
            QMessageBox.warning(self.main_window, "File not Found", f"Not Found:\n{self.file_path_creation}")
            return
        except ValueError as e:
            QMessageBox.warning(self.main_window, "Invalid Sheet", f"Sheet not Read '{sheet_name}':\n{e}")
            return
        except Exception as e:
            QMessageBox.critical(self.main_window, "Wrong Excel Reading", str(e))
            return

        df = df.fillna("") #Clean NaN values

        tbl = self.ui.tb_creationMB21 # o self.ui.tableWidget
        tbl.setSortingEnabled(False)
        tbl.clearContents()
        tbl.setRowCount(len(df))
        tbl.setColumnCount(len(df.columns))
        tbl.setHorizontalHeaderLabels([str(c) for c in df.columns])

        for r in range(len(df)):# Change dataframe to table
            for c, col in enumerate(df.columns):
                tbl.setItem(r, c, QTableWidgetItem(str(df.iat[r, c])))

        tbl.resizeColumnsToContents()

        self._df_creation = df #Save DataFrame as attribute for later use

    def creation_clickedMB21(self):
        if not getattr(self, 'file_path_creation', None): # Read file path from txt_filecreation
            QMessageBox.information(self.main_window, "No file selected", "Please select a file to create documents from.")
            return

        user = os.getlogin() # Get current user
        file_folder = rf"C:\Users\{user}\Downloads"

        msgBox = QMessageBox(self.main_window)
        msgBox.setWindowTitle("Creation Documents")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Creation documents")
        msgBox.setInformativeText("Are you sure you want to create the documents?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setModal(True)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:

            try:
                self.main_window.showMinimized()
                self.sap.create_ordersMB21(self.ui.txt_filecreationMB21.text(), file_folder)# Send file path and pdf folder to create_documents
                msg = QMessageBox(self.main_window)
                msg.setWindowTitle("Creation")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Documents created successfully.")
                msg.exec()
            except Exception as e:
                QMessageBox.critical(self.main_window, "Creation Error", f"Error creating documents:\n{e}")
                return


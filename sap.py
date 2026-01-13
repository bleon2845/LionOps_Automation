import win32com.client
import sys
import subprocess
import time
import pandas as pd
from tkinter import*
from tkinter import messagebox
import pyautogui
import os
import win32gui
import win32con
import threading
from datetime import datetime
import shutil

class SapGui():
    def __init__(self):
        self.application = None
        self.connection  = None
        self.session     = None

    def open_sap(self):

        try:
        # Try connecting to an existing SAP session
            sapgui = win32com.client.GetObject("SAPGUI")
            self.application = sapgui.GetScriptingEngine
            return  # SAP is already open

        except Exception:

            paths = [
                r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe",
                r"C:\Program Files\SAP\FrontEnd\SAPGUI\saplogon.exe"
            ]

            for path in paths:

                if os.path.exists(path):
                    self.path = path
                    subprocess.Popen(path)
                    time.sleep(3)
                    break
            else:
                raise FileNotFoundError("Path SAP logon not found")
        
            sapgui = win32com.client.GetObject("SAPGUI")
            self.application = sapgui.GetScriptingEngine

    def connect_sap(self, system_name=None, index=None):

        try:
            sapgui = win32com.client.GetObject("SAPGUI")

        except Exception:
                raise RuntimeError("SAP GUI Scripting not available.")
        
        if sapgui is None:
            raise RuntimeError("SAP GUI Scripting not available.")

        app = sapgui.GetScriptingEngine
        self.application = app

        if index is not None:

            if app.Children.Count <= index:
                raise RuntimeError(f"Not existing SAP connection with index {index}")
            self.connection = app.Children(index)

        else:
        # Si ya existe al menos una conexión abierta, usarla
            if app.Children.Count > 0:
                self.connection = app.Children(0)
            else:
                # Si no hay conexiones, abrir una nueva
                if not system_name:
                    raise RuntimeError("system_name is required when no connections are available.")
                self.connection = app.OpenConnection(system_name, True)

        time.sleep(2)

        if self.connection.Children.Count == 0:
            raise RuntimeError("Not session available in the selected connection.")

        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").maximize()

    def login_sap(self, username, password, system_name=None, index=None):
        self.open_sap()
        time.sleep(2)
        self.connect_sap(system_name = system_name, index = index)

        try:
            self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "300" #"100" #Claro # "500" #Telefonica
            self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username #Add username when the code is ready
            time.sleep(2)
            self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password #Add password when the code is ready
            self.session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "ES" #Idioma
                
            self.session.findById("wnd[0]").sendVKey(0) # Send enter

            # 2) Fallback press button logon
            try:
                self.session.findById("wnd[0]/usr/btnLOGON", False) and \
                    self.session.findById("wnd[0]/usr/btnLOGON").press()
            except Exception:
                pass

            # 3) Fallback press button logon
            try:
                self.session.findById("wnd[0]/tbar[0]/btn[0]", False) and \
                    self.session.findById("wnd[0]/tbar[0]/btn[0]").press()   # "Enter" (✔)
            except Exception:
                pass

        except Exception as e:
            raise RuntimeError(f"Error durante el login: {e}") from e
        
        return True

    #----------- Create documents from excel file -----------
    def element_exists(self, element_id):
        try:
            self.session.findById(element_id)
            return True
        except:
            return False

    def ensure_header(self):
        header_tabs = ("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL")

        if not self.element_exists(header_tabs):
            try:
                self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB1:SAPLMEVIEWS:1100/subSUB1:SAPLMEVIEWS:4000/btnDYN_4000-BUTTON").press()
            except:
                pass
        self.session.findById(header_tabs + "/tabpTABHDT3").select()

    def create_documents(self, file_path, file_folder): # Use folder to save temporary files if needed
        datacreation = pd.read_excel(file_path, sheet_name='Creation').astype(str)# File must have a sheet named 'Creation'
        datacreation.columns = (datacreation.columns.str.strip().str.upper().str.replace(r"\s+", "_", regex=True))# Check columns format

        self.connect_sap() # Connect to SAP if not connected

        # Register general data
        self.session.findById("wnd[0]/tbar[0]/okcd").Text = "/NME21N"
        self.session.findById("wnd[0]").sendVKey(0)

        self.ensure_header() # Ensure header is visible

        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/cmbMEPO_TOPLINE-BSART").setFocus()
        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/cmbMEPO_TOPLINE-BSART").key = "AUB"
        time.sleep(1)

        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").text = "C906"

        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKORG").text = "CO02"
        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKGRP").text = "T34"
        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").text = "CO15"
        self.session.findById("wnd[0]").sendVKey(0)

        # Register header text NA
        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT3").select()
        # Change the text "NA" according to file
        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT3/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1230/subTEXTS:SAPLMMTE:0100/subEDITOR:SAPLMMTE:0101/cntlTEXT_EDITOR_0101/shellcont/shell").text = "NA"
        
        # Click to zoom in items
        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB1:SAPLMEVIEWS:4000/btnDYN_4000-BUTTON").press()
        
        procesando = False  #Control variable to avoid multiple processing

        row_number = 0 #Row counter for items in SAP
        scroll_number = 0 #Scroll counter to manage scrolling in SAP table

        for i, row in datacreation.iterrows():

            if row["INDICE"] == "X":
                procesando = True

            #Execute only when the row is marked to be processed
            if procesando:

                # Register Item Data
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/txtMEPO1211-AFNAM[2,{row_number}]").text = row["PROYECTO"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-EMATN[3,{row_number}]").text = row["MATERIAL"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/txtMEPO1211-MENGE[4,{row_number}]").text = row["CANTIDAD"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-EEIND[5,{row_number}]").text = row["FECHA"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[6,{row_number}]").text = row["CENTRO"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-LGOBE[7,{row_number}]").text = row["ALM.DEST"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-CHARG[8,{row_number}]").text = row["LOTE"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/txtMEPO1211-BEDNR[9,{row_number}]").text = row["OT"]
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-RESLO_BEZ[10,{row_number}]").text = row["BODEGA"]
                # Focus in each row to avoid errors
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-LGOBE[7,{row_number}]").setFocus()
                self.session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-LGOBE[7,{row_number}]").caretPosition = 4

                # Confirm destination warehouse this action open a popup
                self.session.findById("wnd[0]").sendVKey(0)

                # Try to find popup window
                try:
                    popup = self.session.findById("wnd[1]")
                    # If found, press OK button
                    popup.findById("tbar[0]/btn[0]").press()
                except:
                    # If not found, continue without failing
                    pass
                
                #time.sleep(5)

                try:
                    self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB1:SAPLMEVIEWS:4002/btnDYN_4000-BUTTON").press()
                except:
                    try:
                        self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB3:SAPLMEVIEWS:1100/subSUB1:SAPLMEVIEWS:4002/btnDYN_4000-BUTTON").press()
                    except:
                        pass

                row_number += 1
                scroll_number += 1

                if scroll_number == 14:
                    for pos in range(1, 14):
                        self.session.findById(
                            "wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211"
                        ).verticalScrollbar.position = pos
                        row_number = 1  # Reset row number after scrolling

                
            if row["GUARDAR"] == "X":
                break

            

            

            #self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/txtMEPO1211-AFNAM[2,0]").setFocus()
            #self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/txtMEPO1211-AFNAM[2,0]").caretPosition = 0

    #----------- Print documents from excel file ----------- 
    def save_pdf(self, full_path: str, timeout: float = 40.0):
        

        TARGET_CLASSES = {"#32770", "Xaml_WindowedPopupClass"}# Class names to look for

        def _find_file_dialog():
            found = None

            def cb(hwnd, _):
                nonlocal found
                if found is not None:
                    return

                if not win32gui.IsWindowVisible(hwnd):
                    return

                cls = win32gui.GetClassName(hwnd)
                if cls not in TARGET_CLASSES:
                    return

                title = win32gui.GetWindowText(hwnd) or ""

                if "SAP Logon" in title: # Avoid the main SAP window
                    return

                found = hwnd

            win32gui.EnumWindows(cb, None)
            return found

        print("[save_pdf] Search (Save As / PopupHost)...")

        end = time.time() + timeout
        hwnd_dialog = None
        while time.time() < end and hwnd_dialog is None:
            hwnd_dialog = _find_file_dialog()
            if hwnd_dialog is None:
                time.sleep(0.3)

        if hwnd_dialog is None:
            raise RuntimeError("Window Save As not found.")

        title = win32gui.GetWindowText(hwnd_dialog)
        cls = win32gui.GetClassName(hwnd_dialog)
        print(f"[save_pdf] Window in use hwnd={hwnd_dialog}, clase='{cls}', título='{title}'")

        try: # Bring it to the front
            win32gui.SetForegroundWindow(hwnd_dialog)
        except Exception as e:
            print("window of saved no activated:", e)

        time.sleep(0.7)

        pyautogui.hotkey("alt", "n")   # Go to File name field
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(full_path)
        pyautogui.press("enter")

        print(f"[save_pdf] Path written: {full_path}")

    def print_documents(self, file_path, output_folder):
        dataprint = pd.read_excel(file_path, sheet_name='Print').astype(str) #file must have a sheet named 'Print'
        dataprint.columns = (dataprint.columns.str.strip().str.upper().str.replace(r"\s+", "_", regex=True))# Check columns format
        current_year = str(datetime.now().year)

        self.connect_sap() # Connect to SAP if not connected
    

        for _, row in dataprint.iterrows():

            #--------------- MB02 PRINT MATERIAL DOCUMENT ---------------#
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/NMB02" #Transaction code to print material document
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]/usr/ctxtRM07M-MBLNR").text = row["DOCUMENTO"]
            self.session.findById("wnd[0]/usr/txtRM07M-MJAHR").text = current_year #row["AÑO"] # Year of the document
            self.session.findById("wnd[0]/usr/txtRM07M-MJAHR").setFocus()
            self.session.findById("wnd[0]/usr/txtRM07M-MJAHR").caretPosition = 4
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/sub:SAPMM07M:0420/txtMSEG-ERFMG[0,5]").setFocus()
            self.session.findById("wnd[0]/usr/sub:SAPMM07M:0420/txtMSEG-ERFMG[0,5]").caretPosition = 3
            self.session.findById("wnd[0]").sendVKey (2)
            self.session.findById("wnd[0]/tbar[1]/btn[14]").press()
            self.session.findById("wnd[0]/usr/tblSAPDV70ATC_NAST3/ctxtDNAST-KSCHL[1,7]").text = "CF07"
            self.session.findById("wnd[0]/usr/tblSAPDV70ATC_NAST3/ctxtNAST-SPRAS[2,7]").text = "ES"
            self.session.findById("wnd[0]/usr/tblSAPDV70ATC_NAST3/ctxtNAST-SPRAS[2,7]").setFocus()
            self.session.findById("wnd[0]/usr/tblSAPDV70ATC_NAST3/ctxtNAST-SPRAS[2,7]").caretPosition = 2
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/tbar[1]/btn[5]").press()
            self.session.findById("wnd[0]/usr/cmbNAST-VSZTP").key = "4"
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[0]/tbar[1]/btn[2]").press()
            #self.session.findById("wnd[0]/usr/chkNAST-DIMME").selected = True #Flag to print immediately
            self.session.findById("wnd[0]/usr/ctxtNAST-LDEST").text = "LP01"
            self.session.findById("wnd[0]/usr/txtNAST-ANZAL").text = "1"
            self.session.findById("wnd[0]/usr/cmbNAST-TDOCOVER").key = "D"
            self.session.findById("wnd[0]/usr/cmbNAST-TDOCOVER").setFocus()
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            #-------------------------------------------------------#

            #--------------- CHECK PRINT STATUS SP02 ---------------#
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "SP02" #Transaction to check print status
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]").maximize()
            
            try:
                # Try with checkbox
                self.session.findById("wnd[0]/usr/chk[1,3]").selected = True
                self.session.findById("wnd[0]/usr/chk[1,3]").setFocus()
                
            except:
                # Try without checkbox
                self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellColumn = ""
                self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectedRows = "0"

            #-------------------------------------------------------#

            entrega = row["ENTREGA"] # Name of column in excel
            nombre_pdf = f"SAP_{entrega}.pdf"
            carpeta = output_folder
            full_path = os.path.join(carpeta, nombre_pdf)

            t = threading.Thread(
            target=self.save_pdf,
            args=(full_path,),
            daemon=True
            )
            t.start()
            
            time.sleep(0.5) #Wait for thread to start

            #---------------- Select the print job ----------------#
            self.session.findById("wnd[0]/mbar/menu[0]/menu[2]/menu[2]").select()
            #---------------- Come back to main window ----------------#
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()

    #---------- Print documents of identity ----------------
    def save_docs(self, df_print, output_folder):
    # Verificar PDF
        if not getattr(self, 'file_path_doc', None):
            raise FileNotFoundError("No se ha seleccionado un PDF base.")

        pdf_base = self.file_path_doc
        if not os.path.exists(pdf_base):
            raise FileNotFoundError("El PDF seleccionado no existe.")

        # Iterar sobre el DataFrame recibido
        for _, row in df_print.iterrows():
            order = row["ENTREGA"]
            new_pdf_name = f"DOC_{order}.pdf"
            new_pdf_path = os.path.join(output_folder, new_pdf_name)

            shutil.copy(pdf_base, new_pdf_path)

        return True



if __name__ == "__main__":

    sap = SapGui()


    #window = Tk() #Check this late
    #window.geometry("200x60")
    #btn = Button(window, text="Login SAP", command=lambda: SapGui().sapLogin())
    #btn.pack()
    #window.mainloop()

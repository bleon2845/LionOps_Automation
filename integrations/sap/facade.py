from integrations.sap.sap_gui import SapGUI
from integrations.sap.create_order import CreateOrder

class SapFacade:

    def __init__(self, sap_gui: SapGUI):
        self.sap = sap_gui
        self._create_order = None

    #------------ Connection and Login -------------
    def open_and_connect(self,system_name: str = None,index: int = None) -> None:
        self.sap.open_sap()
        self.sap.connect_sap(system_name=system_name, index=index)

    def login(self,username: str, password: str,system_name: str = None) -> bool:
        self.sap.open_sap()
        self.sap.connect_sap(system_name=system_name)
        session = self.sap.session
        if not session:
            raise RuntimeError("SAP session not available. Cannot perform login.")  
        
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password
        session.findById("wnd[0]").sendVKey(0)

        return True

    #------------ Create Order ME21N -------------
    def create_orders(self, excel_path: str):
        if not self.sap.session:
            raise RuntimeError("SAP session not available. Please login first.")

        if not self._create_order:
            self._create_order = CreateOrder(self.sap.session)

        self._create_order.create_documents(excel_path)

    #------------ Save PDF MB02 SP01------------- 
    def print_documents(self, excel_path: str, output_folder: str):
        if not self.sap.session:
            raise RuntimeError("SAP session not available. Please login first.")

        if not self.save_docs_service:
            raise RuntimeError("SaveDocs service not initialized.")

        self.save_docs_service.print_documents(excel_path, output_folder)

    #------------ Create Identity Document -------------
    def save_docs(self, df_print, output_folder):
        if not self.session:
            raise RuntimeError("SAP session not available. Please login first.")

        if not self.save_docs_service:
            raise RuntimeError("SaveDocs service not initialized.")

        self.save_docs_service.save_docs(df_print, output_folder)









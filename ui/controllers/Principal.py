from PySide2.QtWidgets import QWidget
from views.Principal import Principal
from PySide2.QtWidgets import QMainWindow


class Principal(Principal, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.data_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.user_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))

        self.tabla_computadoras_activas.setColumnWidth(0,560)
        self.tabla_computadoras_activas.setColumnWidth(1,560)
        self.tabla_computadoras_activas.setColumnWidth(2,560)

        self.tabla_computadoras_desactivas.setColumnWidth(0,560)
        self.tabla_computadoras_desactivas.setColumnWidth(1,560)
        self.tabla_computadoras_desactivas.setColumnWidth(2,560)


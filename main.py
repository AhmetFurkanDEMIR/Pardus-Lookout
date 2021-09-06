from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from pathlib import Path
import qdarkstyle
import datetime
import FaceMesh
import PyQt5
import sys
import os

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PyQt5.__file__).resolve().parent / "Qt5" / "plugins"
)

Path = "{}/parduspng.ico".format(os.getcwd())
FaceMesh = FaceMesh.FaceMesh()

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self):

        #super().__init__()

        ui.setObjectName("Pardus Lookout")
        ui.resize(1005, 526)
        icon = QtGui.QIcon.fromTheme(Path)
        ui.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(ui)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("")
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 2)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(1)

        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.datetime = datetime.datetime.now()
        self.year = self.datetime.year
        self.month = self.datetime.month
        self.day = self.datetime.day
        self.hour = self.datetime.hour
        self.minute = self.datetime.minute

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.year, self.day, self.month), QtCore.QTime(self.hour, self.minute+5, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.gridLayout_3.addWidget(self.dateTimeEdit, 1, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(self.year, self.day, self.month), QtCore.QTime(self.hour+1, self.minute+5, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.gridLayout_3.addWidget(self.dateTimeEdit_2, 2, 1, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName("checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName("checkBox_3")

        self.gridLayout_4.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)

        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2.setMaximum(240)
        self.spinBox_2.setValue(2)
        self.spinBox_2.setObjectName("spinBox_2")

        self.gridLayout_4.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setObjectName("radioButton_2")

        self.gridLayout_5.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName("radioButton")

        self.gridLayout_5.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setObjectName("radioButton_3")

        self.gridLayout_5.addWidget(self.radioButton_3, 2, 0, 1, 1)

        self.verticalLayout.addWidget(self.groupBox_4)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 5)

        self.icon = QtGui.QIcon("icon.png")

        # Create the tray
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(False)

        # Create the menu
        self.menu = QtWidgets.QMenu()

        self.actionNor = QtWidgets.QAction("Normalize")
        self.NormalLambda = lambda:(ui.showNormal(),self.tray.setVisible(False))
        self.actionNor.triggered.connect(self.NormalLambda)
        self.menu.addAction(self.actionNor)

        self.actionMin = QtWidgets.QAction("Minimize")
        self.MinimizeLambda = lambda:(ui.showMinimized(),self.tray.setVisible(False))
        self.actionMin.triggered.connect(self.MinimizeLambda)
        self.menu.addAction(self.actionMin)

        # Add a Quit option to the menu.
        self.quit = QtWidgets.QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)

        # Add the menu to the tray
        self.tray.setContextMenu(self.menu)

        ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)

    def retranslateUi(self, ui):

        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("MainWindow", "Pardus Lookout"))

        FaceMesh.StartTime = self.dateTimeEdit.dateTime().toString(self.dateTimeEdit.displayFormat())
        FaceMesh.FinishTime = self.dateTimeEdit_2.dateTime().toString(self.dateTimeEdit.displayFormat())

        self.groupBox.setTitle(_translate("MainWindow", "Screen Privacy"))
        self.checkBox.setText(_translate("MainWindow", "Activate"))
        self.label_2.setText(_translate("MainWindow", "Tolerated Faces :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Screen Sentry"))
        self.label_4.setText(_translate("MainWindow", "Finish Time : "))
        self.checkBox_2.setText(_translate("MainWindow", "Activate"))
        self.label_3.setText(_translate("MainWindow", "Start Time :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sleep Mode"))
        self.checkBox_3.setText(_translate("MainWindow", "Activate"))
        self.label_5.setText(_translate("MainWindow", "Inactivity Time (Min) :"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Action to be taken"))
        self.radioButton_2.setText(_translate("MainWindow", "Suspend"))
        self.radioButton.setText(_translate("MainWindow", "Shut Down"))
        self.radioButton_3.setText(_translate("MainWindow", "Warn"))

        self.checkBox.toggled.connect(self.PrivacyCheck)
        self.checkBox_2.toggled.connect(self.SentryCheck)
        self.checkBox_3.toggled.connect(self.SleepCheck)
        self.radioButton.toggled.connect(self.ActionRadio)
        self.radioButton_2.toggled.connect(self.ActionRadio)
        self.radioButton_3.toggled.connect(self.ActionRadio)

        self.spinBox.valueChanged.connect(self.FacesSpinBox)
        self.spinBox_2.valueChanged.connect(self.FacesSpinBox)

        self.dateTimeEdit.dateTimeChanged.connect(self.TimeCheck)
        self.dateTimeEdit_2.dateTimeChanged.connect(self.TimeCheck)

        self.timer=QTimer()
        self.timer.timeout.connect(self.loopVideoRead)
        self.timer.start(30)

    def PrivacyCheck(self):

        if FaceMesh.Action=="":

            if self.checkBox.isChecked()==False:

                return

            self.checkBox.setChecked(False)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select the action to take.")
            msg.setWindowTitle("Error")
            msg.exec_()

            return

        elif self.checkBox.isChecked():

            self.checkBox.setText("Deactivate")
            FaceMesh.notificationCo = 500           
            FaceMesh.Privacy=1

        else:

            self.checkBox.setText("Activate")
            FaceMesh.notificationCo = 500
            FaceMesh.Privacy=0

    def SentryCheck(self):

        if FaceMesh.Action=="":

            if self.checkBox_2.isChecked()==False:

                return

            self.checkBox_2.setChecked(False)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select the action to take.")
            msg.setWindowTitle("Error")
            msg.exec_()

            return

        elif self.checkBox_2.isChecked():

            self.checkBox_2.setText("Deactivate")
            FaceMesh.notificationSe=500       
            FaceMesh.Sentry=1

        else:

            self.checkBox_2.setText("Activate")
            FaceMesh.notificationSe=500
            FaceMesh.Sentry=0

    def SleepCheck(self):

        if FaceMesh.Action=="":

            if self.checkBox_3.isChecked()==False:

                return

            self.checkBox_3.setChecked(False)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select the action to take.")
            msg.setWindowTitle("Error")
            msg.exec_()

            return

        elif self.checkBox_3.isChecked():

            self.checkBox_3.setText("Deactivate")
            FaceMesh.notificationSl=500         
            FaceMesh.Sleep=1

        else:

            self.checkBox_3.setText("Activate")
            FaceMesh.notificationSl=500
            FaceMesh.Sleep=0

    def ActionRadio(self,checked):

        FaceMesh.notificationSl=500
        FaceMesh.notificationSe=500
        FaceMesh.notificationCo = 500

        if self.radioButton.isChecked():

            FaceMesh.Action="ShutDown"

        elif self.radioButton_2.isChecked():

            FaceMesh.Action="Suspend"

        elif self.radioButton_3.isChecked():

            FaceMesh.Action="Warn"

    def FacesSpinBox(self):

        if FaceMesh.ToleratedFaces!=self.spinBox.value():

            FaceMesh.notificationCo = 500

        if FaceMesh.InactivityTime!=self.spinBox_2.value():

            FaceMesh.notificationSl=500


        FaceMesh.ToleratedFaces = self.spinBox.value()
        FaceMesh.InactivityTime = self.spinBox_2.value()

    def TimeCheck(self):

        FaceMesh.notificationSe=500
        FaceMesh.StartTime = self.dateTimeEdit.dateTime().toString(self.dateTimeEdit.displayFormat())
        FaceMesh.FinishTime = self.dateTimeEdit_2.dateTime().toString(self.dateTimeEdit.displayFormat())


    def closeEvent(self, event):
        
        self.tray.setVisible(True)
        ui.hide()
        event.ignore()



    def loopVideoRead(self):

        self.frame = FaceMesh.readFrame()

        self.qimg = QtGui.QImage(self.frame,self.frame.shape[1], self.frame.shape[0], QtGui.QImage.Format_RGB888)
        self.pixmapb = QtGui.QPixmap.fromImage(self.qimg)
        self.label.setPixmap(self.pixmapb)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

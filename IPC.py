from Xipc import *
from PyQt5.QtWidgets import QApplication, QWidget
from sys import exit,argv
from matplotlib.pyplot import plot,suptitle,subplot2grid,title,xlabel,ylabel,show

class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ventana_()
        self.ui.setupUi(self)
        self.porcentaje1 = 1
        self.porcentaje2= 1
        self.porcentaje3 = 1
        self.porcentaje4 = 1
        self.ano01 = 1
        self.ano02 = 1
        self.ano03 = 1
        self.ano04 = 1
        self.ano05 = 1
        self.ano11 = 1
        self.ano12 = 1
        self.ano13 = 1
        self.ano14 = 1
        self.ano21 = 1
        self.ano22 = 1
        self.ano23 = 1
        self.ano24 = 1
        self.calculo1 = 0
        self.calculo2 = 0

        self.ui.inputAno2.clicked.connect(self.activar1)
        self.ui.inputBienes4.clicked.connect(self.activar2)
        self.ui.inputBienes3.clicked.connect(self.activar3)
        self.ui.inputBienes2.clicked.connect(self.activar4)
        self.ui.botonGrafico.clicked.connect(self.boton)
    def activar1(self):
        if self.ui.inputAno2.isChecked() == True:
            self.ui.inputBienes4.setEnabled(True)
            self.ui.inputBienes3.setEnabled(True)
            self.ui.inputBienes2.setEnabled(True)
    def activar2(self):
        if self.ui.inputBienes4.isChecked() == True:
            self.ui.inputPorcentaje1.setEnabled(True)
            self.ui.inputPorcentaje2.setEnabled(True)
            self.ui.inputPorcentaje3.setEnabled(True)
            self.ui.inputPorcentaje4.setEnabled(True)
            self.ui.inputAno01.setEnabled(True)
            self.ui.inputAno02.setEnabled(True)
            self.ui.inputAno03.setEnabled(True)
            self.ui.inputAno04.setEnabled(True)
            self.ui.inputAno11.setEnabled(True)
            self.ui.inputAno12.setEnabled(True)
            self.ui.inputAno13.setEnabled(True)
            self.ui.inputAno14.setEnabled(True)
            self.ui.inputAno21.setEnabled(True)
            self.ui.inputAno22.setEnabled(True)
            self.ui.inputAno23.setEnabled(True)
            self.ui.inputAno24.setEnabled(True)

            if self.ui.inputAno2.isChecked() == True:
                self.ui.botonGrafico.setEnabled(True)
            else:
                self.ui.botonGrafico.setEnabled(False)

    def activar3(self):
        if self.ui.inputBienes3.isChecked() == True:
            self.ui.inputPorcentaje1.setEnabled(True)
            self.ui.inputPorcentaje2.setEnabled(True)
            self.ui.inputPorcentaje3.setEnabled(True)
            self.ui.inputPorcentaje4.setEnabled(False)
            self.ui.inputAno01.setEnabled(True)
            self.ui.inputAno02.setEnabled(True)
            self.ui.inputAno03.setEnabled(True)
            self.ui.inputAno04.setEnabled(False)
            self.ui.inputAno11.setEnabled(True)
            self.ui.inputAno12.setEnabled(True)
            self.ui.inputAno13.setEnabled(True)
            self.ui.inputAno14.setEnabled(False)
            self.ui.inputAno21.setEnabled(True)
            self.ui.inputAno22.setEnabled(True)
            self.ui.inputAno23.setEnabled(True)
            self.ui.inputAno24.setEnabled(False)
            if self.ui.inputAno2.isChecked() == True:
                self.ui.botonGrafico.setEnabled(True)
            else:
                self.ui.botonGrafico.setEnabled(False)

    def activar4(self):
        if self.ui.inputBienes2.isChecked() == True:
            self.ui.inputPorcentaje1.setEnabled(True)
            self.ui.inputPorcentaje2.setEnabled(True)
            self.ui.inputPorcentaje3.setEnabled(False)
            self.ui.inputPorcentaje4.setEnabled(False)
            self.ui.inputAno01.setEnabled(True)
            self.ui.inputAno02.setEnabled(True)
            self.ui.inputAno03.setEnabled(False)
            self.ui.inputAno04.setEnabled(False)
            self.ui.inputAno11.setEnabled(True)
            self.ui.inputAno12.setEnabled(True)
            self.ui.inputAno13.setEnabled(False)
            self.ui.inputAno14.setEnabled(False)
            self.ui.inputAno21.setEnabled(True)
            self.ui.inputAno22.setEnabled(True)
            self.ui.inputAno23.setEnabled(False)
            self.ui.inputAno24.setEnabled(False)
            if self.ui.inputAno2.isChecked() == True:
                self.ui.botonGrafico.setEnabled(True)
            else:
                self.ui.botonGrafico.setEnabled(False)
    def boton(self):
        if self.ui.inputAno2.isEnabled() == True and self.ui.inputPorcentaje4.isEnabled() == True and self.ui.inputPorcentaje3.isEnabled() == True:
            self.ui.botonGrafico.setEnabled(True)
            self.porcentaje1 = self.ui.inputPorcentaje1.value()
            self.porcentaje2 = self.ui.inputPorcentaje2.value()
            self.porcentaje3 = self.ui.inputPorcentaje3.value()
            self.porcentaje4 = self.ui.inputPorcentaje4.value()
            self.ano01 = self.ui.inputAno01.value()
            self.ano02 = self.ui.inputAno02.value()
            self.ano03 = self.ui.inputAno03.value()
            self.ano04 = self.ui.inputAno04.value()
            self.ano11 = self.ui.inputAno11.value()
            self.ano12 = self.ui.inputAno12.value()
            self.ano13 = self.ui.inputAno13.value()
            self.ano14 = self.ui.inputAno14.value()
            self.ano21 = self.ui.inputAno21.value()
            self.ano22 = self.ui.inputAno22.value()
            self.ano23 = self.ui.inputAno23.value()
            self.ano24 = self.ui.inputAno24.value()
            self.calculos1 = (self.porcentaje1 * (self.ano11 / self.ano01)) + (self.porcentaje2 * (self.ano12 / self.ano02)) + (self.porcentaje3 * (self.ano13 / self.ano03)) + (self.porcentaje4 * (self.ano14 / self.ano04))
            self.calculos2 = (self.porcentaje1 * (self.ano21 / self.ano01)) + (self.porcentaje2 * (self.ano22 / self.ano02)) + (self.porcentaje3 * (self.ano23 / self.ano03)) + (self.porcentaje4 * (self.ano24 / self.ano04))

            X = [1, 2]
            Y1 = []
            Y2 = []

            Y1.append(100)
            Y2.append(100)
            Y1.append(self.calculos1)
            Y2.append(self.calculos2)
            total = []
            total.append(Y1[1])
            total.append(Y2[1])

            suptitle("Evolución del IPC", fontsize=26)
            subplot2grid((2, 2), (0, 0), rowspan=2)
            title("Total del IPC", fontsize=18)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, total)

            subplot2grid((2, 2), (0, 1))
            title("IPC del Año 1", fontsize=15)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, Y2)

            subplot2grid((2, 2), (1, 1))
            title("IPC del Año 2", fontsize=15)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, Y1)
            show()
        elif self.ui.inputAno2.isEnabled() == True and self.ui.inputPorcentaje4.isEnabled() == False and self.ui.inputPorcentaje3.isEnabled() == True:
            self.ui.botonGrafico.setEnabled(True)
            self.porcentaje1 = self.ui.inputPorcentaje1.value()
            self.porcentaje2 = self.ui.inputPorcentaje2.value()
            self.porcentaje3 = self.ui.inputPorcentaje3.value()

            self.ano01 = self.ui.inputAno01.value()
            self.ano02 = self.ui.inputAno02.value()
            self.ano03 = self.ui.inputAno03.value()

            self.ano11 = self.ui.inputAno11.value()
            self.ano12 = self.ui.inputAno12.value()
            self.ano13 = self.ui.inputAno13.value()

            self.ano21 = self.ui.inputAno21.value()
            self.ano22 = self.ui.inputAno22.value()
            self.ano23 = self.ui.inputAno23.value()

            self.calculos1 = (self.porcentaje1 * (self.ano11 / self.ano01)) + (self.porcentaje2 * (self.ano12 / self.ano02)) + (self.porcentaje3 * (self.ano13 / self.ano03))
            self.calculos2 = (self.porcentaje1 * (self.ano21 / self.ano01)) + (self.porcentaje2 * (self.ano22 / self.ano02)) + (self.porcentaje3 * (self.ano23 / self.ano03))

            X = [1, 2]
            Y1 = []
            Y2 = []

            Y1.append(100)
            Y2.append(100)
            Y1.append(self.calculos1)
            Y2.append(self.calculos2)
            total = []
            total.append(Y1[1])
            total.append(Y2[1])

            suptitle("Evolución del IPC", fontsize=26)
            subplot2grid((2, 2), (0, 0), rowspan=2)
            title("Total del IPC", fontsize=18)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, total)

            subplot2grid((2, 2), (0, 1))
            title("IPC del Año 1", fontsize=15)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, Y2)

            subplot2grid((2, 2), (1, 1))
            title("IPC del Año 2", fontsize=15)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, Y1)
            show()
        elif self.ui.inputAno2.isEnabled() == True and self.ui.inputPorcentaje4.isEnabled() == False and self.ui.inputPorcentaje3.isEnabled() == False:
            self.ui.botonGrafico.setEnabled(True)
            self.porcentaje1 = self.ui.inputPorcentaje1.value()
            self.porcentaje2 = self.ui.inputPorcentaje2.value()

            self.ano01 = self.ui.inputAno01.value()
            self.ano02 = self.ui.inputAno02.value()

            self.ano11 = self.ui.inputAno11.value()
            self.ano12 = self.ui.inputAno12.value()


            self.ano21 = self.ui.inputAno21.value()
            self.ano22 = self.ui.inputAno22.value()


            self.calculos1 = (self.porcentaje1 * (self.ano11 / self.ano01)) + (self.porcentaje2 * (self.ano12 / self.ano02))
            self.calculos2 = (self.porcentaje1 * (self.ano21 / self.ano01)) + (self.porcentaje2 * (self.ano22 / self.ano02))

            X = [1,2]
            Y1 = []
            Y2 = []

            Y1.append(100)
            Y2.append(100)
            Y1.append(self.calculos1)
            Y2.append(self.calculos2)
            total = []
            total.append(Y1[1])
            total.append(Y2[1])

            suptitle("Evolución del IPC", fontsize=26)
            subplot2grid((2, 2), (0, 0), rowspan=2)
            title("Total del IPC", fontsize=18)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, total)

            subplot2grid((2, 2), (0, 1))
            title("IPC del Año 1", fontsize=15)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, Y2)

            subplot2grid((2, 2), (1, 1))
            title("IPC del Año 2", fontsize=15)
            xlabel("Numero de Años")
            ylabel("Valor del IPC ")
            plot(X, Y1)
            show()
        else:
            self.ui.botonGrafico.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(argv)
    miclase = Aplicacion()
    miclase.show()
    exit(app.exec_())

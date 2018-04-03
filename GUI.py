import sys
import matplotlib
from Calculations import Calculations
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QGridLayout,
                               QSizePolicy, QFrame, QTabWidget, QGroupBox)

class PlotCanvas(FigureCanvas):
    fig = plt.figure()
    def __init__(self, parent=None, width=3.5, height=3.5, dpi=100):
        global fig
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, a, b,c, name):   # method that generates plots in matplotlib by given X, Y params. create two plots on one canvas ( 1st line of plots)
        # a - x values, same for both plots, b ,c values- Y params
        global grid
        self.figure.clear()
        ax = self.figure.add_subplot(1,1,1)
        ax.plot(a, b, color='red')
        ax.plot(a, c, color='blue')
        ax.grid()
        ax.axis([0, 3, 0, 4])
        ax.set_title(name)
        self.draw()

    def plot1(self, a, b, name):    # generates error plot
        global grid
        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)
        ax.plot(a, b, color='red')
        max = b[-1]
        ax.grid()
        ax.yaxis.set_tick_params(labelsize=5.8, rotation=50)
        ax.axis([0, 3, 0, 1.5*max])
        plt.tight_layout()
        ax.set_title(name)
        self.draw()

    def plot2(self, a, b, name):    # generates plot of dependance of max error on num of ticks
        global grid
        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)
        ax.plot(a, b, color='red')
        max = b[0]
        ax.grid()
        ax.yaxis.set_tick_params(labelsize=5.8, rotation=50)
        ax.axis([0, a[-1]+a[1]-a[0], 0, 1.5*max])
        ax.set_title(name)
        self.draw()


class Example(QWidget):
    grid = 0.2
    euler = PlotCanvas()
    euler_adv = PlotCanvas()
    cutta = PlotCanvas()
    all = PlotCanvas()
    def __init__(self):     # main method that contain constructor for GUI based on PyQt5 lib
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 1350
        self.height = 900
        self.setWindowTitle('lol')
        self.setGeometry(self.left, self.top, self.width, self.height)
        tab_1 = QFrame()
        self.euler = PlotCanvas(self, width=3.5, height=3.5)
        self.euler_adv = PlotCanvas(self, width=3.5, height=3.5)
        self.cutta = PlotCanvas(self, width=3.5, height=3.5)
        self.euler_error = PlotCanvas(self, width=3.5, height=3.5)
        self.euler_adv_error = PlotCanvas(self, width=3.5, height=3.5)
        self.cutta_error = PlotCanvas(self, width=3.5, height=3.5)
        self.btn = QPushButton('run', self)
        self.titleEdit = QLineEdit()
        self.btn.resize(30, 40)
        self.titleEdit.resize(30, 40)
        self.horizontalGroupBox = QGroupBox("Grid")
        self.scrlbl = QLabel(self)
        self.scrlbl.setText( 'enter how much steps to do:')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.btn)
        vbox2.addWidget(self.scrlbl)
        vbox2.addWidget(self.titleEdit)
        vbox2.addStretch(1)

        layout_tab_1 = QHBoxLayout()
        layout_tab_1.addWidget(self.euler)
        layout_tab_1.addStretch(1)
        layout_tab_1.addWidget(self.euler_adv)
        layout_tab_1.addStretch(1)
        layout_tab_1.addWidget(self.cutta)
        layout_tab_1.addStretch(1)
        layout_tab_1.addLayout(vbox2)
        layout_tab_1.addStretch(1)          # just a lot of "design" code

        layout_tab_1_2 = QHBoxLayout()
        layout_tab_1_2.addWidget(self.euler_error)
        layout_tab_1_2.addStretch(1)
        layout_tab_1_2.addWidget(self.euler_adv_error)
        layout_tab_1_2.addStretch(1)
        layout_tab_1_2.addWidget(self.cutta_error)
        layout_tab_1_2.addStretch(15)

        v_layout=QVBoxLayout()
        v_layout.addLayout(layout_tab_1)
        v_layout.addStretch()
        v_layout.addLayout(layout_tab_1_2)
        tab_1.setLayout(v_layout)

        self.euler_hop_error=PlotCanvas(self, width=4, height=4)
        self.euler_adv_hop_error=PlotCanvas(self, width=4, height=4)
        self.cutta_hop_error=PlotCanvas(self, width=4, height=4)
        self.btn3 = QPushButton('run', self)
        self.titleEdit1 = QLineEdit()
        self.scrlbl1 = QLabel(self)
        self.scrlbl1.setText('set low border\n for steps:')

        self.titleEdit2 = QLineEdit()
        self.scrlbl2 = QLabel(self)
        self.scrlbl2.setText('set high border\n for steps:')
        self.titleEdit3 = QLineEdit()
        self.scrlbl3 = QLabel(self)
        self.scrlbl3.setText('set how much steps\n to do:')

        tab2_button_layout = QVBoxLayout()
        tab2_button_layout.addWidget(self.btn3)
        tab2_button_layout.addWidget(self.scrlbl1)
        tab2_button_layout.addWidget(self.titleEdit1)
        tab2_button_layout.addWidget(self.scrlbl2)
        tab2_button_layout.addWidget(self.titleEdit2)
        tab2_button_layout.addWidget(self.scrlbl3)
        tab2_button_layout.addWidget(self.titleEdit3)
        tab2_button_layout.addStretch(1)

        tab_2 = QFrame()
        tab2_hlayout = QHBoxLayout()
        tab2_hlayout.addWidget(self.euler_hop_error)
        tab2_hlayout.addStretch(1)
        tab2_hlayout.addLayout(tab2_button_layout)
        tab2_hlayout.addStretch(4)

        tab2_hlayout2 = QHBoxLayout()
        tab2_hlayout2.addWidget(self.euler_adv_hop_error)
        tab2_hlayout2.addStretch(1)
        tab2_hlayout2.addWidget(self.cutta_hop_error)
        tab2_hlayout2.addStretch(15)

        tab2_vlayout = QVBoxLayout()
        tab2_vlayout.addLayout(tab2_hlayout)
        tab2_vlayout.addStretch()
        tab2_vlayout.addLayout(tab2_hlayout2)
        tab_2.setLayout(tab2_vlayout)

        self.tab = QTabWidget()
        self.tab.addTab(tab_1, "exact + error plots")
        self.tab.addTab(tab_2, "Max error plots")
        main_layout = QGridLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)
        self.btn.clicked.connect(self.button1_click)
        self.btn3.clicked.connect(self.button3_click)
        self.show()

    def button1_click(self):        #button of resetting first page of program, run Calculations methods for getting new results
        hop = self.titleEdit.text()
        calc = Calculations(hop)
        values = calc.get_y()
        x_points = calc.get_x()
        exact = values[0]
        euler = values[1]
        euler_adv = values[2]
        cutta = values[3]


        self.euler.plot(x_points, exact, euler, 'Euler + exact')
        self.euler_adv.plot(x_points, exact, euler_adv, 'Euler advanced + exact')
        self.cutta.plot(x_points, exact, cutta, 'Runge_cutta + exact')
        e_error = calc.x_error_plot(1)
        self.euler_error.plot1(x_points, e_error, 'Euler errors')
        e_A_error = calc.x_error_plot(2)
        self.euler_adv_error.plot1(x_points, e_A_error, 'Euler advanced errors')
        cut_error = calc.x_error_plot(3)
        self.cutta_error.plot1(x_points, cut_error, 'Runge_cutta errors')

    def button3_click(self):                            #button of resetting second page of program, run Calculations methods for getting new results
        num_of_ticks = int(self.titleEdit3.text())
        start = float(self.titleEdit1.text())
        end = float(self.titleEdit2.text())
        calc = Calculations(num_of_ticks)
        hop = ((end-start)/num_of_ticks)
        x_v =[]
        for i in range(num_of_ticks+1):
            x_v.append(start + i*hop)
        values1 = calc.hop_error_plot(start, end, hop, 1)
        values2 = calc.hop_error_plot(start, end, hop, 2)
        values3 = calc.hop_error_plot(start, end, hop, 3)
        self.euler_hop_error.plot2(x_v,values1,'Dependence of max value error on\n number of ticks (Euler)')
        self.euler_adv_hop_error.plot2(x_v,values2,'Dependence of max value error on\n number of ticks (Euler_adv)')
        self.cutta_hop_error.plot2(x_v,values3,'Dependence of max value error on\n number of ticks (Runge-Cutta)')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

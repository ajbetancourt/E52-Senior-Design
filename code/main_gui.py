#4 buttons upload file, new graph, save
#visuals cnc conneted/unconnected--needs to be be for new graph
import numpy as np
import sys
#from plot3D import plot as plt3D
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import run.py as runClick
import zaxistest as step_motor


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class plot(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):   
        def randrange(n, vmin, vmax):
            '''
            Helper function to make an array of random numbers having shape (n, )
            with each number distributed Uniform(vmin, vmax).
            '''
            return (vmax - vmin)*np.random.rand(n) + vmin
        # Get data 


        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
  
        n = 100

        # For each set of style and range settings, plot n random points in the box
        # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
        x,y,z,b = plot_points()

        ax.scatter(xs, ys, zs, c=c, marker=m)
        
        ax.set_xlabel('X inches ')
        ax.set_ylabel('Y inches')
        ax.set_zlabel('Z inches')
        #plt.show()
        super(plot, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QGridLayout()      

        sc = plot(self, width=5, height=4, dpi=100)
        # def color_gradient():
        #     #max min value for b field then linear gradient from blue (high) to red(low)

        # def upload():
        #     #df
        # def run():
        #     #df

        # def save():
        #     #df


        toolbar = NavigationToolbar(sc, self)

        btnLayout = QHBoxLayout()
  
        runButton = QPushButton('Run', self)
        runButton.clicked.connect(runClick.motor_data(7)) ##fix later 
        btnLayout.addWidget(runButton)

        

        motorCal = QPushButton('Move Motor Down', self)
        motorCal.clicked.connect(step_motor.move_down()) ##fix later
        btnLayout.addWidget(motorCal)
     
        combo = QComboBox()
        combo.addItems(['1/8"','1/2"','3/4"','1"'])
        btnLayout.addWidget(combo)
     
        button_master = QWidget()
        button_master.setLayout(btnLayout)
    
        layout.addWidget(button_master, 0, 4)
        layout.addWidget(toolbar, 1, 4)
        layout.addWidget(sc, 2 ,4 ,20 ,4)
        layWidget = QWidget()
        layWidget.setLayout(layout)
        self.setCentralWidget(layWidget)
    
    def plot_pts():
        ''' These are just for plot testing they will be from a txt file, the end goal being to map in 
        real time --function will call the text file as its being edited, or will upload full txt file'''
        zvals = [0,0,0,0,0,0,0,0]
        for l in range (0,8):
            zvals[l] = l
        xvals = [0,0,0,0,0,0,0,0]
        yvals = [0,0,0,0,0,0,0,0]
        b_field_z = runClick.plot_points
        return xvals, yvals, b_field_z


if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.showMaximized()
    app.exec_()

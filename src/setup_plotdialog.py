import sys
import sqlite3
import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.plotdialog import Ui_PlotDialog
from src.msgboxgenerate import standartbox

class PlotDialog(QDialog, Ui_PlotDialog):
    """ Opens up the plotdialog when the button on the optionscreen is clicked
    Inherits the properties from the mainwindow.
    """

    def __init__(self, parent):
        """ Init function for the MasterDialog class. """
        super(PlotDialog, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ms = parent
        self.devenvironment = self.ms.devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        # connect the buttons
        self.PB_plot_active.clicked.connect(lambda: self.plot_clicked(active=True))
        self.PB_plot_all.clicked.connect(lambda: self.plot_clicked(active=False))
        self.PB_back.clicked.connect(self.back_clicked)

    def plot_clicked(self, active=True):
        """ Plot a leaderboard of the best x employees. By best is ment the most entries. 
        Differentiates between all DB entries, and only still active employees.
        """
        # Selects the 5 employes with the highest comsumption either from all ore active
        if active:
            bonusstring = " WHERE enabled=1"
            headerstring="(active)"
        else:
            bonusstring = ""
            headerstring="(all time)"
        employee_data = self.ms.c.execute("SELECT first_name, last_name, amount FROM employees{} ORDER BY amount DESC LIMIT 5".format(bonusstring))
        namelist = []
        amountlist =  []
        # generates a list of the employees and values for later plotting, only picks up the five highest
        for row in employee_data:
            last_name = row[1]
            namelist.append("{} {}.".format(row[0], last_name[0]))
            amountlist.append(row[2])
        # just for plotting the values of the output
        # print(20*"-")
        # for name, amount in zip(namelist, amountlist):
        #     print(name, amount)
        # opens up the window for the plot
        self.graphwindow = GraphWindow(self, plotvalues=amountlist[::-1], plotlabels=namelist[::-1], headerstring=headerstring)
        self.graphwindow.showFullScreen()

    def back_clicked(self):
        """ Closes the window without any further action. """
        self.close()


class GraphWindow(QDialog):
    """
    Opens up a window where the the top five useres (highes quantity) are shown.

    Parameters:
        -- plotvalues: The values for the bars
        -- plotlabels: The labels for the bars
        -- headerstring: Depreciated, renames the window titel, is not shown anymore in fullscreen
    """
    def __init__(self, parent, plotvalues=None, plotlabels=None, headerstring="all time"):
        super(GraphWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(480, 320)
        self.setMinimumSize(QSize(0, 0))
        self.setMaximumSize(QSize(480, 320))
        self.setWindowTitle("Leaderboard {}".format(headerstring))
        self.setModal(True)
        self.ms = parent
        self.devenvironment = self.ms.devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        # a figure instance to plot on
        self.figure = plt.figure(figsize=(2.874, 1.916), dpi=167)
        # adds a button to go back
        self.backbutton = QPushButton('< Back')
        # sets the minimum size and the fontsize
        self.backbutton.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backbutton.setFont(font)
        self.backbutton.clicked.connect(self.back_clicked)
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.backbutton)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # clears the old values and then adds a subplot to isert all the data
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # plots a horizontal bargraph with the values and the namelabels
        y_pos = np.arange(len(plotlabels))
        ax.xaxis.grid(linestyle='--', color='w', zorder=0)
        # generates a color grade from red to blue
        clist = [(0, '#1f77b4'), (1, '#d62728')]
        rvb = mcolors.LinearSegmentedColormap.from_list("", clist)
        ax.barh(y_pos, plotvalues, tick_label=plotlabels, zorder=3, height=0.9, color=rvb(y_pos/len(plotlabels)))
        # gets the numbers in front of each bar
        for i, v in enumerate(plotvalues):
            ax.text(max(plotvalues)/50, i-0.05, str(v), color='w', fontweight='bold', va='center', fontsize=10)
        # removes the ticks from each axis
        for ticx in ax.xaxis.get_major_ticks():
            ticx.tick1line.set_visible(False)
            ticx.tick2line.set_visible(False)
        for ticy in ax.yaxis.get_major_ticks():
            ticy.tick1line.set_visible(False)
            ticy.tick2line.set_visible(False)
        # recolours the style into invers (black is white, white is black)
        self.figure.patch.set_facecolor('k')
        ax.patch.set_facecolor('k')
        ax.spines['bottom'].set_color('w')
        ax.spines['top'].set_color('w')
        ax.spines['left'].set_color('w')
        ax.spines['right'].set_color('w')
        plt.setp(ax.get_xticklabels(), color="w", fontsize=8)
        plt.setp(ax.get_yticklabels(), color="w", fontsize=8)
        plt.tight_layout()
        # refresh canvas
        self.canvas.draw()

    def back_clicked(self):
        """ Closes the window. """
        self.close()

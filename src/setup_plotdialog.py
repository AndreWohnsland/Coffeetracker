import sys
import sqlite3
import datetime
import matplotlib.pyplot as plt
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
        self.ms = parent
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
        employee_data = self.ms.c.execute("SELECT first_name, last_name, amount FROM employees{} ORDER BY amount DESC".format(bonusstring))
        namelist = []
        amountlist =  []
        # generates a list of the employees and values for later plotting, currently only prints them out
        for number, row in enumerate(employee_data):
            if number == 5:
                break
            last_name = row[1]
            namelist.append("      {} {}.".format(row[0], last_name[0]))
            amountlist.append(row[2])
        print(20*"-")
        for name, amount in zip(namelist, amountlist):
            print(name, amount)
        self.graphwindow = GraphWindow(self, plotvalues=amountlist, plotlabels=namelist, headerstring=headerstring)
        self.graphwindow.show()
        # y_pos = np.arange(len(namelist))
        # plt.barh(y_pos, amountlist, align='center')
        # plt.yticks(y_pos, namelist)
        # plt.show()

    def back_clicked(self):
        """ Closes the window without any further action. """
        self.close()


class GraphWindow(QDialog):
    """ A Popup window to show a graph of the user with the most quantities. """
    def __init__(self, parent, plotvalues=None, plotlabels=None, headerstring="all time"):
        super(GraphWindow, self).__init__(parent)
        self.resize(480, 320)
        self.setMinimumSize(QSize(480, 320))
        self.setMaximumSize(QSize(480, 320))
        self.setWindowTitle("Leaderboard {}".format(headerstring))
        # a figure instance to plot on
        self.figure = plt.figure()
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # clears the old values and then adds a subplot to isert all the data
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # plots a horizontal bargraph with the values and the namelabels
        y_pos = np.arange(len(plotlabels))
        ax.xaxis.grid(linestyle='--', color='w', zorder=0)
        ax.barh(y_pos, plotvalues, tick_label=plotlabels, zorder=3)
        # gets the numbers in front of each bar
        for i, v in enumerate(plotvalues):
            ax.text(max(plotvalues)/50, i-0.05, str(v), color='w', fontweight='bold', va='center', fontsize=14)
        # removes the ticks from each axis
        for ticx in ax.xaxis.get_major_ticks():
            ticx.tick1On = ticx.tick2On = False
        for ticy in ax.yaxis.get_major_ticks():
            ticy.tick1On = ticy.tick2On = False
        # recolours the style into invers (black is white, white is black)
        self.figure.patch.set_facecolor('k')
        ax.patch.set_facecolor('k')
        ax.spines['bottom'].set_color('w')
        ax.spines['top'].set_color('w')
        ax.spines['left'].set_color('w')
        ax.spines['right'].set_color('w')
        plt.setp(ax.get_xticklabels(), color="w", fontsize=12)
        plt.setp(ax.get_yticklabels(), color="w", fontsize=12)
        plt.tight_layout()
        # refresh canvas
        self.canvas.draw()
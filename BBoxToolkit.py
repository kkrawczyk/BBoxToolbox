import inspect
import os

from PyQt5.QtWidgets import QAction
from qgis.PyQt.QtGui import *

from .ui import BBoxPreviewWindow


class BBoxToolkit(object):

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.action = QAction(QIcon(os.path.join(current_directory, "icons", "app-icon.png")),
                              "&Bounding box toolkit", self.iface.mainWindow())
        self.action.triggered.connect(self.showMainDialog)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Bounding box toolkit", self.action)
        # self.geocodingWidget = GeocodingDockWidget(self.iface)
        # self.iface.addDockWidget(Qt.BottomDockWidgetArea, self.geocodingWidget)

    def unload(self):
        self.iface.removePluginMenu("Bounding box toolkit", self.action)
        self.iface.removeToolBarIcon(self.action)
        # self.iface.removeDockWidget(self.geocodingWidget)

    def showMainDialog(self):
        self.bboxPreviewWindow = BBoxPreviewWindow(self.iface)
        self.bboxPreviewWindow.show()

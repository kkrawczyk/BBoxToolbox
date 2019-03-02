import os

import qgis
import qgis.core
from qgis.PyQt import uic

from .. import biz

try:
    from qgis.PyQt.QtGui import QDialog, QMessageBox
except ImportError:
    from qgis.PyQt.QtWidgets import QDialog, QMessageBox


class BBoxPreviewWindow(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        ui_path = os.path.join(os.path.dirname(__file__), 'BBoxPreviewWindow.ui')
        uic.loadUi(ui_path, self)
        self.bboxString.setPlainText(
            '[20.09329832743496169, 21.92297676502402126, 52.71931350015093187, 51.73818035812892191]')
        self.showButton.clicked.connect(self.showBbox)
        self.formatManager = biz.FormatManager()
        for format in self.formatManager.formatClasses:
            self.formatsComboBox.addItem(self.formatManager.formatClasses[format].displayName(), format)

    def showBbox(self):
        bboxString = self.bboxString.toPlainText()
        layer = self.destinationLayer.currentLayer()
        crs = self.projectionSelectionWidget.crs()
        selectedFormat = self.formatsComboBox.itemData(self.formatsComboBox.currentIndex())
        format = self.formatManager.getFormatInstanceForClass(selectedFormat)
        self.displayBboxOnMap(layer, crs, bboxString, format)

    def createTemporaryLayer(self):
        # TODO: Create temporary layer
        print('TODO: create temporary layer')

    def show(self):
        self.formatManager.getAllFormats()
        proj = qgis.core.QgsProject.instance()
        self.projectionSelectionWidget.setCrs(proj.crs())
        QDialog.show(self)

    def displayBboxOnMap(self, dstLayer, crs, bboxString, formatInstance):
        bboxGeom = formatInstance.format(bboxString)
        print(bboxGeom)

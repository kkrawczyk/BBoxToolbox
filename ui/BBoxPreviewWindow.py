import os

import qgis
import qgis.core
from qgis.PyQt import uic
from qgis.PyQt.QtCore import *

from .. import biz

B_BOX_TOOLBOX = "BBoxToolbox"

try:
    from qgis.PyQt.QtGui import QDialog, QMessageBox
except ImportError:
    from qgis.PyQt.QtWidgets import QDialog, QMessageBox


class BBoxPreviewWindow(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        ui_path = os.path.join(os.path.dirname(__file__), 'BBoxPreviewWindow.ui')
        uic.loadUi(ui_path, self)
        self.canvas = iface.mapCanvas()
        self.destinationLayer.setCurrentIndex(0)
        self.destinationLayer.setFilters(qgis.core.QgsMapLayerProxyModel.PolygonLayer)
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

    def createTemporaryLayer(self, crs):
        typeString = "%s?crs=%s" % ('Polygon', crs.authid())
        layerTitle = QCoreApplication.translate(B_BOX_TOOLBOX, "BBoxToolbox visualization")
        layer = qgis.core.QgsVectorLayer(typeString, layerTitle, "memory")
        layer.dataProvider().addAttributes([qgis.core.QgsField("name", QVariant.String)])
        qgis.core.QgsProject.instance().addMapLayer(layer)
        return layer

    def createFeature(self, geom):
        f = qgis.core.QgsFeature()
        f.setGeometry(geom)
        return f

    def show(self):
        self.formatManager.getAllFormats()
        proj = qgis.core.QgsProject.instance()
        self.projectionSelectionWidget.setCrs(proj.crs())
        QDialog.show(self)

    def displayBboxOnMap(self, dstLayer, crs, bboxString, formatInstance):
        bboxGeom = formatInstance.format(bboxString)
        if dstLayer is None:
            dstLayer = self.createTemporaryLayer(crs)
        if dstLayer.readOnly():
            errorMessage = QCoreApplication.translate(B_BOX_TOOLBOX, "Selected layer is readonly")
            QMessageBox.Critical(self.iface.mainWindow(), B_BOX_TOOLBOX, errorMessage)
            return
        f = self.createFeature(bboxGeom)
        dstLayer.dataProvider().addFeature(f)
        dstLayer.updateExtents()
        dstLayer.reload()
        self.canvas.refreshAllLayers()

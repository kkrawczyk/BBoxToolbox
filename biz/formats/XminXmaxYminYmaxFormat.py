import re
from decimal import Decimal

from qgis.core import QgsGeometry, QgsPointXY

from .AbstractBBoxFormat import AbstractBBoxFormat


class XminXmaxYminYmaxFormat(AbstractBBoxFormat):

    def __init__(self):
        self.pattern = r'\[([\d]+(\.\d+)?), ?([\d]+(\.\d+)?), ?([\d]+(\.\d+)?), ?([\d]+(\.\d+)?)\]'
        self.compiledPattern = re.compile(self.pattern)

    def displayName(self):
        return "[Xmin, Xmax, Ymin, Ymax]"

    def format(self, bboxString):
        print(bboxString)
        m = self.compiledPattern.match(bboxString)
        if m is not None:
            xmin = Decimal(m.group(1))
            xmax = Decimal(m.group(3))
            ymin = Decimal(m.group(5))
            ymax = Decimal(m.group(7))
            p1 = QgsPointXY(xmin, ymin)
            p2 = QgsPointXY(xmax, ymin)
            p3 = QgsPointXY(xmax, ymax)
            p4 = QgsPointXY(xmin, ymax)
            p5 = QgsPointXY(xmin, ymin)
            coords = [p1, p2, p3, p4, p5]
            geom = QgsGeometry.fromPolygonXY([coords])
            return geom
        return None

from .AbstractBBoxFormat import AbstractBBoxFormat


class XminXmaxYminYmaxFormat(AbstractBBoxFormat):
    def displayName(self):
        return "[Xmin, Xmax, Ymin, Ymax]"

    def format(self, bboxString):
        print(bboxString)

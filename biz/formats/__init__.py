from .AbstractBBoxFormat import AbstractBBoxFormat
from .XminXmaxYminYmaxFormat import XminXmaxYminYmaxFormat


class FormatManager(object):
    def __init__(self):
        self.formatClasses = {}
        self.initFormats()
        # self.formatClasses.

    def initFormats(self):
        instance = XminXmaxYminYmaxFormat()
        self.formatClasses[instance.__class__.__name__] = instance

    def getAllFormats(self):
        return self.formatClasses

    def getFormatInstanceForClass(self, classname):
        for cname in self.formatClasses:
            if cname == classname:
                return self.formatClasses[cname]
        return None

# -*- coding: utf-8 -*-
import os


def classFactory(iface):
    if 'DEBUG_PLUGIN' in os.environ and os.environ['DEBUG_PLUGIN'] == "BBoxToolkit":
        from .debuger import InitDebug
        InitDebug()
    from .BBoxToolkit import BBoxToolkit
    return BBoxToolkit(iface)

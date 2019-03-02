import os


######################### REMOTE DEBUG #########################

def checkDebuggerPresence():
    try:
        import pydevd
        return True
    except:
        return False


def InitDebug():
    if 'DEBUG_PLUGIN' in os.environ and os.environ['DEBUG_PLUGIN'] == "BBoxToolkit":
        if checkDebuggerPresence():
            import pydevd
            pydevd.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True, suspend=False)
######################### /REMOTE DEBUG #########################

from os.path import realpath, expanduser, join as path_join
import sys

def guess_inkscape_config_path():
    if getattr(sys, 'frozen', None):
        path = realpath(path_join(sys._MEIPASS, "..", "..", ".."))
        if sys.platform == "win32":
            import win32api

            # This expands ugly things like EXTENS~1
            path = win32api.GetLongPathName(path)
    else:
        path = expanduser("~/.config/inkscape")

    return path

import os, sys

base_dir = '.'

def checkPath(base_dir):
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS)
    return base_dir
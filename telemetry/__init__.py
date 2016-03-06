from .const import *
from .tele import *
import curses

title="Telemetry"

def launch(scr):
	scr.clear()
	return tele(scr)

from .const import *
from .trip import *
import curses

title="Current trip"

def launch(scr):
	scr.clear()
	return trip(scr)

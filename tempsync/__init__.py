from .const import *
from .sync import *
import curses

title="Temp sync"

def launch(scr):
	scr.clear()
	scr.addstr(0, int((COLS - len(title)) / 2), title)
	scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	scr.refresh()
	return sync(scr)

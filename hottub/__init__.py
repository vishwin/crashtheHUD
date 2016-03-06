from .const import *
from .toggle import *
import curses

title="Hot tub"

def launch(scr):
	scr.clear()
	scr.addstr(0, int((COLS - len(title)) / 2), title)
	scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	scr.refresh()
	return toggle(scr)

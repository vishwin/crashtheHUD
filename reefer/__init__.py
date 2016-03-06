from .const import *
from .display import *
import curses

title="Server/reefer"

def launch(scr):
	scr.clear()
	scr.addstr(0, int((COLS - len(title)) / 2), title)
	scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	scr.refresh()
	return display(scr)

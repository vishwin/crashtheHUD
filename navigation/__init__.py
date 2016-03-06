from .const import *
import curses

title="Navigation"
menu_display_max=ROWS - 2

def launch(scr):
	return wait(scr)

def wait(scr):
	keypress=None
	scr.clear()
	scr.addstr(0, int((COLS - len(title)) / 2), title)
	scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	scr.refresh()
	keypress=scr.getch()

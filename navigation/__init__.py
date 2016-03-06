from .const import *
import curses

title="Navigation"
menu_display_max=ROWS - 2

def launch(scr):
	return wait(scr)

def wait(scr):
	keypress=None
	wait_message=("Set driving", "directions on", "mobile phone")
	scr.clear()
	scr.addstr(0, int((COLS - len(title)) / 2), title)
	scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	for i in range(2, 2 + len(wait_message)):
		scr.addstr(i, int((COLS - len(wait_message[i - 2])) / 2), wait_message[i - 2])
	scr.refresh()
	keypress=scr.getch()

from .const import *
import curses

def toggle(scr):
	keypress=None
	status=False
	while keypress!=260:
		status_str="Status: Off"
		toggle_str="Cancel/Toggle"
		if status==True:
			status_str="Status: On"
		scr.addstr(2, int((COLS - len(status_str)) / 2), status_str)
		scr.addstr(3, int((COLS - len(toggle_str)) / 2), toggle_str)
		scr.addch(3, COLS - 2, '>')
		scr.addch(3, 0, '<')
		scr.refresh()
		keypress=scr.getch()
		if keypress==261:
			status=not status
			scr.addstr(2, 0, " " * COLS)

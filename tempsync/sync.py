from .const import *
import curses

def confirm(scr):
	msg_str="Setting updated"
	scr.clear()
	scr.border()
	scr.addstr(2, int((COLS - len(msg_str)) / 2), msg_str)
	scr.refresh()
	curses.napms(2000)

def sync(scr):
	keypress=None
	status=False
	while keypress!=260:
		car_temp_str="Car temp: 24 C"
		home_temp_str="Home temp: 14 C"
		status_str="Status: Not synced"
		menu_str="Cancel/Toggle"
		if status==True:
			status_str="Status: Synced"
		scr.addstr(2, int((COLS - len(car_temp_str)) / 2), car_temp_str)
		scr.addstr(3, int((COLS - len(home_temp_str)) / 2), home_temp_str)
		scr.addstr(4, int((COLS - len(status_str)) / 2), status_str)
		scr.addstr(5, int((COLS - len(menu_str)) / 2), menu_str)
		scr.addch(5, 0, '<')
		scr.addch(5, COLS - 2, '>')
		scr.refresh()
		keypress=scr.getch()
		if keypress==261:
			status=not status
			return confirm(scr)

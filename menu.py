COLS=20
ROWS=6

HUD_name="Crash the HUD"

import curses

def main(scr):
	menu_items=("Telemetry", "Navigation", "Temp sync", "Hot tub", "Server move")
	menu_display_max=4
	menu_pos=0
	keypress=None
	
	while True:
		scr.clear()
		scr.addstr(0, int((COLS - len(HUD_name)) / 2), HUD_name)
		scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
		for i in range(2, 6):
			menu_i=i - 2 + (menu_display_max - 4)
			scr.addstr(i, 2, " " * int((COLS - 5 - len(menu_items[menu_i])) / 2) + menu_items[menu_i])
			if menu_pos==menu_i:
				scr.addch(i, COLS-2, '>')
		scr.refresh()
		keypress=scr.getch()
		if keypress==258:
			menu_pos+=1
			if menu_pos>=len(menu_items):
				menu_pos=0
		elif keypress==259:
			menu_pos-=1
			if menu_pos<0:
				menu_pos=len(menu_items) - 1
		if menu_pos==menu_display_max:
			menu_display_max+=1
		if menu_pos<menu_display_max - 4:
			menu_display_max-=1

try:
	scr=curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	scr.keypad(True)
	
	main(scr)
	
	curses.nocbreak()
	scr.keypad(False)
	curses.echo()
	curses.endwin()
except:
	curses.nocbreak()
	scr.keypad(False)
	curses.echo()
	curses.endwin()

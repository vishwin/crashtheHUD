COLS=20
ROWS=6

HUD_name="Crash the HUD"

import curses

def main(scr):
	menu_items=("Telemetry", "Navigation", "Temperature sync", "Hot tub")
	menu_display_max=4
	keypress=None
	
	while keypress!=curses.KEY_EXIT:
		scr.clear()
		scr.addstr(0, int((COLS - len(HUD_name)) / 2), HUD_name)
		scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
		for i in range(2, 6):
			menu_i=i - 2 + (menu_display_max - 4)
			scr.addstr(i, 2, " " * int((COLS - 4 - len(menu_items[menu_i])) / 2) + menu_items[menu_i])
		scr.refresh()
		keypress=scr.getkey()

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

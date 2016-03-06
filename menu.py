COLS=20
ROWS=6

HUD_name="Crash the HUD"

import curses

def main(scr):
	scr.clear()
	scr.addstr(0, int((COLS-len(HUD_name)) / 2), HUD_name)
	scr.hline(1, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	scr.refresh()
	scr.getkey()

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

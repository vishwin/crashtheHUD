from .const import *
import curses
import serial
import time

def trip(scr):
	speed_str="Speed"
	speed_num="30"
	speed_mph="mph"
	dist_num="505"
	dist_mi="miles"
	scr.hline(3, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	scr.vline(0, 10, curses.ACS_VLINE, 3)
	scr.addstr(0, int((10 - len(speed_str)) / 2), speed_str)
	scr.addstr(1, int((10 - len(speed_num)) / 2), speed_num)
	scr.addstr(2, int((10 - len(speed_mph)) / 2), speed_mph)
	scr.addstr(4, int((COLS - len(dist_num)) / 2), dist_num)
	scr.addstr(5, int((COLS - len(dist_mi)) / 2), dist_mi)
	scr.refresh()
	scr.getch()

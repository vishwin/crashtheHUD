from .const import *
import curses
import serial

ser=serial.Serial('/dev/ttyACM0', 115200)

def tele(scr):
	scr.hline(3, 0, curses.ACS_HLINE, scr.getmaxyx()[1])
	speed_str="Speed"
	speed_mph="mph"
	scr.addstr(0, int((COLS - len(speed_str)) / 2), speed_str)
	scr.addstr(2, int((COLS - len(speed_mph)) / 2), speed_mph)
	scr.refresh()
	while True:
		speed=int(float(str(ser.readline()).rstrip()) * 1.151)
		speed_num=str(speed)
#		location="Brighton, NY, USA"
		scr.addstr(1, int((COLS - len(speed_num)) / 2), speed_num)
#		scr.addstr(4, 0, location)
		scr.refresh()
		if scr.getch():
			return

from .const import *
import curses

def display(scr):
	reefer_temp="Reefer: 5 C"
	reefer_fuel="Reefer fuel: 35%"
	avg_server_temp="Server temps: 12 C"
	servers_online="Online: 100/100"
	scr.addstr(2, int((COLS - len(reefer_temp)) / 2), reefer_temp)
	scr.addstr(3, int((COLS - len(reefer_fuel)) / 2), reefer_fuel)
	scr.addstr(4, int((COLS - len(avg_server_temp)) / 2), avg_server_temp)
	scr.addstr(5, int((COLS - len(servers_online)) / 2), servers_online)
	scr.refresh()
	scr.getch()

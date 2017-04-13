import wnck
import gtk 
import subprocess 
import time

class minimizarVentanas():

	def minimizar(self):
		screen = wnck.screen_get_default()

		while gtk.events_pending():
		    gtk.main_iteration()

		windows = screen.get_windows()
		active = screen.get_active_window()

		for w in windows:
		    if  w == active:
		        w.minimize()



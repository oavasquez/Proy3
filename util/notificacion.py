import pynotify
import gtk
import os
from time import  sleep


class notificacion():

    def notificaciones(self,title, msg, icon=None):
        """Send notification icon messages through libnotify.

        Parameters:

        (str) title -- The notification title
        (str) msg -- The message to display into notification
        (str / uri) icon -- Type of icon (ok|info|error|warm|ask|sync) or icon file

        """
        if not pynotify.is_initted():
            pynotify.init(title)
       
        note = pynotify.Notification(title, msg, icon)
        

        note.show()




        
    def mirando(self,juego):
        self.notificaciones("Inpeccionando", "Identificando juego: "+str(juego),os.getcwd()+"/util/image/eye1.png")

    def no_mirando(self):
        self.notificaciones("No se identifica", "No se observa ningun juego: ",os.getcwd()+"/util/image/eye2.png")

    def juego_terminado(self):
         self.notificaciones("Juego Terminado", " Partida perdida", os.getcwd()+"/util/image/gameOver.png")

    def jugando(self):
         self.notificaciones("Jugando", " Se esta jugando la partida", os.getcwd()+"/util/image/gameOver.png")



   
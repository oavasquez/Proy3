import sys
import time
import threading
from time import sleep
import math

class BarraProgreso(threading.Thread):
    def __init__(self, cantidad_de_archivos, indice):
        super(barraProgreso, self).__init__()
        self._stop = threading.Event()
        self.cantidad_de_archivos = cantidad_de_archivos
        self.indice = indice
        self.parar = False
        self.bloque = u"\u2588"


    def set_indice(self, indice):
        self.indice = indice

    def parar(self):
        self.parar = True

    def run(self):
            parar=False
            sys.stdout.flush()
            try:
                while self.indice < (self.cantidad_de_archivos-1) and not(self.parar):
                    self.indice=int((self.indice*100)/self.cantidad_de_archivos)
                    sys.stdout.write('\r')
                    sys.stdout.write("[%-25s]  %d%%" % (self.bloque*int(self.indice*0.25), self.indice+1))
                    sys.stdout.flush()
                    sleep(0.5)
            except Exception,e:
                self.parar=True
                print "parar"

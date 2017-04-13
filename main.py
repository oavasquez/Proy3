from util.CapturarPantalla import CapturarPantalla
from util.Leer import Leer




ci=CapturarPantalla()
ruta=ci.capturarFullSize()

Leer=Leer(ruta)
Leer.identificarJuego()
Leer.arregloImage()

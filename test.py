from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

raton1 = Raton('USB', 'Hp')
teclado1 = Teclado('Bluethoot', 'Genius')
monitor1 = Monitor('Samnsung', '25"')
computadora1 = Computadora('Lenovo', raton1, teclado1, monitor1)

raton2 = Raton('USB Tipo C', 'Logitech')
teclado2 = Teclado('USB', 'HP')
monitor2 = Monitor('Xiaomi', '30"')
computadora2 = Computadora('Acer', raton2, teclado2, monitor2)

raton3 = Raton('Bluethoot', 'Genius')
teclado3 = Teclado('USB/Bluethoot', 'Anne Pro 2')
monitor3 = Monitor('LG', '28"')
computadora3 = Computadora('Asus', raton2, teclado2, monitor2)


computadoras = [computadora1, computadora2]
orden1 = Orden(computadoras)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)
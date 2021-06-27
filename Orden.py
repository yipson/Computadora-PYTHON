from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora

class Orden:
    contador_ordenes = 0
    
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)
    
    
    @property
    def id_orden(self):
        return self._id_orden
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden
    
    
    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)
         
    def __str__(self):
        computadoras_str = '  '
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__() + '\n  '

        return f'Orden # {self._id_orden}, Computadoras: \n{computadoras_str}'

if __name__ == '__main__':
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
    
    # # orden1.agregar_computadora(computadora2)
    
    
    
    
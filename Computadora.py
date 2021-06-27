from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor

class Computadora:
    contador_computadoras = 0
    
    def __init__(self, nombre_computadora, raton, teclado, monitor):
        
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre_computadora
        self._raton = raton
        self._teclado = teclado
        self._monitor = monitor
        
    
    @property
    def id_computadora(self):
        return self._id_computadora
    @id_computadora.setter
    def id_computadora(self, id_computadora):
        self._id_computadora = id_computadora
        
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
        
    def __str__(self):
        return f'{self._nombre} [ ID: {self._id_computadora}, Marca: {self._nombre} \n    {self._raton} \n    {self._teclado} \n    {self._monitor} ]'
   
        
if __name__ == '__main__':
    # pass
    raton1 = Raton('USB', 'Hp')
    teclado1 = Teclado('Bluethoot', 'Genius')
    monitor1 = Monitor('Samnsung', '25"')
    computadora = Computadora('Lenovo', raton1, teclado1, monitor1)
    print (computadora)
    
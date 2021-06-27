class Monitor:
    contador_monitores = 0
    
    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamano
    
    
    @property
    def id_monitor(self):
        return self.id_monitor
    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self._id_monitor = id_monitor
        
        
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
    
    @property
    def tamano(self):
        return self._tamano
    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano
           
        
    def __str__(self):
        return f'Monitor [ ID: {self._id_monitor}, Marca: {self._marca}, Tamano: {self._tamano} ]'


if __name__ == '__main__':
    pass
    # monitor1 = Monitor('samsung', '28"')
    # print(monitor1)
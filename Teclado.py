from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipo_entrada, marca)
        
    def __str__(self):
        return f'Teclado [ ID: {self._id_teclado}, {super().__str__()} ]'
    
if __name__ == '__main__':
    pass
    # teclado1 = Teclado('bluethoot', 'samsung')
    # print(teclado1)
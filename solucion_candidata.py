class Candidato:
    vector_binario = None
    fitness = None
    
    def __init__(self, vector_binario):
        self.vector_binario = vector_binario
        pass
    
    def set_fitness(self, vector_movimientos, factura):
        movimientos_solucion = []
        for i in range(0, len(vector_movimientos)):
            if(self.vector_binario[i] == 1):
                movimientos_solucion.append(vector_movimientos[i])
                pass
            pass
        movimientos_solucion.sort(key=lambda mov: mov.monto, reverse=True)
        
        suma_montos = sum(movimiento.monto for movimiento in movimientos_solucion)
        
        diferencia = abs(factura.monto - suma_montos)
        
        self.fitness = 1 / diferencia
        
        pass
        
        
        
    
        
        
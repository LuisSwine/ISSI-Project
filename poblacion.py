import random

import solucion_candidata

class Poblacion: 
    tam_poblacion = None
    factura = None
    
    vector_movimientos = []
    vector_soluciones = []
    
    mejor_solucion = None
    mejor_fitness = 0
    
    def __init__(self, tam_poblacion, factura, vector_movimientos):
        self.tam_poblacion = tam_poblacion
        self.factura = factura
        self.vector_movimientos = vector_movimientos
        pass
    
    def inicializar_poblacion(self):
        for i in range (0, self.tam_poblacion):
            solucion = [random.randint(0,1) for j in range(len(self.vector_movimientos))]
            solucion = solucion_candidata.Candidato(solucion)
            solucion.set_fitness(self.vector_movimientos, self.factura)
            self.vector_soluciones.append(solucion)
        pass
    
    def mejor_solution(self):
        for solucion in self.vector_soluciones:
            solucion.set_fitness(self.vector_movimientos, self.factura)
            
        self.vector_soluciones.sort(key=lambda solucion: solucion.fitness, reverse=True)
        
        self.mejor_solucion = self.vector_soluciones[0]
        self.mejor_fitness = self.mejor_solucion.fitness
        
        print(self.mejor_solucion.vector_binario)
        print(self.mejor_fitness)
        
        pass
    pass

    
    

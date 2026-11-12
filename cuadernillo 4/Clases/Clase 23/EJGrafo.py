class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self,vertices):
        for vertice in vertices:
            if vertice not in self.adyacencia:
                self.adyacencia[vertice]=[]    

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
            self.adyacencia[destino].append(origen)

            if origen not in self.adyacencia[destino]:
                self.adyacencia[destino].append(origen)

    def obtener_vecinos(self, vertice):
        return self.adyacencia.get(vertice, [])

    def mostrar(self):
        for vertice, vecinos in self.adyacencia.items():
            print(F"Vertice{vertice} conectado con ={vecinos}")

red = Grafo()

red.agregar_arista("A", "B")
red.agregar_arista("A", "C")
red.agregar_arista("B", "C")
red.agregar_arista("B", "D")
red.agregar_arista("C", "D")
red.mostrar()
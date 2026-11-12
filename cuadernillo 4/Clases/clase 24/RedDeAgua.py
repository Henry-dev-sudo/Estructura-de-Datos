#Red de distribucion de agua

class BuscarUnion:
    def __init__(self, nodos):
        self.padre = {nodo: nodo for nodo in nodos}
    def encontrar(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.encontrar(self.padre[nodo])
        return self.padre[nodo]
    
    def unir(self, nodo1, nodo2):
        raiz1= self.encontrar(nodo1)
        raiz2 = self.encontrar(nodo2)
        if raiz1 != raiz2:
            self.padre[raiz2] = raiz1
            return True
        return False

def kruskal_mst(nodos, conexiones):
    mst = []
    total_costo = 0 
    uf = BuscarUnion(nodos)
    conexiones.sort()
    for costo, nodo1, nodo2 in conexiones:
        if uf.unir(nodo1, nodo2):
            mst.append((nodo1, nodo2, costo))
            total_costo += costo
    return mst, total_costo

nodos = ["A", "B", "C", "D", "E"]
conexiones = [
    (4, "A", "B"),
    (3, "A", "C"),
    (2, "B", "C"),
    (5, "B", "D"),
    (7, "C", "D"),
    (8, "C", "E"),
    (6, "D", "E")
]

mst_resultado, costo_total= kruskal_mst(nodos, conexiones)

print ("Tuberias selecionadas para la red: ")
for nodo1, nodo2, costo in mst_resultado:
    print(f"{nodo1} a {nodo2} / cost de: ${costo} K")

print (f"\n Costo total minimo de la red: ${costo_total} K")
import heapq

grafo = {
    "Portal Norte": [("Calle 100", 5), ("Suba", 10)],
    "Calle 100": [("Portal Norte", 5), ("Centro", 3)],
    "Suba": [("Portal Norte", 10), ("Centro", 1)],
    "Centro": [("Calle 100", 3), ("Suba", 1), ("Sur", 2)],
    "Sur": [("Centro", 2)]
}

def dijkstra(grafo, inicio, fin):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        (costo, nodo, camino) = heapq.heappop(cola)

        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == fin:
            return costo, camino

        for vecino, peso in grafo.get(nodo, []):
            heapq.heappush(cola, (costo + peso, vecino, camino))

    return float("inf"), []

def reglas(hora):
    if 6 <= hora <= 9:
        print("Hora pico: evitar rutas largas")
    else:
        print("Horario normal")

inicio = "Suba"
fin = "Sur"
hora = 11 

reglas(hora)
costo, ruta = dijkstra(grafo, inicio, fin)

print("Ruta optima:", " -> ".join(ruta))
print("Costo total:", costo)
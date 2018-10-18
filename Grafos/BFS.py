import queue


def breadth_first_search(inicio, grafo):
    """Implementacion de BFS usando cola"""
    descubiertos = {v: v == inicio for v in grafo}
    a_visitar = queue.Queue()

    while not a_visitar.empty():
        actual = a_visitar.get()
        for adyacente in actual.obtener_adyacentes():  # O como se llame el metodo
            if not descubiertos[adyacente]:
                descubiertos[adyacente] = True
                a_visitar.put(adyacente)

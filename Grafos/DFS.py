def depth_first_search(inicio, grafo):
    """Implementacion de DFS usando listas de python como pilas"""
    a_visitar = [inicio]
    explorados = {v: False for v in grafo}

    while a_visitar:
        actual = a_visitar.pop()
        if not explorados[actual]:
            explorados[actual] = True
            for adyacente in actual.obtener_adyacentes():
                a_visitar.append(adyacente)

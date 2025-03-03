# pip3 install networkx matplotlib

# BFS - Largura primeiro explora todos os nós filhos em primeiro lugar
# DFS - Profundidade primeiro explora todos os nós até n haver mais e volta para traz

import queue
import time
import networkx as nx
import matplotlib.pyplot as plt

# Largura em primeiro lugar

def order_bfs(graph, start_node):
    visited = set()                                               # Keep track of visited nodes
    q = queue.Queue()                                             # First in First Out Queue
    q.put(start_node)                                             # nó inicial
    order = []                                                    # nós na ordem bfs correcta

    while not q.empty():                                          # enquanto a queue não estiver vazia
        vertex = q.get()                                          # vamos buscar um nó para processamento
        if vertex not in visited:                                 # primeira vez que visitamos este nó
            order.append(vertex)                                  # colocamos este nó na ordem
            visited.add(vertex)                                   # passa a ser um nó visitado
            for node in graph[vertex]:                            # todos os vizinhos deste nó
                if node not in visited:                           # se não tivermos visto este estado
                    q.put(node)                                   # metemos na queue para processamento

    return order


# profundidade em primeiro lugar

def order_dfs(graph, start_node, visited = None):
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))

    return order

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, node_color=['r' if n == node else 'g' for n in G.nodes ])
        plt.draw()
        plt.pause(1.5)
    plt.show()
    time.sleep(0.5)

def generate_connected_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G

# Gerar os nós conectados a mao
# G = nx.Graph()
# G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])

G = generate_connected_random_graph(20, 30)
pos = nx.spring_layout(G)

# visualize_search(order_bfs(G, 'A'), 'Breadth First Search', G, pos )
visualize_search(order_dfs(G, 0), 'Depth First Search', G, pos )
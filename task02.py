import networkx as nx


# Створення графа
G = nx.Graph()
nodes = ["Центр", "Вокзал", "Оболонь", "Печерськ", "Либідська", "Теремки"]
G.add_nodes_from(nodes)

edges = [
    ("Центр", "Вокзал"),
    ("Центр", "Печерськ"),
    ("Вокзал", "Либідська"),
    ("Оболонь", "Центр"),
    ("Печерськ", "Теремки"),
    ("Либідська", "Теремки"),
    ("Оболонь", "Либідська"),
]

G.add_edges_from(edges)


# Алгоритм пошуку в глибину (DFS)
def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]  # Список пар (вузол, шлях)

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path
            for neighbor in graph.neighbors(vertex):
                stack.append((neighbor, path + [neighbor]))
    return None


# Алгоритм пошуку в ширину (BFS)
def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]  # Список пар (вузол, шлях)

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path
            for neighbor in graph.neighbors(vertex):
                queue.append((neighbor, path + [neighbor]))
    return None


# Приклад використання
start_node = "Центр"
goal_node = "Теремки"

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

# Виведення результатів
print(f"Шлях (DFS) з {start_node} до {goal_node}: {dfs_path}")
print(f"Шлях (BFS) з {start_node} до {goal_node}: {bfs_path}")

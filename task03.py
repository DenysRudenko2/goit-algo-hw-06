import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа з вагами
G = nx.Graph()
nodes = ["Центр", "Вокзал", "Оболонь", "Печерськ", "Либідська", "Теремки"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами
edges_with_weights = [
    ("Центр", "Вокзал", 5),
    ("Центр", "Печерськ", 2),
    ("Вокзал", "Либідська", 3),
    ("Оболонь", "Центр", 4),
    ("Печерськ", "Теремки", 7),
    ("Либідська", "Теремки", 1),
    ("Оболонь", "Либідська", 6),
]

G.add_weighted_edges_from(edges_with_weights)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиції вузлів для візуалізації
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')

# Додавання ваг до ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start, goal):
    # Ініціалізація
    shortest_paths = {node: (float('inf'), []) for node in graph.nodes()}
    shortest_paths[start] = (0, [start])
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        # Якщо досягнута цільова вершина, повертаємо шлях і його довжину
        if current_node == goal:
            return shortest_paths[current_node][1], current_distance

        # Оновлення шляхів для сусідніх вершин
        for neighbor, data in graph[current_node].items():
            weight = data['weight']
            distance = current_distance + weight

            # Якщо знайдений коротший шлях до сусідньої вершини
            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_node][1] + [neighbor])
                heapq.heappush(priority_queue, (distance, neighbor))

    # Якщо шлях не знайдено
    return None, float('inf')

# Приклад використання
start_node = "Центр"
goal_node = "Теремки"

shortest_path, path_length = dijkstra(G, start_node, goal_node)

# Виведення результатів
print(f"Найкоротший шлях з {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {path_length}")

# Знаходження найкоротших шляхів між усіма парами вершин
def all_pairs_dijkstra(graph):
    all_shortest_paths = {}
    for start in graph.nodes():
        all_shortest_paths[start] = {}
        for goal in graph.nodes():
            if start == goal:
                continue
            path, length = dijkstra(graph, start, goal)
            all_shortest_paths[start][goal] = (length, path)
    return all_shortest_paths

# Виведення результатів для всіх пар
shortest_paths = all_pairs_dijkstra(G)
print("Найкоротші шляхи між усіма парами вершин:")

for start_node, destinations in shortest_paths.items():
    for end_node, (length, path) in destinations.items():
        print(f"Найкоротший шлях з {start_node} до {end_node}: {path} (довжина: {length})")

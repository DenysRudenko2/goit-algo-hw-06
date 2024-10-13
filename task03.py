import networkx as nx
import matplotlib.pyplot as plt

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

# Алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start, goal):
    return nx.dijkstra_path(graph, start, goal), nx.dijkstra_path_length(graph, start, goal)

# Приклад використання
start_node = "Центр"
goal_node = "Теремки"

shortest_path, path_length = dijkstra(G, start_node, goal_node)

# Виведення результатів
print(f"Найкоротший шлях з {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {path_length}")

# Знаходження найкоротших шляхів між усіма парами вершин
shortest_paths = dict(nx.all_pairs_dijkstra(G))

# Виведення результатів
print("Найкоротші шляхи між усіма парами вершин:")

for start_node, (length_dict, path_dict) in shortest_paths.items():
    for end_node in path_dict.keys():
        if start_node == end_node:
            continue
        length = length_dict[end_node]
        path = path_dict[end_node]
        print(f"Найкоротший шлях з {start_node} до {end_node}: {path} (довжина: {length})")

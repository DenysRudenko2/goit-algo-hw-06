import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (зупинок/станцій)
nodes = ["Центр", "Вокзал", "Оболонь", "Печерськ", "Либідська", "Теремки"]
G.add_nodes_from(nodes)

# Додавання ребер (маршрутів)
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

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиції вузлів для візуалізації
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
plt.title("Транспортна мережа Києва")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()  # Кількість вершин
num_edges = G.number_of_edges()  # Кількість ребер
degrees = dict(G.degree())  # Ступені вершин

# Виведення результатів
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for node, degree in degrees.items():
    print(f"  {node}: {degree}")

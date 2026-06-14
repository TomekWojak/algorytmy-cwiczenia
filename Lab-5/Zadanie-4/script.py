import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

wierzcholki = ["S1", "S2", "S3", "S4", "S5", "S6"]
G.add_nodes_from(wierzcholki)

krawedzie = [
    ("S1", "S2"),
    ("S1", "S3"),
    ("S2", "S4"),
    ("S3", "S4"),
    ("S3", "S5"),
    ("S4", "S6"),
    ("S5", "S6"),
]
G.add_edges_from(krawedzie)

plt.figure(figsize=(8, 6))

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(
    G, pos, node_size=700, node_color="skyblue", edgecolors="black"
)
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")

nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

plt.title("Wizualizacja Grafu Nieskierowanego (Sieć LAN)", fontsize=14)

plt.axis("off")


plt.tight_layout()
plt.show()
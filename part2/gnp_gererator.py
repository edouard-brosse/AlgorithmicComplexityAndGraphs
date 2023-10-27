from networkx import gnp_random_graph
import networkx as nx
import matplotlib.pyplot as plt
from test_matching import *

def plot_graph(G: nx.Graph, graph_name: str, var: str) -> None:
    image_name = f"images/{graph_name}.pdf"
    plt.title(f"{graph_name}\n{var}")
    # visualize the graph
    # choose colors
    node_color="#b6cef2"
    edge_color="#1b50a1"
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos=nx.spring_layout(G, seed=1)
    # pos=nx.spring_layout(G)
    # if you prefer a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(G,
            pos,
            node_size=160,
            node_color=node_color,
            edge_color=edge_color,
            font_size=6,
            width=1,
            with_labels=True)
    plt.tight_layout()
    plt.savefig(image_name)
    plt.close()

n = 120
p = 0.04
g = gnp_random_graph(n, p)
plot_graph(g, f"original_graph", f"n = {n} p = {p*100}%")

# nx_match = nx.maximal_matching(g)
# print(f"networkx matching: size {len(nx_match)}, {nx_match}\n")

min = test_matching(g.copy(), (lambda x, y: x < y))
print(f"min degree matching: size {len(min)}, {min}\n")

max = test_matching(g.copy(), (lambda x, y: x > y))
print(f"max degree matching: size {len(max)}, {max}")

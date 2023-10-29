from networkx import gnp_random_graph
from time import time
from gnp_gererator import plot_graph
from test_matching import test_matching

n = 120
p = 0.04
g = gnp_random_graph(n, p)
plot_graph(g, f"original_graph", f"n = {n} p = {p*100}%")

# nx_match = nx.maximal_matching(g)
# print(f"networkx matching: size {len(nx_match)}, {nx_match}\n")
min_start = time()
min = test_matching(g.copy(), (lambda x, y: x < y))
min_end = time()
print(f"min degree matching: size {min.size()} {min.edges()}\ntook {min_end-min_start}\n")

max_start = time()
max = test_matching(g.copy(), (lambda x, y: x > y))
max_end = time()
print(f"max degree matching: size {max.size()} {max.edges()}\ntook {max_end-max_start}")

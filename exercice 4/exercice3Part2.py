import matplotlib.pyplot as plt
import networkx as nx
import random

#create random graph
def CreaGraph(num_nodes, edge_probability):
    return nx.erdos_renyi_graph(num_nodes, edge_probability, directed=False)

#find eulerian path
def EuleurianPaht(graph):
    if nx.is_eulerian(graph):
        return list(nx.eulerian_circuit(graph))
    else:
        return None

#find hamilton path
def HamiltonPath(line_graph):
    try:
        return list(nx.approximation.traveling_salesman_problem(line_graph, cycle=True))
    except nx.NetworkXError:
        return None

#display graph
def DisplayGraph(graph, paths, title, path_color):
    fig, ax = plt.subplots(figsize=(12, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, font_size=12, font_color='black', node_color='lightblue',
            edgelist=graph.edges(), arrows=False)
    
    if paths:
        for path in paths:
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color=path_color, width=2.0)

    ax.set_title(title)
    plt.show()

if __name__ == "__main__":
    num_nodes = 6
    edge_probability = 0.4

    # Create random graph
    G = CreaGraph(num_nodes, edge_probability)
    line_graph = nx.line_graph(G)

    # Find Eulerian & Hamiltonian paths
    eulerian_path = EuleurianPaht(G)
    hamiltonian_path = HamiltonPath(line_graph)

    # Display  graph 
    DisplayGraph(G, [eulerian_path] if eulerian_path else [], "Eulerian Path", 'red')
    DisplayGraph(line_graph, [hamiltonian_path] if hamiltonian_path else [], "Hamiltonian Path", 'blue')


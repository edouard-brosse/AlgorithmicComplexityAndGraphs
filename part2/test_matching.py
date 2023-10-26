import networkx as nx

def test_matching_min(g):
    nodeMin = None
    nodeMin2 = None
    degMin = None
    deg = None
    match = []
    while not nx.is_empty(g):
        for node in g.nodes():
            deg = g.degree(node)
            if degMin is None or (deg > 0 and degMin > deg):
                nodeMin, degMin = node, deg
        degMin = None
        for edge in g.edges(nodeMin):
            deg = g.degree(edge[1])
            if degMin is None or (deg > 0 and degMin > deg):
                nodeMin2, degMin = edge[1], deg
        degMin = None
        match.append((nodeMin, nodeMin2))
        g.remove_node(nodeMin)
        g.remove_node(nodeMin2)
    return match

def test_matching_max(g):
    nodeMax = None
    nodeMax2 = None
    degMax = None
    deg = None
    match = []
    while not nx.is_empty(g):
        for node in g.nodes():
            deg = g.degree(node)
            if degMax is None or (deg > 0 and degMax < deg):
                nodeMax, degMax = node, deg
        degMax = None
        for edge in g.edges(nodeMax):
            deg = g.degree(edge[1])
            if degMax is None or (deg > 0 and degMax < deg):
                nodeMax2, degMax = edge[1], deg
        degMax = None
        match.append((nodeMax, nodeMax2))
        g.remove_node(nodeMax)
        g.remove_node(nodeMax2)
    return match

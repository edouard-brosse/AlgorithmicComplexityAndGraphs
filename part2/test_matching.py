import networkx as nx
from types import FunctionType

def cmp_deg(g, cmp: FunctionType, nodes):
    deg = None
    Xdeg = None
    Xnode = None
    for node in nodes:
        deg = g.degree(node)
        if deg > 0 and (Xdeg is None or cmp(deg, Xdeg)):
            Xnode, Xdeg = node, deg
    return Xnode

def test_matching(g, cmp: FunctionType):
    Xnode = None
    Xnode2 = None
    match = set()
    while not nx.is_empty(g):
        Xnode = cmp_deg(g, cmp, g)
        Xnode2 = cmp_deg(g, cmp, g[Xnode])
        match.add((Xnode, Xnode2))
        g.remove_node(Xnode)
        g.remove_node(Xnode2)
    return match


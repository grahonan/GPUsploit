from path import Path

import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()

G.add_node("ROOT")

for i in xrange(5):
    G.add_node("Child_%i" % i)
    G.add_node("Grandchild_%i" % i)
    G.add_node("Greatgrandchild_%i" % i)

    G.add_edge("ROOT", "Child_%i" % i)
    G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
    G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

dfs = list(nx.dfs_edges(G, 'ROOT')) #get list of all traces with dfs
trace1 = dfs[0:3] #hardcoded
path1 = Path(trace1)
print("Path:" + str(path1.nodeList) + "\nOverflow:" + str(path1.overflow))

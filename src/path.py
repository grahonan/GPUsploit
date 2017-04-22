"""A path of custom nodes representing a program trace"""

import networkx as nx
import matplotlib.pyplot as plt

class Path():

    def __init__(self, edgeList):
        self.nodeList = self.getNodeList(edgeList);
        self.overflowFlag = False;

    def getNodeList(self, edgeList):
        return [node for node in edgeList]


def main():
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
    print("Path:" + str(path1.nodeList) + "\nOverflow:" + str(path1.overflowFlag))
        
if __name__ == "__main__":
    main()

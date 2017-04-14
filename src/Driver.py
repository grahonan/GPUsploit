from parser import Parser
import networkx as nx
import matplotlib.pyplot as plt

def getPaths(graph, root):
    dfs = nx.dfs_edges(graph, root)
    path = []
    paths = []
    for node in dfs:
        if node[0] in path:
            idx = path.index(node[0])
            paths.append(path)
            path = path[0:idx]
        else:
            path.append(node[0])
    paths.append(path)

    return paths

def main():
    parser = Parser("../assets/stack_overflow_1.json");
    paths = getPaths(parser.G, 'root')
    print(paths)
    #print(parser.data['root']['children']['taken']);
    #print('');
    #print(len(parser.data['root']))
    #print(len(parser.data))
    
    
    #nx.nx_pydot.write_dot(parser.G,'test.dot');
    #pos = nx.nx_pydot.graphviz_layout(parser.G, prog = 'dot');
    #nx.draw(parser.G, pos, with_labels = True, arrows = False);
    #plt.show();
                                            
if __name__ == "__main__":
    main()
        

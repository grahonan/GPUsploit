from parser import Parser
from path import Path

import networkx as nx
import matplotlib.pyplot as plt


def main():
    parser = Parser("../assets/stack_overflow_1.json");
    paths = [Path(path) for path in nx.all_simple_paths(parser.G, 'root', 'end')]
    print("Number of traces: " + str(len(paths)))
    print(parser.G.node[paths[0].nodeList[0]])
    #paths = [Path(path) for path in paths]
    
    #print(paths)
    #print(parser.data['root']['children']['taken']);
    #print('');
    #print(len(parser.data['root']))
    #print(len(parser.data))
    
    
    nx.nx_pydot.write_dot(parser.G,'test.dot');
    pos = nx.nx_pydot.graphviz_layout(parser.G, prog = 'dot');
    nx.draw(parser.G, pos, with_labels = True, arrows = False);
    plt.show();
                                            
if __name__ == "__main__":
    main()
        

from parser import Parser
from path import Path

import networkx as nx
import matplotlib.pyplot as plt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

	print(parser.G.node['node52']['buffer'].getAccessorList()[0].getVar());
	aL = {};
	vals = [];
	for i in paths:
		#reset dict for each new path
		aL = {};
		for j in i.nodeList:
			vals = []; #reset list for each new node
			if(parser.G.node[j]['accessor'] != ''):
				aL[parser.G.node[j]['accessor'].var] = parser.G.node[j]['accessor'].max;
			if(parser.G.node[j]['buffer'] != ''):
				for bufAcc in parser.G.node[j]['buffer'].getAccessorList():
					if(is_number(aL[bufAcc.var])): # add to vals list, to be passed into expression
						vals.append(aL[bufAcc.var]);
						#print(j);
						#print(aL[bufAcc.var])
					else: #must be INT, UINT, LONG, ULONG, etc
						i.overflowFlag = True;
						parser.G.node[j]['overflowFlag'] = True;
				if(parser.G.node[j]['overflowFlag'] == False):
					evaluation = parser.G.node[j]['buffer'].evalExpression(vals);
					#check if max is exceeded
					if(evaluation >= parser.G.node[j]['buffer'].size):
						i.overflowFlag = True;
						parser.G.node[j]['overflowFlag'] = True;
	for i in paths:
		if (i.overflowFlag == True):
			for j in i.nodeList:
				print(j);

	nx.nx_pydot.write_dot(parser.G,'test.dot');
	pos = nx.nx_pydot.graphviz_layout(parser.G, prog = 'dot');
	nx.draw(parser.G, pos, with_labels = True, arrows = False);
	plt.show();
                                            
if __name__ == "__main__":
    main()
        

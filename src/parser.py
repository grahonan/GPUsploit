import json
import networkx as nx
import matplotlib.pyplot as plt
import pydotplus

class Parser():

	def addNodes(self,currNode,parent):
		print("test");
		print(currNode);
		self.G.add_node(currNode);
		if(parent != ''):
			self.G.add_edge(parent,currNode);
		if(self.data[currNode]['children']['taken'] == '') and (self.data[currNode]['children']['nTaken'] == ''):
			return;
		parent = currNode;
		currNode = 'node'+self.data[currNode]['children']['taken'];
		self.addNodes(currNode,parent);
		if(self.data[currNode]['children']['nTaken'] != ''):
			parent = currNode;
			currNode = 'node'+self.data[currNode]['children']['nTaken'];
			self.addNodes(currNode,parent);
			
			
	def __init__(self, file):
		with open(file) as data_file: 
			self.data = json.load(data_file);
		self.G = nx.DiGraph();
		#self.G.add_node(self.data['root']['nodeName']['line#']);
		self.addNodes('root','');
		print(self.G.nodes());
		print(self.G.edges());
		
	
	
		
	
    
def main():
	parser = Parser("../assets/stack_overflow_1.json");
	print(parser.data['root']['children']['taken']);
	print('');
	print(len(parser.data['root']))
	print(len(parser.data))
	
	
	nx.nx_pydot.write_dot(parser.G,'test.dot');
	pos = nx.nx_pydot.graphviz_layout(parser.G, prog = 'dot');
	nx.draw(parser.G, pos, with_labels = True, arrows = False);
	plt.show();
	
if __name__ == "__main__":
    main()
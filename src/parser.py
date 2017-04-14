import json
import networkx as nx
import matplotlib.pyplot as plt
import pydotplus
from buf import Buf
from accessor import Accessor

class Parser():

	def addNodes(self,currNode,parent):
		#print("test");
		#print(currNode);
		aL = [];
		self.G.add_node(currNode,overFlowFlag = False, accessor = '', buffer = '');
		if(self.data[currNode]['accessors']['vars'] != ''):
			tempAcc = Accessor(self.data[currNode]['accessors']['vars'], self.data[currNode]['accessors']['maxValues']);
			self.G.add_node(currNode,accessor = tempAcc);
		if(self.data[currNode]['bufField']['accessors'] != ''):
			tempVars = self.data[currNode]['bufField']['accessors'].split(',');
			for i in range(len(tempVars)):
				aL.append(Accessor(tempVars[i],""));
			tempBuffer = Buf(aL,self.data[currNode]['bufField']['size'],self.data[currNode]['bufField']['expression'],self.data[currNode]['bufField']['type']);
			self.G.add_node(currNode,buffer = tempBuffer);
			
		
		if(parent != ''):
			self.G.add_edge(parent,currNode);
		if(self.data[currNode]['children']['taken'] == '') and (self.data[currNode]['children']['nTaken'] == ''):
			self.G.add_node('end');
			self.G.add_edge(currNode,'end');
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
		#print(self.G.nodes());
		#print(self.G.edges());
		
	
	
		
	
    
def main():
	parser = Parser("../assets/stack_overflow_1.json");
	print(parser.data['root']['children']['taken']);
	print('');
	print(len(parser.data['root']))
	print(len(parser.data))
	print(parser.G.node['node52']['buffer'].getAccessorList()[0].getVar());
	
	nx.nx_pydot.write_dot(parser.G,'test.dot');
	pos = nx.nx_pydot.graphviz_layout(parser.G, prog = 'dot');
	nx.draw(parser.G, pos, with_labels = True, arrows = True);
	plt.show();
	
if __name__ == "__main__":
    main()

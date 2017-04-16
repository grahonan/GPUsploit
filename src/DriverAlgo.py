from parser import Parser
from path import Path

import re
import networkx.drawing.nx_agraph as nx_agraph
import networkx as nx
import matplotlib.pyplot as plt
import sys
import getopt
import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main(argv):
	inputfile = '';
	cupath = '';
	cufile = '';
	
	try:
		inputfile = argv[0];
	except IndexError:
		print 'test.py <inputJson> <inputCU>';
		sys.exit(2);
	try:
		cupath = argv[1];
		cufile = os.path.basename(cupath);
		cufile = cufile[:cufile.index('.')];
		print(cufile);
	except IndexError:
		print 'test.py <inputJson> <inputCU>';
		sys.exit(2);
	
	try:		
		parser = Parser(inputfile); #"../assets/stack_overflow_1.json"
	except:
		print "File doesn't exist or is the wrong format!";
		sys.exit(2);
	paths = [Path(path) for path in nx.all_simple_paths(parser.G, 'root', 'end')]
	print("Number of traces: " + str(len(paths)))
	#print(parser.G.node[paths[0].nodeList[0]])
	#paths = [Path(path) for path in paths]

	#print(paths)
	#print(parser.data['root']['children']['taken']);
	#print('');
	#print(len(parser.data['root']))
	#print(len(parser.data))

	#print(parser.G.node['node52']['buffer'].getAccessorList()[0].getVar());
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
                                                #print ("overflow detected");


        renderGraph = nx_agraph.to_agraph(parser.G)
        count = 0
        f = open(cupath, 'r')
        if not os.path.exists(os.path.dirname('../out/'+cufile+'/')):
    		try:
        		os.makedirs(os.path.dirname('../out/'+cufile+'/'))
    		except OSError as exc: # Guard against race condition
        		if exc.errno != errno.EEXIST:
					raise
        
        fw = open('../out/'+cufile+'/log.txt', 'w')
        codeString = f.readlines()
        stacktrace = []
        line = []
        for i in paths:
		if (i.overflowFlag == True):
                    print("Overflow Trace " + str(count) + "\n")
                    fw.write("Overflow Trace " + str(count) + "\n")
                    tempGraph = renderGraph
                    for j in i.nodeList:
                        if(parser.G.node[j]['overflowFlag'] == True):
                            #print(lineNum)
                            lineNum = parser.G.node[j]['line']
                            if(lineNum != ''):
                                tmpLine = "At Line " + lineNum + ": Exception: Warning! Overflow Detected:" + re.sub(r"\s+"," ",codeString[int(lineNum) - 1])
                                print(tmpLine)
                                fw.write(tmpLine + "\n")
                            #re.sub(r"\s+","",codeString[int(lineNum) - 1]))
                            tempNode = tempGraph.get_node(j)
                            tempNode.attr['style'] = 'filled'
                            tempNode.attr['fillcolor'] = 'red'
                        else:
                            #print(lineNum)
                            tempNode = tempGraph.get_node(j)
                            lineNum = parser.G.node[j]['line']
                            if(lineNum != ''):
                                tmpLine = "At Line " + lineNum + ":" + re.sub(r"\s+"," ",codeString[int(lineNum) - 1])
                                print(tmpLine)
                                fw.write(tmpLine + "\n")
                            tempNode.attr['style'] = 'filled'
                            tempNode.attr['fillcolor'] = 'yellow'
                        #print(j);
                    tempGraph.layout(prog='dot')
                    tempGraph.draw('../out/'+cufile+'/trace' + str(count) + '.png')
                    count+= 1
                    fw.write("\n\n\n--------------------------------------------------------------------------\n\n\n")
                    print("\n\n\n--------------------------------------------------------------------------\n\n\n")
        #print (stacktrace)
        fw.close()

        #parser.G.node['node98']['color']='black'
	#nx.nx_pydot.write_dot(parser.G,'test.dot');
	#pos = nx.nx_pydot.graphviz_layout(parser.G, prog = 'dot');
	#nx.draw(parser.G, pos, with_labels = True, arrows = False);
	#plt.show();
                                            
if __name__ == "__main__":
    main(sys.argv[1:])
        

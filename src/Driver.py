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
		parser = Parser(inputfile);
	except:
		print "File doesn't exist or is the wrong format!";
		sys.exit(2);
	paths = [Path(path) for path in nx.all_simple_paths(parser.G, 'root', 'end')]
	print("Number of traces: " + str(len(paths)))
	
	graphs = [];
	paths2 = [];
	
	for i in range(len(paths)):
		graphs.append(Parser(inputfile));
	for i in graphs:
		paths2.append([Path(path) for path in nx.all_simple_paths(i.G, 'root', 'end')]);
	

	aL = {};
	vals = [];

	
	for graphIndex in range(len(paths)):
		aL = {};
		for j in paths2[graphIndex][graphIndex].nodeList:
			vals = [];
			if(graphs[graphIndex].G.node[j]['accessor'] != ''):
				aL[graphs[graphIndex].G.node[j]['accessor'].var] = graphs[graphIndex].G.node[j]['accessor'].max;
			if(graphs[graphIndex].G.node[j]['buffer'] != ''):
				for bufAcc in graphs[graphIndex].G.node[j]['buffer'].getAccessorList():

                                    if(is_number(aL[bufAcc.var])): # add to vals list, to be passed into expression
						
					vals.append(aL[bufAcc.var]);
	                            else: #must be INT, UINT, LONG, ULONG, etc
					paths2[graphIndex][graphIndex].overflowFlag = True;
					graphs[graphIndex].G.node[j]['overflowFlag'] = True;
						
				
				if(graphs[graphIndex].G.node[j]['overflowFlag'] == False):
				    evaluation = graphs[graphIndex].G.node[j]['buffer'].evalExpression(vals);
					#check if max is exceeded
				    if(evaluation >= graphs[graphIndex].G.node[j]['buffer'].size):
					paths2[graphIndex][graphIndex].overflowFlag = True;
					graphs[graphIndex].G.node[j]['overflowFlag'] = True;

		renderGraph = []
        for graphIndex in range(len(paths)):
        	renderGraph.append(nx_agraph.to_agraph(graphs[graphIndex].G));
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

        for graphIndex in range(len(paths)):
		if (paths2[graphIndex][graphIndex].overflowFlag == True):
                    print("Overflow Trace " + str(count) + "\n")
                    fw.write("Overflow Trace " + str(count) + "\n")
                    tempGraph = renderGraph[graphIndex];
                    for j in paths2[graphIndex][graphIndex].nodeList:
                        if(graphs[graphIndex].G.node[j]['overflowFlag'] == True):
                            lineNum = graphs[graphIndex].G.node[j]['line']
                            if(lineNum != ''):
                                tmpLine = "At Line " + lineNum + ": Exception: Warning! Overflow Detected:" + re.sub(r"\s+"," ",codeString[int(lineNum) - 1])
                                print(tmpLine)
                                fw.write(tmpLine + "\n")
                            tempNode = tempGraph.get_node(j)
                            tempNode.attr['style'] = 'filled'
                            tempNode.attr['fillcolor'] = 'red'
                        else:
                            tempNode = tempGraph.get_node(j)
                            lineNum = graphs[graphIndex] .G.node[j]['line']
                            if(lineNum != ''):
                                tmpLine = "At Line " + lineNum + ":" + re.sub(r"\s+"," ",codeString[int(lineNum) - 1])
                                print(tmpLine)
                                fw.write(tmpLine + "\n")
                            tempNode.attr['style'] = 'filled'
                            tempNode.attr['fillcolor'] = 'yellow'
                    tempGraph.layout(prog='dot')
                    tempGraph.draw('../out/'+cufile+'/trace' + str(count) + '.png')
                    count+= 1
                    fw.write("\n\n\n--------------------------------------------------------------------------\n\n\n")
                    print("\n\n\n--------------------------------------------------------------------------\n\n\n")
        fw.close()

                                            
if __name__ == "__main__":
    main(sys.argv[1:])
        

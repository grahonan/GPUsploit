"""A path of custom nodes representing a program trace"""

#from .node import Node

class Path():

    def __init__(self, edgeList):
        self.nodeList = self.getNodeList(edgeList);
        self.overflowFlag = False;

    def getNodeList(self, edgeList):
        return [node for node in edgeList]

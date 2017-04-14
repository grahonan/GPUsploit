from accessor import Accessor

class Node():

    def __init__(self, buf, accessorList):
    	self.buf = buf;
    	self.overflowFlag = False;
    	self.accessorList = accessorList; # list of accessors
    
    def getBuf(self):
    	return self.buf;
    	
    def getOverflowFlag(self):
    	return self.overflowFlag;	
    
    def getAccessorsList(self):
    	return self.accessorsList;
    	   	
    def setBuf(self,buf):
    	self.buf = buf;
    	
    def setOverflowFlag(self,overflowFlag):
    	self.overflowFlag = overflowFlag;
	
	def setAccessorsList(self,accessorsList):
		self.accessorsList = accessorsList;

def main():
	node = Node("test",[Accessor("i",5)]);
	print(node.accessorList[0].var);
	print(node.getOverflowFlag());
	node.setOverflowFlag(True);
	print(node.getOverflowFlag());
	
if __name__ == "__main__":
    main()
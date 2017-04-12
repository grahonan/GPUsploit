class Node():

    def __init__(self, buf, accessorList):
    	self.buf = buf;
    	self.overflowFlag = False;
    	self.accessorList = accessorList; # list of accessor vars
    
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
	node = Node("test",5);
	print(node.getOverflowFlag());
	node.setOverflowFlag(True);
	print(node.getOverflowFlag());
	
if __name__ == "__main__":
    main()
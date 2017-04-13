class Buf():

    def __init__(self, accessorList, size, expression, type):
    	self.accessorList = accessorList; # list of accessor vars
    	self.size = size; # number
    	self.expression = expression; # relation between accessor vars as a string, e.g. "i+j"
    	self.type = type; # type of buffer content as a string, e.g. "int"
    	
    def getAccessorList(self):
    	return self.accessorList;
    	
    def getSize(self):
    	return self.size;
    	
    def getExpression(self):
    	return self.expression;
    	
    def getType(self):
    	return self.type;
	
	def setAccessorList(self,accessorList):
		self.accessorList = accessorList;
    	
    def setSize(self, size):
    	self.size = size;
    	
    def setExpression(self,expression):
    	self.expression = expression;
    	
    def setType(self,type):
    	self.type = type;


def main():
	buffer = Buf("test",5,"i+k",int);
	print(buffer.getSize());
	buffer.setSize(22);
	print(buffer.getSize());
	
if __name__ == "__main__":
    main()
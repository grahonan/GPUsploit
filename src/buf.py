from numericstringparser import NumericStringParser
from accessor import Accessor

class Buf():

    def __init__(self, accessorList, size, expression, type):
    	self.accessorList = accessorList; # list of accessors
    	self.size = size; # number
    	self.expression = expression; # relation between accessor vars as a string, e.g. "i+j"
    	self.type = type; # type of buffer content as a string, e.g. "int"
    	self.nsp = NumericStringParser();
    	
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
    	
    	
    def evalExpression(self,vals):
    	remake = self.expression;
    	for index in range(len(vals)):
    		remake = remake.replace(self.accessorList[index].var,str(vals[index]));
		print("Remake");
		print(remake);
    	return self.nsp.eval(remake);



def main():
	accarr = [Accessor("i",2),Accessor("j",2)];
	buffer = Buf(accarr,5,"i+j","int");
	print(buffer.getSize());
	buffer.setSize(22);
	print(buffer.getSize());
	arr = [1,2];
	arr2 = [99,2];
	print(buffer.evalExpression(arr));
	print(buffer.evalExpression(arr2));
	
if __name__ == "__main__":
    main()
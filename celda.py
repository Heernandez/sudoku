class Celda:

    def __init__(self):
        self.value = ""
        self.totalAdd = ""
        self.siblingList = [] #coordenadas x,y de sus hermanos [[1,1],[3,1]]
    
    def setValue(self,value):
        self.value = value
    
    def getValue(self):
        return self.value

    def setSiblings(self,positionList):
        self.siblingList.append(positionList)
    
    def setSibling(self,positionList):
        self.setSibling.append(positionList)


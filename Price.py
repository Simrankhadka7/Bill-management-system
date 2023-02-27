class Price:
    #constructor
    def __init__(self,itemName, markedPrice, vatAmount, finalAmount):
        #prevent negative input in all prices
        self.itemName = itemName
        self.markedPrice = markedPrice if(self.preventNegative(markedPrice)) else 0
        self.vatAmount = vatAmount if(self.preventNegative(vatAmount)) else 0
        self.finalAmount = finalAmount if(self.preventNegative(finalAmount)) else 0
        
    #get JSON 
    def getJSON(self):
        
        dataDictionary = {
            "itemName": self.stringify(self.itemName),
            "markedPrice": self.stringify(self.markedPrice),
            "vatAmount": self.stringify(self.vatAmount),
            "finalAmount": self.stringify(self.finalAmount)
        }
        
        return dataDictionary
        
    #prevent negative input
    def preventNegative(self, amount):
        if amount >= 0:
            return True
        else:
            return False
     
    #stringify input   
    def stringify(self, input):
        return "{}".format(input)
    

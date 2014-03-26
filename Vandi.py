import sys

class RotateTire:
    def __init__(self, numberOfTyres, skipDirection, skipIndex):

        self.numberOfTyres = numberOfTyres
        self.skipDirection = skipDirection
        self.skipIndex = skipIndex

    def runMain(self):
        
        #Variables 
        startIndex = 0 
        spare = 'S'
        self.skipIndex = self.skipIndex + 1

        #Lists
        tireList = range(self.numberOfTyres)
        checkList = [0] * self.numberOfTyres
        
        print "%s - %s" % (spare, tireList)
        iterationCount = 0 
        firstIndex = (startIndex) % self.numberOfTyres
        secondIndex = (startIndex+self.skipIndex) % self.numberOfTyres
        self.rotateTyre(firstIndex, secondIndex, spare, tireList, checkList, iterationCount)
         

    def rotateTyre(self, firstIndex, secondIndex, spare, tireList, checkList, iterationCount):

        #End condition
        if iterationCount == self.numberOfTyres:
            return

        if  checkList[firstIndex] == 0:
            temp = spare
            spare = tireList[firstIndex]
            tireList[firstIndex] = temp
            print "%s - %s" % (spare, tireList)

        temp = tireList[secondIndex] 
        tireList[secondIndex] = spare
        spare = temp
        print "%s - %s" % (spare, tireList)
        checkList[secondIndex] = 1

   
        #Clockwise
        if self.skipDirection == 'C': 
            firstIndex = (firstIndex+self.skipIndex)%self.numberOfTyres
            secondIndex = (secondIndex+self.skipIndex)%self.numberOfTyres
            if(checkList[secondIndex] == 1):
                firstIndex +=1
                secondIndex +=1  

  
        #Anti clockwise
        elif self.skipDirection == 'CC':        
            firstIndex = (firstIndex-self.skipIndex)%self.numberOfTyres
            secondIndex = (secondIndex-self.skipIndex)%self.numberOfTyres
            if(checkList[secondIndex] == 1):
                firstIndex -=1
                secondIndex -=1  


        iterationCount += 1
        self.rotateTyre(firstIndex, secondIndex, spare, tireList, checkList,  iterationCount)
        
if __name__ == "__main__":
    rotate_obj = RotateTire(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    rotate_obj.runMain()

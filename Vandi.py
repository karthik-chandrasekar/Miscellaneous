import sys

class RotateTire:
    def __init__(self, numberOfTyres, shiftDirection, skipIndex):

        self.numberOfTyres = numberOfTyres
        self.shiftDirection = shiftDirection
        self.skipIndex = skipIndex
        self.outputList = []

    def runMain(self):
        
        #Variables 
        startIndex = 0 
        spare = 'S'
        self.skipIndex = self.skipIndex + 1

        #Lists
        self.tireList = range(self.numberOfTyres)
        self.checkList = [0] * self.numberOfTyres
        
        print "%s - %s" % (spare, self.tireList)
        
        tempList = [spare]
        tempList.extend(self.tireList)
        self.outputList.append(tempList)

        iterationCount = 0 
        firstIndex = (startIndex) % self.numberOfTyres
        secondIndex = (startIndex+self.skipIndex) % self.numberOfTyres
        self.rotateTyre(firstIndex, secondIndex, spare, iterationCount)
        self.displayOutput()

    def rotateTyre(self, firstIndex, secondIndex, spare, iterationCount):

        #End condition
        if iterationCount == self.numberOfTyres:
            return

        #Runs at the beginning of every cycle
        if  self.checkList[firstIndex] == 0:
            temp = spare
            spare = self.tireList[firstIndex]
            self.tireList[firstIndex] = temp
            print "%s - %s" % (spare, self.tireList)
            self.addOutput(spare, self.tireList)
        
        #Executes for every element    
        temp = self.tireList[secondIndex] 
        self.tireList[secondIndex] = spare
        spare = temp
        print "%s - %s" % (spare, self.tireList)
        self.checkList[secondIndex] = 1
        self.addOutput(spare, self.tireList)
 
        #Clockwise condition
        if self.shiftDirection == 'C': 
            firstIndex = (firstIndex+self.skipIndex)%self.numberOfTyres
            secondIndex = (secondIndex+self.skipIndex)%self.numberOfTyres
            if(self.checkList[secondIndex] == 1):
                firstIndex +=1
                secondIndex +=1  

        #Anti-clockwise condition
        elif self.shiftDirection == 'CC':        
            firstIndex = (firstIndex-self.skipIndex)%self.numberOfTyres
            secondIndex = (secondIndex-self.skipIndex)%self.numberOfTyres
            if(self.checkList[secondIndex] == 1):
                firstIndex -=1
                secondIndex -=1  

        iterationCount += 1
        self.rotateTyre(firstIndex, secondIndex, spare,  iterationCount)
   
    def addOutput(self, spare, tyreList):
        tempList = [spare]
        tempList.extend(self.tireList)
        self.outputList.append(tempList)
        

    def displayOutput(self):
        
        for index, tyresList in enumerate(self.outputList):
            subList = []
            subList.append(self.formatString(tyresList[0]))

            for tyre in tyresList[1:]:
                subList.append(self.formatString(tyre))
        
            print "State#%s: %s" % (index,', '.join(subList))
        print 'DONE.'       
        
    def formatString(self, tyre):
        if tyre == 'S':
            tyre = 'Spare'
        else:
            tyre = 'Tire#%s' % (tyre)
        return tyre
 

if __name__ == "__main__":
    rotate_obj = RotateTire(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    rotate_obj.runMain()

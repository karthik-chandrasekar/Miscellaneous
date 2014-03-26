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
        fromIndex = (startIndex) % self.numberOfTyres
        toIndex = (startIndex+self.skipIndex) % self.numberOfTyres
        self.rotateTyre(fromIndex, toIndex, spare, iterationCount)
        self.displayOutput()

    def rotateTyre(self, fromIndex, toIndex, spare, iterationCount):

        #End condition
        while iterationCount < self.numberOfTyres:

            #Runs at the beginning of every cycle
            if  self.checkList[fromIndex] == 0:
                temp = spare
                spare = self.tireList[fromIndex]
                self.tireList[fromIndex] = temp
                print "%s - %s" % (spare, self.tireList)
                self.addOutput(spare, self.tireList)
            
            #Executes for every element    
            temp = self.tireList[toIndex] 
            self.tireList[toIndex] = spare
            spare = temp
            print "%s - %s" % (spare, self.tireList)
            self.checkList[toIndex] = 1
            self.addOutput(spare, self.tireList)
     
            #Clockwise condition
            if self.shiftDirection == 'C':
                signDigit = 1

            #Anti-clockwise condition
            elif self.shiftDirection == 'CC':        
                signDigit = -1        
 
            fromIndex = (fromIndex+self.skipIndex * signDigit)%self.numberOfTyres
            toIndex = (toIndex+self.skipIndex * signDigit)%self.numberOfTyres
            if(self.checkList[toIndex] == 1):
                fromIndex = fromIndex + 1 * signDigit
                toIndex = toIndex + 1 * signDigit 

            iterationCount += 1
   
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

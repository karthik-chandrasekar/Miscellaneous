import sys

class RotateTire:
    def __init__(self, numberOfTyres, skipDirection, skipIndex):

        self.numberOfTyres = numberOfTyres
        self.skipDirection = skipDirection
        self.skipIndex = skipIndex
        self.outputList = []

    def runMain(self):
        
        #Variables 
        startIndex = 0 
        spare = 'S'
        self.skipIndex = self.skipIndex + 1

        #Lists
        tireList = range(self.numberOfTyres)
        checkList = [0] * self.numberOfTyres
        
        print "%s - %s" % (spare, tireList)
        
        tempList = [spare]
        tempList.extend(tireList)
        self.outputList.append(tempList)

        iterationCount = 0 
        firstIndex = (startIndex) % self.numberOfTyres
        secondIndex = (startIndex+self.skipIndex) % self.numberOfTyres
        self.rotateTyre(firstIndex, secondIndex, spare, tireList, checkList, iterationCount)
        self.displayOutput()

    def rotateTyre(self, firstIndex, secondIndex, spare, tireList, checkList, iterationCount):

        #End condition
        if iterationCount == self.numberOfTyres:
            return

        if  checkList[firstIndex] == 0:
            temp = spare
            spare = tireList[firstIndex]
            tireList[firstIndex] = temp
            print "%s - %s" % (spare, tireList)

            tempList = [spare]
            tempList.extend(tireList)
            self.outputList.append(tempList)
            

        temp = tireList[secondIndex] 
        tireList[secondIndex] = spare
        spare = temp
        print "%s - %s" % (spare, tireList)
        checkList[secondIndex] = 1

        tempList = [spare]
        tempList.extend(tireList)
        self.outputList.append(tempList)
  
 
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
            tyre = 'Time#%s' % (tyre)
        return tyre
 

if __name__ == "__main__":
    rotate_obj = RotateTire(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    rotate_obj.runMain()

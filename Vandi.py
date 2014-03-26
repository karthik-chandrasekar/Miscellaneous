import sys

class RotateTire:
    def __init__(self):
        pass

    def runMain(self, numberOfTires, skipDirection, skipIndex):
        
        #Variables 
        startIndex = 0 
        spare = 'S'
        skipIndex = skipIndex + 1

        #Lists
        tireList = range(numberOfTires)
        checkList = [0] * numberOfTires
        
        maxIndex = len(tireList)

        print "%s - %s" % (spare, tireList)
        self.rotateTire(startIndex%maxIndex, (startIndex+skipIndex)%maxIndex, spare, tireList, checkList, skipIndex, maxIndex, skipDirection)
        print "%s - %s" % (spare, tireList)
         

    def rotateTire(self, oneIndex, twoIndex, spare, tireList, checkList, skipIndex, maxIndex, skipDirection):

        #End condition
        if sum(checkList) == maxIndex - 1:
            for index, value in enumerate(tireList):
                if value == 'S':
                    tireList[index] = spare
            return

        if  checkList[oneIndex] == 0:
            temp = spare
            spare = tireList[oneIndex]
            tireList[oneIndex] = temp
            print "%s - %s" % (spare, tireList)

        temp = tireList[twoIndex] 
        tireList[twoIndex] = spare
        spare = temp
        print "%s - %s" % (spare, tireList)
        checkList[twoIndex] = 1
   
        #Clockwise
        if skipDirection == 'C': 
            oneIndex = (oneIndex+skipIndex)%maxIndex
            twoIndex = (twoIndex+skipIndex)%maxIndex
            if(checkList[twoIndex]) == 1:
                oneIndex +=1
                twoIndex +=1  
  
        #Anti clockwise
        elif skipDirection == 'CC':        
            oneIndex = (oneIndex-skipIndex)%maxIndex
            twoIndex = (twoIndex-skipIndex)%maxIndex
            if(checkList[twoIndex]) == 1:
                oneIndex -=1
                twoIndex -=1    

        self.rotateTire(oneIndex, twoIndex, spare, tireList, checkList, skipIndex, maxIndex, skipDirection)
        
if __name__ == "__main__":
    rotate_obj = RotateTire()
    rotate_obj.runMain(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    #rotate_obj.runMain(4, 'C', 1)

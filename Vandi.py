
class RotateTire:
    def __init__(self):
        pass

    def run_main(self, numberOfTires, skipDirection, skipNumber):
        
        tireList = range(numberOfTires)
        
        self.clockRotate(0, tireList, skipNumber+1)

    def clockRotate(self, index, tireList, skipIndex):
        spare = 'S'

        temp = None
        print "%s - %s" % (spare, tireList)
        self.singleRotate(index, index+skipIndex, spare, tireList, [0, 0, 0, 0, 0], skipIndex, len(tireList))
        print "%s - %s" % (spare, tireList)
         

    def singleRotate(self, oneIndex, twoIndex, spare, tireList, checkList, skipIndex, maxIndex):

        
        if sum(checkList) == maxIndex - 1:
            for index, value in enumerate(tireList):
                if value == 'S':
                    tireList[index] = spare
            return

        first = None
        if  checkList[oneIndex] == 0:
            temp = spare
            spare = tireList[oneIndex]
            first = spare
            tireList[oneIndex] = temp
            print "%s - %s" % (spare, tireList)

        temp = tireList[twoIndex] 
        tireList[twoIndex] = spare
        spare = temp
        print "%s - %s" % (spare, tireList)

        checkList[twoIndex] = 1
    
        oneIndex = (oneIndex+skipIndex)%maxIndex
        twoIndex = (twoIndex+skipIndex)%maxIndex
        
        if(checkList[twoIndex]) == 1:
            oneIndex +=1
            twoIndex +=1    

        self.singleRotate(oneIndex, twoIndex, spare, tireList, checkList, skipIndex, maxIndex)
        
if __name__ == "__main__":
    rotate_obj = RotateTire()
    rotate_obj.run_main(4, 'C', 1)

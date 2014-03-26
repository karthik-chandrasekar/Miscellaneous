import sys, logging

class RotateTyre:
    def __init__(self, numberOfTyres, shiftDirection, skipIndex):

        #Input parameters
        self.numberOfTyres = numberOfTyres
        self.shiftDirection = shiftDirection
        self.skipIndex = skipIndex + 1

        #Lists
        self.outputList = []
        self.tyreList = range(self.numberOfTyres)
        self.checkList = [0] * self.numberOfTyres

        #File
        self.logging = None
        self.logger_file = "TyreRotation.log"

    def initialize_logger(self):
        logging.basicConfig(filename=self.logger_file, level=logging.INFO)
        logging.info("Initialized logger")
        self.logging = logging

    def runMain(self):
        
        self.initialize_logger()
        self.logging.info("Number of Tyres - %s, Direction - %s, SkipIndex - %s" % (self.numberOfTyres, self.shiftDirection, self.skipIndex-1))
         
        #Variables 
        iterationCount = 0 
        startIndex = 0 
        spare = 'S'
        self.addOutput(spare)

        #Clockwise direction condition
        if self.shiftDirection == 'C':
            signDigit = 1

        #Anti-clockwise direction condition
        elif self.shiftDirection == 'CC':        
            signDigit = -1        
        fromIndex = (startIndex) % self.numberOfTyres
        toIndex = (startIndex+self.skipIndex * signDigit) % self.numberOfTyres
        

        self.rotateTyre(fromIndex, toIndex, spare, iterationCount)
        self.displayOutput()

    def rotateTyre(self, fromIndex, toIndex, spare, iterationCount):

        while iterationCount < self.numberOfTyres:

            #Runs at the beginning of every cycle
            if  self.checkList[fromIndex] == 0:
                temp = spare
                spare = self.tyreList[fromIndex]
                self.tyreList[fromIndex] = temp
                self.addOutput(spare)
            
            #Executes for every element    
            temp = self.tyreList[toIndex] 
            self.tyreList[toIndex] = spare
            spare = temp
            self.checkList[toIndex] = 1
            self.addOutput(spare)
     
            #Clockwise direction condition
            if self.shiftDirection == 'C':
                signDigit = 1

            #Anti-clockwise direction condition
            elif self.shiftDirection == 'CC':        
                signDigit = -1        
 
            fromIndex = (fromIndex+self.skipIndex * signDigit)%self.numberOfTyres
            toIndex = (toIndex+self.skipIndex * signDigit)%self.numberOfTyres
            if(self.checkList[toIndex] == 1):
                fromIndex = fromIndex + 1 * signDigit
                toIndex = toIndex + 1 * signDigit 

            iterationCount += 1
   
    def addOutput(self, spare):
        #Add state information of tyre rotation

        tempList = [spare]
        tempList.extend(self.tyreList)
        self.outputList.append(tempList)
        
    def displayOutput(self):
        #Prints the output in the desired form       
 
        for index, tyresList in enumerate(self.outputList):
            subList = []
            subList.append(self.formatString(tyresList[0]))
            for tyre in tyresList[1:]:
                subList.append(self.formatString(tyre))
            print "State#%s: %s" % (index,', '.join(subList))
        print 'DONE.'       
        
    def formatString(self, tyre):
        #Returns the string in desired format

        if tyre == 'S':
            tyre = 'Spare'
        else:
            tyre = 'Tyre#%s' % (tyre)
        return tyre

if __name__ == "__main__":

    if (len(sys.argv) == 4):
        if sys.argv[2] not in ('C', 'CC'):
            print "Direction is not valid. Please select between C-Clockwise/CC-Counter Clockwise"
            sys.exit()

        if int(sys.argv[1]) == 0:
            print "Enter valid number of tyres"
            sys.exit()

        rotate_obj = RotateTyre(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
        rotate_obj.runMain()
    else:
        print "Please enter all the input parameters - Number of tyres, Direction, Skip number"        

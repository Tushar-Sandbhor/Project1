import sys
import random

def CreateSampleFile(noOfRows, numOfElements):
    """ This function creates sample file with inputs like 'number of rows',
        'number of elements' given in the console input"""
    tempArray = []
    
    fp = open('sample.txt', 'w')
    
    for row in range(noOfRows):
        for ele in range(numOfElements):
            tempArray.append(str(random.randint(1, 100)))
        fp.write(' '.join(tempArray))
        fp.write('\n')
        tempArray = []
        
    fp.close()
            
        
def ProcessNDumpResults():
    """ This function reads the created sample files with inputs like 'number of rows',
        'number of elements' and multiplies every element in row with given multiplier."""
         
    resultArray = []
    fp = open('sample.txt', 'r')
    for line in fp.readlines():
        tempVar = map(int, line.split(' '))
        resultArray.extend([var*multiplier for var in tempVar])
        
    with open('result.txt', 'w') as fw:
        fw.write(str(resultArray))
    


if __name__ == '__main__':
    noOfRows, numOfElements, multiplier = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    CreateSampleFile(noOfRows, numOfElements)
    ProcessNDumpResults()

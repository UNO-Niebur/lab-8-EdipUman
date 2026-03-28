#ProcessData.py
#Name:Edip Uman
#Date:3/28/26
#Assignment: Lab 8

import random
 
def makeID(first, last, idNum):
    
    if len(last) < 5:
        last = last + "x"
 
    
    idLen = len(idNum)
    id = first[0].lower() + last.lower() + idNum[idLen - 3:]
    return id
 
def makeMajorYear(major, year):
    
    majorPart = major[:3].upper()
 
    
    if year == "Freshman":
        yearPart = "FR"
    elif year == "Sophomore":
        yearPart = "SO"
    elif year == "Junior":
        yearPart = "JR"
    else:
        yearPart = "SR"
 
    return majorPart + "-" + yearPart
 
def getFirst(data):
    return data[0]
 
def getLast(data):
    return data[1]
 
def main():
 
   
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')
 
    
    for line in inFile:
        data = line.split()
        first = getFirst(data)
        last = getLast(data)
        idNum = data[3]
        year = data[5]
        major = data[6]
 
        student_id = makeID(first, last, idNum)
        major_year = makeMajorYear(major, year)
 
        output = last + "," + first + "," + student_id + "," + major_year + "\n"
        outFile.write(output)
 
    #Close files in the end to save and ensure they are not damaged.
    inFile.close()
    outFile.close()
 
if __name__ == '__main__':
    main()

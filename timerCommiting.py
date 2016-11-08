# date and time retriving
import datetime
import StringIO

nowDT = datetime.datetime.now()
nowString = nowDT.strftime("%Y %m %d %H").replace(" ","") + "\n" 
print(nowDT)

# function of writing into files 
# and git operations

import os

def write2File(counter):
    # get date and time
    nowDT = datetime.datetime.now()
    nowString = nowDT.strftime("%Y %m %d %H").replace(" ","") + "\n" 
    
    # create new file
    fileName  = "stamp/" + nowString.strip() + ".txt"
    stampFile = open(fileName, "w")
    stampFile.close()

    # write to and close file
    for i in range(0, counter):
        stampFile = open(fileName, "w")
        stampFile.write(nowString)
        stampFile.close()
        addCommand = "git add stamp/" + fileName
        commitCommand = "git commit -m \"updated" + str(i) + "on " + nowDT.strftime("%Y %m %d") + "\""

    print(filename)

    return(counter + 1)

def timerWrite(counter):
    counter = write2File(counter)
    threading.Timer(60, timerWrite).start()
    return(counter)

totalDays = 50
iterCounter = 1

while(iterCounter <- totalDays):
    iterCounter = timerWrite()

# addCommand = "git add stamp/fileName"
# commitCommand = "git commit -m \"updated " + str(iterCounter) + " on " + nowDT.strftime("%Y %m %d") + "\""


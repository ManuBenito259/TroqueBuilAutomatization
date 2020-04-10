
import os
import sys
from zipfile import ZipFile
import datetime

#Obteining the current time
currentDT = datetime.datetime.now()

#Create the name of the build
buildName = "ConDetodo-"  + sys.argv[1] + "-Build_date-" + currentDT.strftime("%d-%m-%Y") +"-at-"+currentDT.strftime("%H-%M") + ".zip"

#Create a zip object
zipObj = ZipFile(buildName, "w")




# Iterate over all the files in directory
for folderName, subfolders, filenames in os.walk("build"):
    for filename in filenames:
        #create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        zipObj.write(filePath)


#Close the zip object
zipObj.close()

#saving the build name to upload
buildRegister = open("latestBuild.txt", "w")
buildRegister.write(buildName)
buildRegister.close()
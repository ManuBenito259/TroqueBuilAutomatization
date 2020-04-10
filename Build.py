from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import sys
from zipfile import ZipFile
import datetime

#Obteining the current time
currentDT = datetime.datetime.now()

#Create the name of the build
buildName = "ConDetodo-" + sys.argv[1] + "-Build_date-" + currentDT.strftime("%d-%m-%Y") +"-at-"+currentDT.strftime("%H-%M") + ".zip"

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

#Upload the file to Drive
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

with open(buildName,"r") as file:
    file_drive = drive.CreateFile({'title': os.path.basename(file.name)})
    file_drive.SetContentString(file.read())
    file_drive.Upload()
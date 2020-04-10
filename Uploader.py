from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


#Atuhenticate with Google Drive
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

#Obtain the name of the last build
buildReg = open("latestBuild.txt", "r")
buildName = buildReg.read();
buildReg.close()


#Create the drive file and upload it
file_drive = drive.CreateFile({'title': os.path.basename(buildName)})
file_drive.SetContentFile(buildName)
file_drive.Upload()
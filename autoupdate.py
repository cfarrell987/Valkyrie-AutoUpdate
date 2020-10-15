#SteamCMD Workshop Mods Auto Updater for Arma 3 Mods.
#Written By: Caleb 'Crow' Farrell
#Date: 2020 - 10 - 15

import glob
import re
import os

#Arma 3 SteamID
appId = '107410'

#Arma3 Server SteamID
serverAppId = '233780'
#Arma 3 Workshop Mod ID
publishedId = []
#ALL Mods should have a meta.cpp file, if not at the moment this will crash the script.
#I'm to lazy to actually make this not happen and skip the files that don't. suck it up.
metaFile = "meta.cpp"
#This should reference where you store all your mods,
# AGAIN STORE THEM ALL IN A SEPERATE FOLDER
# AS SAID ABOVE FAILURE TO DO SO WILL CRASH THE SCRIPT
modStorePath = input("Enter Path to mods store: ")
print("Path is: " + modStorePath)

#Getting all mod folders
modFolders = glob.glob(modStorePath + "/*/")

print(modFolders)

#This is reading the meta.cpp for the publisherID and appending it to our array
for item in modFolders:
    print(item)
    f = open(item + metaFile)
    lines = (f.readlines())
    publishedId.append(lines[1])

#here we define a new array for the cleansed publisherIDs
publishedIDs = []
#Thanks to ZE JEW #9273 on Discord for the assistance on this one!
for i in publishedId:
    publishedIDs.append(
        int(
            ''.join(
                re.findall(r'\d+', i)
            )
        )
    )

print(publishedIDs)

#Running the steamCMD with to update Arma server

steamCmdPath = input("Define Path to SteamCMD: " )
print(steamCmdPath)

serverPath = input("Define Path to Arma 3 Server: ")
print(serverPath)



os.system('cd' + steamCmdPath)
os.system('SteamCMD +login anonymous + force_install_dir' + serverPath + '+app_update' + serverAppId + 'validate +quit')




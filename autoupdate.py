#Valkyrie-AutoUpdate
#Written By: Caleb 'Crow' Farrell
#Date: 2020 - 10 - 15

import glob
import re
import os
import time
import json

#config stuffs
configFile = 'config.json'

with open(configFile, 'r') as f:
    datastore = json.load(f)

steamCMDPath = datastore["steamCmdPath"]
serverPath = datastore["arma3ServerPath"]
modsRepoPath = datastore["modsRepoPath"]

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

print(" Mods Repo Path is: " + modsRepoPath)

#Getting all mod folders
modFolders = glob.glob(modsRepoPath + "/*/")

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

#Running the steamCMD to update Arma server
print(steamCMDPath)

print(serverPath)


os.system(steamCMDPath+'\\'+'SteamCMD +login anonymous + force_install_dir' + serverPath + '+app_update' + serverAppId + 'validate +quit')

for item in publishedIDs:
    print(item)
    os.system(steamCMDPath+'\\'+'SteamCMD +login anonymous + force_install_dir' + serverPath + '+workshop_download_item' + appId + str(item) + 'validate +quit')
    time.sleep(15)


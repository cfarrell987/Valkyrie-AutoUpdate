# Valkyrie-AutoUpdate
# Written By: Caleb 'Crow' Farrell
# Date: 2020 - 10 - 15

# TODO: allow for both anon and signed in use of SteamCMD
# In Progress:
# TODO: Create a system for users to download new mods by checking a file and referencing it to the array of existing

import glob
import re
import os
import time
import json
import logging
import csv


# config stuffs
configFile = 'config.json'
with open(configFile, 'r') as f:
    datastore = json.load(f)

steamCMDPath = datastore["steamCmdPath"]
serverPath = datastore["arma3ServerPath"]
modsRepoPath = datastore["modsRepoPath"]

serverUpdateEnabled = int(datastore["serverUpdateEnabled"])
debuggingMode = int(datastore["debuggingMode"])
# Logging Stuffs
loggingEnabled = int(datastore["loggingEnabled"])
if loggingEnabled == 1:
    if not os.path.exists('./logs'):
        os.mkdir('./logs')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='./logs/' + time.strftime("%Y-%m-%d %H-%M-%S_") + 'OUTPUT.log', level=logging.DEBUG)
else:
    logging.warning("LOGGING IS DISABLED")

logging.info('Initializing...')

# Arma 3 SteamID
appId = '107410'
# Arma3 Server SteamID
serverAppId = '233780'
# Arma 3 Workshop Mod ID
publishedId = []
#setting var for meta file
metaFile = "meta.cpp"

print(" Mods Repo Path is: " + modsRepoPath)
logging.info('Complete!')

# Getting all mod folders
modFolders = glob.glob(modsRepoPath + "/*/")

print(modFolders)
# This is reading the meta.cpp for the publisherID and appending it to our array
for item in modFolders:
    print(item)
    if os.path.exists(item + './' + metaFile):
        f = open(item + metaFile)
        lines = (f.readlines())
        publishedId.append(lines[1])
    else:
        logging.warning("meta.cpp does not exist in:" + item + "If mod folder please re-download manually")
# here we define a new array for the cleansed publisherIDs
publishedIDs = []

# Thanks to ZE JEW #9273 on Discord for the assistance on this one!
for i in publishedId:
    publishedIDs.append(
        int(
            ''.join(
                re.findall(r'\d+', i)
            )
        )
    )

# WIP may not work as intended yet
# if you don't like it, delete it

indices = []
for i in range(len(publishedIDs)):
    if publishedIDs[i] == 0:
        indices.append(i)

nullMeta = [modFolders[index] for index in indices]
logging.warning("PublishedID is Null in:" + str(nullMeta))

print(publishedIDs)
# Running the steamCMD to update Arma server
print(steamCMDPath)

print(serverPath)

# Checking for new mods in CSV, referencing existing publishedIDs to ensure re-download isn't done
newMods = []
if not os.path.exists("./newMods.csv"):
    f = open("./newMods.csv", "x")

else:
    with open("./newMods.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
if serverUpdateEnabled == 1:
    os.system(steamCMDPath + '\\' + 'SteamCMD +login anonymous + force_install_dir' + serverPath + '+app_update' + serverAppId + 'validate +quit')
else:
    logging.warning("Server Update is Disabled!")

if not debuggingMode == 1:
    for item in publishedIDs:
        print(item)
        os.system(
            steamCMDPath + '\\' + 'SteamCMD +login anonymous + force_install_dir' + serverPath + '+workshop_download_item' + appId + str(
                item) + 'validate +quit')
        time.sleep(15)
else:
    logging.warning("Debugging Mode Enabled!")
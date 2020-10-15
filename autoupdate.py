import glob
import re
import os
#SteamCMD Workshop Mods Auto Updater for Arma 3 Mods.
#Written By: Caleb 'Crow' Farrell
#Date: 2020 - 10 - 15
appId = '107410'
publishedId = []
metaFile = "meta.cpp"
modStorePath = input("Enter Path to mods store: ")
print("Path is: " + modStorePath)

modFolders = glob.glob(modStorePath + "/*/")

print(modFolders)

for item in modFolders:
    print(item)
    f = open(item + metaFile)
    lines = (f.readlines())
    publishedId.append(lines[1])

publishedIDs = []
for i in publishedId:
    publishedIDs.append(
        int(
            ''.join(
                re.findall(r'\d+', i)
            )
        )
    )

os.system('SteamCMD +login anonymous + force_install_dir "F:\SteamLibrary\steamapps\common\Arma 3 Server" +app_update' + appId + 'validate +quit')



print(publishedIDs)
#SteamCMD Workshop Mods Auto Updater.
#This Specific program is using ArmA 3 as it's game
#This can be changed by changing the appid variable
#Written By: Caleb 'Crow' Farrell
#Date: 2020 - 10 - 15

import os
import glob

appId = 107410
publishedId=[]
metaFile= "meta.cpp"
modStorePath = input("Enter Path to mods store: ")
print("Path is: " + modStorePath)

modFolders = glob.glob(modStorePath + "/*/")

print(modFolders)

for item in modFolders:
    print(item)
    f = open(item+metaFile)
    lines = (f.readlines())
    publishedId.append(lines[1])

x=0
for i in publishedId:
    publishedId[x]=i.rstrip('n')
    x+=1


print(publishedId)
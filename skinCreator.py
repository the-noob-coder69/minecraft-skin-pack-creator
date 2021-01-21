
import json,os

path='/storage/emulated/0/games/com.mojang/skin_packs/Shantnu\'s skin pack/'
f=open(path+"skins.json",'r')

full_data=json.load(f)
skins=full_data['skins']

skin_names=[]

for i in skins:
    skin_names.append(i['localization_name'])


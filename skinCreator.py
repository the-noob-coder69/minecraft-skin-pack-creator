import json,os
import re

def load_skinjson(file):
    print('loading file')
    full_data=json.load(file)
    skins=full_data['skins']

    skin_names=[]
    for i in skins:
        skin_names.append(i['localization_name'])

    print('full_data',full_data,'skins',skins,'skin_names',skin_names,sep='\n\n\n\n\n\n')

def skins(path) -> list:
    lst=[]
    print(os.listdir(path))
    for i in os.listdir(path):
        if i[-3:]=='png':
            for j in ["geometry.humanoid.custom", "geometry.humanoid.customSlim"]:
                if j[-4:]=='Slim': lst.append(skin(i[:-4]+' slim',j,i,'free'))
                else: lst.append(skin(i[:-4],j,i,'free'))
    return lst

def skin(name: str,geo: str,texture: str,type: str) -> dict:
    return {"localization_name":name,"geometry":geo,"texture":texture,"type":type}

def create_skinjsonfile(path: str,sname: str,lname: str) -> dict:
    """json file format :-
    {
        "skins":[
            {
                "localization_name":...,
                "geometry":...,
                "texture":...,
                "type":...
            }
        ],
        "serialize_name":...,
        "localization_name":...
    }
    """
    return {"skins":skins(path),"serialize_name":sname,"localization_name":lname}

def main():
    from config import path
    f=open(path+"skins.json",'r')
    load_skinjson(f)
main()
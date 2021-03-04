import json,os


def load_skinjson(file):
    full_data=json.load(file)
    skins=full_data['skins']

    skin_names=[]
    for i in skins:
        skin_names.append(i['localization_name'])

    print('full_data',full_data,'skins',skins,'skin_names',skin_names,sep='\n\n\n\n\n\n')

def main():
    from config import path
    f=open(path+"skins.json",'r')
    load_skinjson(f)
import zipfile
import os
import re

a = os.listdir(r"./")[:-1]  #in this Folder all zipfile unzip
a = filter(lambda x : re.search("zip", x), a)   #filterling zip file

def zipout(opath,outpath,password):
    zip = zipfile.ZipFile(opath, "r",zipfile.zlib.DEFLATED)
    try:
        zip.extractall(path=outpath,members=zip.namelist() , pwd=password)  #unzip path and using password
        return 1
    except:
        return 0

ppass="start"   #zip password

while(1):
    for f in a:
        if zipout(r"./"+f,r"./out/"+f,ppass)==1:    #if zipfile password is corrected
            print (f + '\n')
            r=open(r"./out/"+f+"/1.txt","r")    #make folder and output text
            rr=r.read()
            print rr
            r.close()
            ppass=rr.split("\n")[0].split("is ")[1] #parsing



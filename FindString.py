import os
import sys
import optparse
 
def FindString(msg,verbos):
    ResultFile = open("result","w")
    for (path,dirname,files) in os.walk("/Users/kimtae"):
        for filenames in files:
            try:
                if verbos:
                    print "[*]check "+path+"/"+filenames
                f = open(path+"/"+filenames,"r")
                buf = f.read()
                f.close()
                if msg in buf:
                    ResultFile.write(path+"/"+filenames+"\n")
                    print "[*]find "+path+"/"+filenames
            except:
                continue
 
    ResultFile.close()
 
def main():
    parser = optparse.OptionParser(usage="FindString.py "+"-v True "+"Searc_String")
    parser.add_option("-v",dest="Vervos",type="string",help="Dicide whether print detail or not")
 
    (options,args) = parser.parse_args()
    if(len(args) == 0):
        print parser.usage
        return
    FindString(args[0],options.Vervos); 
 
 
if __name__ == '__main__':
	main()


import sys
from ruler import Ruler


DATASET = sys.argv[1]
# L'argument envoyé par le sytème est [bundle.py, fichier.txt]
with open(DATASET,'r') as f:
    l = ""
    t = 0
    for i, line in enumerate(f,start=1):
        if i%2 != 0:
            l = line
        else:
            ruler = Ruler(l,line)
            ruler.compute()
            top, bottom = ruler.report()
            t += 1
            print(f"====== exemple #{t}- distance ={ruler.distance()}\n{top}\n{bottom}")
        
            
        
            
        
        
        
            
            
            
            

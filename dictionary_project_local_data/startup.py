from os import getcwd
from sys import path

path.insert(1,getcwd()+"\\Library\\")

import Library

vloop = "Y"
vask = "N"

while (vloop=="Y") or (vloop=="y"):

    Library.main.main()

    while (vask=="N"):
            vloop= input ("\nDo you want to try another word? (Y/N) ")
            
            if (vloop=="Y") or (vloop=="N") or (vloop=="y") or (vloop=="n"):
                vask="Y"
            else:
                print ("Incorrect option")
                vask="N"
    vask = "N"
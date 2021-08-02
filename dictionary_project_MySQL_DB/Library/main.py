from os import getcwd
from sys import path

path.insert(1,getcwd()+"\\Library\\packages\\")

import packages


def main():
    
    vloop = "Y"
    vask = "N"
    
    configpath = getcwd()+"\\Library\\config\\"

    dbcon = packages.db_connect.db_connect(configpath)

    dictionary = packages.load_dict.load_dict_data(dbcon)
    
    while (vloop=="Y") or (vloop=="y"):

        search_word = packages.user_input.user_input(dictionary)

        meanings = packages.search.search(search_word[1].lower(),dictionary)
        if len(meanings) == 0:
            print(f"\nKeyError : The entered word '{search_word[0]}' is not found in dictionary, please double check it.")
        elif len(meanings) == 1:
            if search_word[2] == 2:
                print (f"\nThere is {len(meanings)} meaning for '{search_word[1]}' found in dictionary")
            else:
                print (f"\nThere is {len(meanings)} meaning for '{search_word[0]}' found in dictionary")
        else:
            if search_word[2] == 2:
                print (f"\nThere are {len(meanings)} meanings for '{search_word[1]}' found in dictionary")
            else:
                print (f"\nThere are {len(meanings)} meanings for '{search_word[0]}' found in dictionary")

        count = 0
        for meaning in meanings:
            count = count+1
            print (f"\n{count}) {meaning}")

        while (vask=="N"):
            vloop= input ("\nDo you want to try another word? (Y/N) ")
            
            if (vloop=="Y") or (vloop=="N") or (vloop=="y") or (vloop=="n"):
                vask="Y"
            else:
                print ("Incorrect option")
                vask="N"
        vask = "N"
    
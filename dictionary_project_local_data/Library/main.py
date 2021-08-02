from os import getcwd
from sys import path

path.insert(1,getcwd()+"\\Library\\packages\\")

import packages


def main():
    datapath = getcwd()+"\\Library\\data\\"

    dictionary = packages.load_dict.load_dict_data(datapath)
    
    search_word = packages.user_input.user_input(dictionary)

    try:
        meanings = packages.search.search(search_word[1].lower(),dictionary)
        if len(meanings) == 1:
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

    except KeyError as e:
        print ("\n" + e.__class__.__name__,f": The entered word '{search_word[0]}' is not found in dictionary, please double check it.")

    
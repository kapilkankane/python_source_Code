from difflib import get_close_matches

def get_match(word,dict_data):
    match_word = get_close_matches(word,dict_data.keys())
    if len(match_word) != 0:
        return match_word[0]
    else:
        return None

def user_input(dict_data):
    input_word = input("\nEnter word to search in Dictionary: ")

    
    if input_word.lower() in dict_data.keys():
        return (input_word,input_word,1)    
    else:
        response = "Y"
        check_input = "N"
        match_word = get_match(input_word.lower(),dict_data)

        if match_word != None:
            while (check_input == "N"):
                response = input ("\nThe entered word '{}' seems to be incorrect, do you want to search for '{}' instead ? (Y/N) : ".format(input_word,match_word.title()))

                if (response == "Y") or (response == "y"):
                    check_input = "Y"
                    return (input_word,match_word.title(),2)

                elif (response == "N") or (response == "n"):
                    return (input_word,input_word,1)
                else:
                    print ("Incorrect option")
                    check_input = "N"
        else:
            return (input_word,input_word,1)
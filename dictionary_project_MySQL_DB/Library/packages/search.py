def search(word,dict_data):
    meanings = []
    for dict_values in dict_data:
        if dict_values[0].lower() == word:
            meanings.append(dict_values[1])
    return meanings
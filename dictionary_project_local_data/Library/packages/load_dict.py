# import required module
from os import getcwd
from sys import path
from cryptography.fernet import Fernet


def load_dict_data(datapath):

#    with open(datapath + "datakey.key", "rb") as filekey:
#            key = filekey.read()
    try:
        # opening the key
        with open(datapath + "datakey.key", "rb") as filekey:
            key = filekey.read()
    except FileNotFoundError as e:
        print ("\n"+ e.__class__.__name__,": The datakey file is missing. Contact Support.")
        exit()

    try:
        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open(datapath + "data.encrpyted", "rb") as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
    except FileNotFoundError as e:
        print ("\n"+ e.__class__.__name__,": The data file for dictionary is missing. Contact Support.")
        exit()
    except Exception as e:
        print ("\n" + e.__class__.__name__,f": The datakey file is corrupted. Contact Support.")
        exit()
    else:
        data = eval(decrypted)
        #data = json.load(open(filepath))
        data =  {k.lower(): v for k, v in data.items()}
        return data

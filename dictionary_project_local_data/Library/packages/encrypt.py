# import required module
from os import getcwd
from sys import path
from cryptography.fernet import Fernet

datafile = getcwd()+"\\Library\\data\\data.json"
datapath = getcwd()+"\\Library\\data\\"

# key generation
key = Fernet.generate_key()
  
# string the key in a file
with open(datapath + "datakey.key", "wb") as filekey:
   filekey.write(key)
   
 # opening the key
with open(datapath + "datakey.key", "rb") as filekey:
    key = filekey.read()
  
# using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open(datafile, "rb") as file:
    original = file.read()
      
# encrypting the file
encrypted = fernet.encrypt(original)
  
# opening the file in write mode and 
# writing the encrypted data
with open(datapath + "data.encrpyted", "wb") as encrypted_file:
    encrypted_file.write(encrypted)
import mysql.connector
import stdiomask

class ConfigFileError(Exception): 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

def db_connect(configpath):

        try:
                username = input("Enter Username: ")
                password = stdiomask.getpass("Enter Password: ")
                try:
                        with open(configpath + "config","r") as configfile:
                                dbconfig = eval(configfile.read())
                                if type(dbconfig) != dict:
                                        raise ConfigFileError("Config file cannot be parsed, it might be corrupted. Contact Support.")
                except ConfigFileError as e:
                        print("\n" + e.__class__.__name__ + " : " + e.value)
                        exit()
                except FileNotFoundError as e:
                        print("\n" + e.__class__.__name__ + " : The config file for database is missing. Contact Support.")
                        exit()
        
                con = mysql.connector.connect(
                        user = username, #"ardit700_student",
                        password = password, #"ardit700_student",
                        host = dbconfig["hostname"],  #"108.167.140.122",
                        database = dbconfig["database"] #"ardit700_pm1database"
                        )
                return con
        except Exception as e:
                print("\n" + e.__class__.__name__ + " : " + e.args[1])
                exit()

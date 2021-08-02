class NoDataFoundError(Exception): 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
 
def load_dict_data(dbcon):
    try:

        cursor = dbcon.cursor()

        query = cursor.execute("SELECT * FROM dictionary")

        dict_data = cursor.fetchall()

        if len(dict_data) == 0:
            raise NoDataFoundError("Dictionary cannot be loaded, no data found in database. Contact Support.")

        return dict_data

    except NoDataFoundError as e:
            print("\n" + e.__class__.__name__ + " : " + e.value)
            exit()
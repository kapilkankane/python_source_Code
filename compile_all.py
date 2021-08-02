from os import getcwd,listdir,path
from sys import argv
from compileall import compile_dir


dir_content = listdir(getcwd())
dir_list = []
i=1
x = "Y"
z = "N"
dir_to_compile = ''

for item in dir_content:
    if path.isdir(item):
        dir_list.append(item)

dir_list.append("Exit")

dir_list_len = len(dir_list)

for item in dir_list:
    print (i,item)
    i = i + 1

while (x == 'Y') or (x == 'y'):
    print("\n(enter the number against the Project)")
    dir_num = input("Which Project you want to compile from the above list? ")
    
    if dir_num.strip().isdigit():
        if (eval(dir_num) > 0) and (eval(dir_num) <= (dir_list_len-1)):
                comp_dir = getcwd() + "\\" + dir_list[eval(dir_num)-1] + "\\"
                print("Compiling here: '" + comp_dir)
                compile_dir(comp_dir,force=True)

                while (z == "N"):
                    x= input("\nDo you want to Compile another Project ? (Y/N) ")
                    
                    if (x == "Y") or (x == "N") or (x == "y") or (x == "n"):
                        z = "Y"
                    else:
                        print ("Incorrect option")
                        z = "N"
                z = "N"
        elif eval(dir_num) == dir_list_len:
            print ("Thank You")
            x = 'N'
        else:
            print("Invalid Directory, please select directory number from the list above.")
    else:
        print("Invalid input, please select the directory number from the list above.")
from os import getcwd
from sys import path

path.insert(1,getcwd()+"\\Library\\")

import Library

Library.main.main()
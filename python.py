import datetime
import os.path
import sys

filename = "write_demo.txt"
file_exists = os.path.isfile(filename)

menu_options = {
    1: 'Addition'
    2: 'Substraction'
    3: 'Multiplication',
    4: 'Division',
    5: 'Exit'

}

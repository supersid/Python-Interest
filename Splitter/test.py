import xlsxwriter 
# Insert an image with scaling.
import os, os.path

# simple version for working with CWD
DIR = './data'
#Found the number of files
num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

print(num)
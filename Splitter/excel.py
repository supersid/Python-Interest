import xlsxwriter 
# Insert an image with scaling.
import os, os.path

# simple version for working with CWD
DIR = './data'
#Found the number of files
num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(num)

workbook = xlsxwriter.Workbook('images.xlsx')
worksheet = workbook.add_worksheet()

# A will contain the coordinates of the images
a = []
length = (num/4) + 1
y = 'A D G J ' * int(length)
cols = y.split()
#print(cols)

files = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
fileNums =[]
for x in files:
    fileNums.append(int(x.split('.')[0]))
filesSorted = []
fileNums.sort()
for i in fileNums:
    filesSorted.append(str(i)+'.jpg')

j = 1
i=1
    
for name in filesSorted:
    x = cols[i-1]+str(j)
    print(x)
    fileName = './data/'+str(name)
    print(name)
    worksheet.insert_image(x,fileName, {'x_scale': 0.1, 'y_scale': 0.1})
    a.append(x)
    if(i%4==0 ):
        j+=3 
    i+=1
print(a)
text = open('listfile.txt','w')
text.writelines(str(a))
text.close()    
# Convert array a into a word document 
workbook.close()

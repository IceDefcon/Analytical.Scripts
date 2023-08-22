import os

custom = ['x','y']

#
# Clear Screen
#
os.system('cls') 
path = os.getcwd()

#
# Extracting Custom Entries
#

log = path + "/check.h"
if not os.path.exists(log): 
    print("\nMissing file: .../check.h")
    os.system('pause')
    exit()

file = open("check.h", "r")

lines = file.readlines() 
file.close()

line = 0
line_count = 0

for line in lines:
    if line != "\n":
        line_count += 1

CustomOutput   = open("!custom.h","w")

count = len(custom)

j = 1
x = 0
line = 0

for line in lines:

    precentage = 100*j/line_count
    format_precentage = "{:.2f}".format(precentage)

    progress = " [3] Extracting Custom Entries ---> Progress: " + str(format_precentage) + "%"
    print(progress, end='\r')
    i = 1
    data = line
    data_lower = data.lower()

    for x in range(count):
        index = data_lower.find(custom[x])
        
        if index != -1:
            if i == 1:
                CustomOutput.write(data)
                i = 0
    j = j + 1

CustomOutput.close()

print("\n [x] DONE \n")
os.system('pause')


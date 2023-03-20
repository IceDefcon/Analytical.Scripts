import os

custom = ['x','y']

#
# Clear Screen
#
os.system('cls') 
path = os.getcwd()

#
# Checking Everything
#

log = path + "/check.h"
if not os.path.exists(log): 
    print("\nMissing file: .../logs.h")
    os.system('pause')
    exit()

print(" [1] Reading logs.h")
file = open("check.h", "r")

lines = file.readlines() 
file.close()

lines = lines[15:-1]

line = 0
line_count = 0

for line in lines:
    if line != "\n":
        line_count += 1

print(" [2] Formating timestamp")
output = open("!check.everything.h","w")

for line in lines:

    i = 1
    data = line
    data_lower = data.lower()

    index = data_lower.find("")
    
    if index != -1:
        if i == 1:
            if data[-41:-40] == ":":
                formated = data[-43:-28] + " ---> " + data[0:-43] + "\n"
                output.write(formated)
            else:
                output.write(data)
            i = 0

output.close()

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

CustomOutput   = open("!check.custom.h","w")

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
                if data[-41:-40] == ":":
                    formated = data[-43:-28] + " ---> " + data[0:-43] + "\n"
                    CustomOutput.write(formated)
                else:
                    CustomOutput.write(data)
                i = 0
    j = j + 1

CustomOutput.close()

print("\n [x] DONE \n")
os.system('pause')

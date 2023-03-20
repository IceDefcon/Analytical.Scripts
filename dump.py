import os

suspected = ['x','y']

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
    print("\nMissing file: .../check.h")
    os.system('pause')
    exit()

print(" [1] Reading check.h")
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
# Extracting Suspected Entries
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

SuspectedOutput = open("!check.suspected.h","w")
SuspectedCount  = len(suspected)

i = 1
x = 0
y = 0
line = 0

for line in lines:

    precentage = 100*i/line_count
    format_precentage = "{:.2f}".format(precentage)

    progress = " [3] Extracting Suspected Entries ---> Progress: " + str(format_precentage) + "%"
    print(progress, end='\r')

    data = line
    data_lower = data.lower()

    for x in range(SuspectedCount):
        index_1 = data_lower.find(suspected[x])
        
        if index_1 != -1:
            if data[-41:-40] == ":":
                formated = data[-43:-28] + " ---> " + data[0:-43] + "\n"
                SuspectedOutput.write(formated)
                break
            else:
                SuspectedOutput.write(data)
                break

    i = i + 1

SuspectedOutput.close()

print("\n [x] DONE \n")
os.system('pause')

import os
import numpy as np
#
# Clear Screen
#
os.system('cls') 

#
# Get current path
#
path = os.getcwd()

#
# Map into AMC.number
#
def cpu_switch(arg): 
    switch = { 
        0: 11, 
        1: 22, 
        2: 33, 
        3: 44,
    } 
    return switch.get(arg) 

for UXM in range(5):
    for cpu in range(4):
        amc = cpu_switch(cpu)


def cpus_switch(arg): 
    cpu = { 
        0: "11",
        1: "22",
        2: "33",
        3: "44",
    } 
    return cpu.get(arg) 

# string
spu_string = ['' for i in range(2)] 

# file integer
cpu_file = [0 for i in range(2)]

# open files
for i in range(2):
    spu_string[i] = amc_switch(i)
    cpu_file[i] = open("cpu" + spu_string[i] + ".cpu.h","w")


os.system('pause')

# import packages

import numpy as np
import re

# define function to read text file

def transline(linestr):
    
    linestr = linestr.replace('no', '0')
    
    patternnum = r'[0-9]'
    patternlet = r'[a-z]'
    
    split1 = linestr.split(" bags contain ")
    key = split1[0]
    
    mapstr = split1[1]
    mapstr = list(filter(None,re.split(' bags, | bag, | bags.\n| bag.\n',mapstr)))
    
    mapdest = []
    
    for i in range(len(mapstr)):
        destnum = re.sub(patternlet,'',mapstr[i]).strip()
        destcol = re.sub(patternnum,'',mapstr[i]).strip()
        destvec = [int(destnum),destcol]
        mapdest.append(destvec)
        
    output = [key,mapdest]
    
    return(output)

# read text file into list

mappings = []

text = open("bagsmap.txt","r")
length = len(text.readlines())


for i in range(length):
    text = open("bagsmap.txt","r")
    line = text.readlines()[i]
    mappings.append(transline(line))


baglist = []

for i in range(len(mappings)):
    baglist.append(mappings[i][0])
   
# create mapping matrix

length = len(mappings)

mappingmat = np.zeros([length,length]).astype(int)

for i in range(length):
    
    mappingvec = mappings[i]
    mappingsnum = len(mappingvec[1])

    
    for j in range(mappingsnum):
        
        mappair = mappingvec[1][j]
        
        if mappair[1] == 'other':
            pass
        else:
            row = baglist.index(mappair[1])
            mappingmat[i,row] = mappair[0]
    
 # part 1
 
count = 0

length = len(baglist)

for i in range(length):
    
    init_vec = np.zeros(length).astype(int)
    zeros_vec = np.zeros(length).astype(int)
    init_vec[i] = 1


    while (np.array_equal(init_vec,zeros_vec) == False):
        init_vec = np.matmul(np.transpose(mappingmat),init_vec)
        if init_vec[357] != 0:
            count = count + 1
            break
        else:
            pass

                
print(count)


# part 2

init_vec = np.zeros(length).astype(int)
zeros_vec = np.zeros(length).astype(int)
init_vec[357] = 1


count = 0

while (np.array_equal(init_vec,zeros_vec) == False):
    init_vec = np.matmul(np.transpose(mappingmat),init_vec)
    count = count + sum(init_vec)


print(count)

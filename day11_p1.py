import numpy as np
import copy

input_vec = []

with open("day11input.txt","r") as f:
    for line in f:
        input_vec.append(list(line.rstrip()))
        
        
def mat_conv(mat):
    
    new_mat = []
    
    for i in range(len(mat)):
        
        newline = []
        line = mat[i]
        
        for j in range(len(line)):
            
            seat = line[j]
            
            if seat == 'L':
                x = 1
            elif seat == '#':
                x = 2
            else:
                x = 0
            
            newline.append(x)
            
        new_mat.append(newline)
        
    return(new_mat)
  
  
  
input_mat = mat_conv(input_vec)

size = np.shape(input_mat)

scribe_mat = np.zeros([size[0]+2,size[1]+2]).astype(int)
print(np.shape(scribe_mat))
scribe_mat[1:size[0]+1,1:size[1]+1] = input_mat
  
  
def surround_count(mat,row,col,target):
    surround_mat = copy.deepcopy(mat[row-1:row+2,col-1:col+2])
    surround_mat[1,1] = 0
    output = sum(sum(surround_mat == target))
    return(output)
  
  
def seat_pass(mat):
    
    length = np.shape(mat)
    new_mat = np.zeros([length[0],length[1]]).astype(int)
    
    for i in range(length[0]):
        
        for j in range(length[1]):
            
            seat_val = mat[i,j]
            
            if (seat_val == 0):
                pass
            elif (seat_val == 1):
                if (surround_count(mat,i,j,2) == 0):
                    new_mat[i,j] = 2
                else:
                    new_mat[i,j] = 1
            elif (seat_val == 2):
                if (surround_count(mat,i,j,2) > 3):
                    new_mat[i,j] = 1
                else:
                    new_mat[i,j] = 2
        
    return(new_mat)
                    
  
test_mat = copy.deepcopy(scribe_mat)
passed_mat = seat_pass(test_mat)

while (np.array_equal(test_mat,passed_mat) == False):
    
    test_mat = passed_mat
    passed_mat = seat_pass(test_mat) 
    
print(sum(sum(test_mat == 2))) 

# ROC Algorithm

#Importing the necessary libraries.
import pandas as pd 

#Writing the parts and machines matrix. The rows represent the machines and the columns represent the parts.
#1 means the part 3 needs to be processed by machine 1. 
#With this algorithm, we are trying to group the machine and parts.
data = [[0,0,1,0,0,0,1,0,1],
        [1,0,0,1,1,0,0,0,0],
        [0,0,1,0,0,0,1,0,1],
        [1,0,0,1,1,0,0,0,0],
        [1,0,0,1,1,0,0,0,0],
        [0,1,0,0,0,1,0,1,0],
        [0,0,1,0,0,0,1,0,1],
        [0,1,0,0,0,1,0,1,0]] 

#We create a while loop for necessary calculations.
i = 1
while i < 8:
    rv = [] #Row value
    rvc = [] #Row value copy
    rvi = [] #Row value indices 
    for i in range(len(data)): #Row calculations
        bv = 0 #Binary value (You can understand this better from the explanation file.)
        for j in range(len(data[0])): 
            pwr = len(data[0]) - j -1
            bv = bv + data[i][j]*(2**pwr)
        rv.append(bv)
        rvc.append(bv)
    rvc.sort()
    rvc.reverse()
    
    for i in range(len(rv)): #saving the indices 
        rvi.append(rv.index(rvc[i]) + 1)
        rv[rv.index(rvc[i])]=9999
    data_updated = []
    
    for i in range(len(data)):
        data_updated.append(data[rvi[i]-1]) 
    for i in range(len(data)):
        data[i] = data_updated[i]
    data_T = list(zip(*data)) #taking tranpose of the data

    #We are going to do the same calculations for the column values.
    cv = [] #column values
    cvc = [] #column values copy
    cvi = [] #column values indices
    
    for i in range(len(data_T)): #column calculations 
        bv = 0 #binary value
        for j in range(len(data_T[0])):
            pwr = len(data_T[0]) - j -1
            bv = bv + data_T[i][j]*(2**pwr)
        cv.append(bv)
        cvc.append(bv)
    cvc.sort()
    cvc.reverse()
    
    for i in range(len(cv)):
        cvi.append(cv.index(cvc[i]) + 1)
        cv[cv.index(cvc[i])]=9999
    data_T_updated = []
    for i in range(len(data_T)):
        data_T_updated.append(data_T[cvi[i]-1]) 
    for i in range(len(data_T)): 
        data_T[i] = data_T_updated[i]
        
    #Creating the data frame with the result we have found.
    final = pd.DataFrame(data_T, index=cvi, columns=rvi)
    final = final.transpose()
    print(final)

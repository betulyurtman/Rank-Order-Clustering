# ROC Algorithm

#Importing the necessary libraries.
import pandas as pd 

#Writing the parts and machines matrix. 
data = [[0,0,1,0,0,0,1,0,1],
        [1,0,0,1,1,0,0,0,0],
        [0,0,1,0,0,0,1,0,1],
        [1,0,0,1,1,0,0,0,0],
        [1,0,0,1,1,0,0,0,0],
        [0,1,0,0,0,1,0,1,0],
        [0,0,1,0,0,0,1,0,1],
        [0,1,0,0,0,1,0,1,0]] 
i = 1
while i < 8:
    rv = [] #row value
    rvc = [] #row value copy
    rvi = [] #row value indices 
    for i in range(len(data)): #row calculations
        bv = 0 #binary value
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
        
    final = pd.DataFrame(data_T, index=cvi, columns=rvi)
    final = final.transpose()
    print(final)
import numpy as np 
import copy


def gauss(parameters):
    a=np.array(eval(parameters[0]))
    b=np.array(eval(parameters[1]))

    arr=np.append(a,b,1)
    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]
    responseArr=[]
     
    diagonal=np.diagonal(arr)
    while 0 in diagonal:
        zeroIndex=diagonal.tolist().index(0)
        rowToChange=copy.deepcopy(arr[zeroIndex,:])
        rowToChange2=copy.deepcopy(arr[zeroIndex+1,:])

        arr[zeroIndex,:]=rowToChange2
        arr[zeroIndex+1,:]=rowToChange

        diagonal=np.diagonal(arr)

    responseArr.append("Stage:0--------------------------")
    responseArr.append(np.array2string(arr))


    for i in range(0,length-2):
        responseArr.append(("Stage: ",i+1,"--------------------------"))
        for j in range(i+1,height):
            multi=arr[j,i]/diagonal[i]
            currentRow=arr[j, :]
            previousRow=arr[i, :]
            #aplicamos la formula
            row=currentRow-(multi*previousRow)
            #rermplazamos la fila
            arr[j, :]=row
        responseArr.append(np.array2string(arr))

    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)
    responseArr.append("Answer Matrix--------------")
    responseArr.append(np.array2string(x))
    responseArr.append("Answer--------------------")
    responseArr.append(str(x[0]))
    
    return(responseArr)

'''
a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]
b=[1],[1],[1],[1]


response=gauss(a,b)

for item in response:
    print(item)
'''


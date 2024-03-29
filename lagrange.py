import numpy as np

def lagrange(parameters):
    try:
        x=np.array(eval(parameters[0]))
        y=np.array(eval(parameters[1]))
    except Exception as e:
        return ["Wrong Parameters Entered"]

    n=np.size(x)
    sizey=np.size(y)
    if sizey!=n:
        return ["Make sure x and y are the same size"]

    if n > len(set(x)):
        return ["There can not be repeated elements in x"]

    resultMatrix=[]
    resultMatrix.append("Lagrange Method------------------------------")
    polinome="p(x)= "

    for i in range (n):
        topPart=""
        bottomPart=1
        for j in range(n):
            if j==i:
                continue
            else:
                topPart=topPart+"(x-{})".format(x[j])
                bottomPart=bottomPart*(x[i]-(x[j]))
        li="L{}: {}/{}".format(i,topPart,bottomPart)
        polinome=polinome+"+{}(L{})".format(y[i],i)
        resultMatrix.append(li)

    resultMatrix.append("Lagrange Polinome------------------------")
    resultMatrix.append(polinome)
    return resultMatrix
''''
x="[-1,0,3,4]"
y="[15.5,3,8,1]"

result=lagrange([x,y])
for item in result:
    print(item)
'''

    

    



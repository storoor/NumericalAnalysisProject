import sympy

x = sympy.Symbol('x')
'''
xn =[-1,0,3,4]
fxn =[15.5,3,8,1]
'''
inequality =[]
functions =[]
result =[]
des = []

def createInequality(xn,fxn):
    for i in range(0,len(xn)-1):
        if(i < len(xn)):
            inequality.append(((xn[i],fxn[i]),(xn[i+1],fxn[i+1])))
    
    
def quadratic(parameters):
    try:
        xn=parameters[0]
        fxn=parameters[1]
    except Exception as e:
        return ["Wrong Parameters Entered"]

    n=len(xn)
    sizey=len(fxn)
    if sizey!=n:
        return ["Make sure x and y are the same size"]

    if n > len(set(xn)):
        return ["There can not be repeated elements in x"]
    for i in range(n-1):
        if xn[i]>xn[i+1]:
            return ["Error x are not in ascending order"]

    
    result=[]
    createInequality(xn,fxn) 
    superMatrix = [[0 for x in range(3*len(inequality)+1)] for y in range(3*len(inequality))] 
    for x in superMatrix:
        result.append(x)

    return result
    '''
    n = len(superMatrix)
    j = 0
    z = 0
    for i in inequality:
        auxj = str(z-j)
        superMatrix[j][z] = i[0][0]**2
        superMatrix[j][z+1] = i[0][0]
        superMatrix[j][z+2] = 1
        superMatrix[j][n] = i[0][1]
        superMatrix[j+1][z] = i[1][0]**2
        superMatrix[j+1][z+1] = i[1][0]
        superMatrix[j+1][z+2] = 1
        superMatrix[j+1][n] = i[1][1]
        z += 3
        j += 2
    k = j
    z = 0
    for i in range(0,len(inequality)-1):
        superMatrix[k][z] = 2*inequality[i][1][0]
        superMatrix[k][z+1] = 1
        superMatrix[k][z+3] = -2*inequality[i+1][0][0]
        superMatrix[k][z+4] = -1
        superMatrix[k][n] = 0
        k += 1
        z += 3
    superMatrix[k][0] = 1
    totalPivoting.a = superMatrix
    totalPivoting.n = len(superMatrix)
    totalPivoting.marcas = [i for i in range(0,totalPivoting.n)]
    aux = totalPivoting.elimination()
    j = 0
    for i in range(0,len(inequality)):
        func = aux[j]*x**2+aux[j+1]*x + aux[j+2]
        print(str(inequality[i][0][0])+" <= x <= "+str(inequality[i][1][0]))
        print(func)
        j += 3


xn =[-1,0,3,4]
fxn =[15.5,3,8,1]


quadratic([xn,fxn])
'''
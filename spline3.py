# Trazador cúbico natural
import numpy as np
import sympy as sym

def naturalCubicTracerl(xi,yi):
    n = len(xi)
    
    # h values
    h = np.zeros(n-1, dtype = float)
    for j in range(0,n-1,1):
        h[j] = xi[j+1] - xi[j]
    
    # Equation System
    A = np.zeros(shape=(n-2,n-2), dtype = float)
    B = np.zeros(n-2, dtype = float)
    S = np.zeros(n, dtype = float)
    A[0,0] = 2*(h[0]+h[1])
    A[0,1] = h[1]
    B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])
    for i in range(1,n-3,1):
        A[i,i-1] = h[i]
        A[i,i] = 2*(h[i]+h[i+1])
        A[i,i+1] = h[i+1]
        B[i] = 6*((yi[i+2]-yi[i+1])/h[i+1] - (yi[i+1]-yi[i])/h[i])
    A[n-3,n-4] = h[n-3]
    A[n-3,n-3] = 2*(h[n-3]+h[n-2])
    B[n-3] = 6*((yi[n-1]-yi[n-2])/h[n-2] - (yi[n-2]-yi[n-3])/h[n-3])
    
    # Solve Equation System
    r = np.linalg.solve(A,B)
    # S
    for j in range(1,n-1,1):
        S[j] = r[j-1]
    S[0] = 0
    S[n-1] = 0
    
    # Coeficients
    a = np.zeros(n-1, dtype = float)
    b = np.zeros(n-1, dtype = float)
    c = np.zeros(n-1, dtype = float)
    d = np.zeros(n-1, dtype = float)
    for j in range(0,n-1,1):
        a[j] = (S[j+1]-S[j])/(6*h[j])
        b[j] = S[j]/2
        c[j] = (yi[j+1]-yi[j])/h[j] - (2*h[j]*S[j]+h[j]*S[j+1])/6
        d[j] = yi[j]
    
    # Tracing Polinome
    x = sym.Symbol('x')
    polinomio = []
    for j in range(0,n-1,1):
        ptramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2 + c[j]*(x-xi[j])+ d[j]
        ptramo = ptramo.expand()
        polinomio.append(ptramo)
    
    return(polinomio)

# Test Program
# Test Data
def spline3(parameters):
    try:
        xi = np.array(eval(parameters[0]))
        fi = np.array(eval(parameters[1]))
    except Exception as e:
        return ["Wrong Parameters Entered"]

    n=np.size(xi)
    sizey=np.size(fi)
    if sizey!=n:
        return ["Make sure x and y are the same size"]

    if n > len(set(xi)):
        return ["There can not be repeated elements in x"]

    for i in range(n-1):
        if xi[i]>xi[i+1]:
            return ["Error x are not in ascending order"]
    resolucion = 10 # between each pair of points
    responseArray=[]
    # Procedure
    n = len(xi)
    # obtains the polinome by traces
    polinomio = naturalCubicTracerl(xi,fi)

    # out
    responseArray.append('Polinome by Traces: ')
    for tramo in range(1,n,1):
        responseArray.append(' x = ['+str(xi[tramo-1])+','+str(xi[tramo])+']')
        responseArray.append(str(polinomio[tramo-1]))
    
    return responseArray
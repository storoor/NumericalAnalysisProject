from IncrementalSearch import incrementalSearch
from Biseccion import bisection
from FalsePosition import falsePosition
from Newton import newton
from Punto_Fijo import Punto_Fijo
from SecantMethod import secantMethod
from MultipleRoots import multipleRoots
from gaussianElinimination import gauss 
from parcialPivoting import parcialPivoting
from gaussPivTotal import eliminacion_gaussiana_pivoteo
from jacobi import jacobi
from seidel import seidel
from sor import sor
from vandermondeInterpolacion import vandermonde
from newton_interpolacion import newtonInterpolation
from spline1 import spline1
from spline3 import spline3


numericalMethods={
    "incrementalSearch":incrementalSearch,
    "bisection":bisection,
    "falsePosition":falsePosition,
    "newton":newton,
    "staticPoint":Punto_Fijo,
    "secant":secantMethod,
    "multipleRoots":multipleRoots,
    "gaussianElimination":gauss,
    "parcialPivoting":parcialPivoting,
    "totalPivoting":eliminacion_gaussiana_pivoteo,
    "jacobi":jacobi,
    "gauss-seidel":seidel,
    "sor":sor,
    "vandermonde":vandermonde,
    "newtonInterpolation":newtonInterpolation,
    "spline1":spline1,
    "spline3":spline3

}

def getMethod(key,parameters):
    return numericalMethods[key](parameters)
from sympy import *

x = Symbol('x')

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

result = solve(x+a,x)
print(result)
import sympy

w1,w2, x,y,z = sympy.symbols("w1 w2 x y z")



z = w1 + 15
w = 4
z *= 26
z += w2 + 10

print(z)
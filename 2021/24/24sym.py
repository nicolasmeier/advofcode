import sympy

x,y,z = sympy.symbols("x y z")
w01,w02,w03,w04,w05,w06,w07,w08,w09,w10,w11,w12,w13,w14 = sympy.symbols("w01,w02,w03,w04,w05,w06,w07,w08,w09,w10,w11,w12,w13,w14")

x *= 0
x +=  z
x = x %  26
z /=1
x +=  15
if x != w01:
    x = 1
else:
    x = 0
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w01
y +=  15
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=1
x +=  15
x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w02
y +=  10
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=1
x +=  12
x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w03
y +=  2
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=1
x +=  13
x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w04
y +=  16
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -12
p = sympy.Piecewise((0,x == w05),(1,True))
x = p.subs(x,x)
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w05
y +=  12
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=1
x +=  10
x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w06
y +=  11
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -9
if x == w07:
    x = 0
else:
    x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w07
y +=  5
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=1
x +=  14
x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w08
y +=  16
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=1
x +=  13
x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w09
y +=  6
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -14
if x == w10:
    x = 0
else:
    x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w10
y +=  15
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -11
if x == w11:
    x = 0
else:
    x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w11
y +=  3
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -2
if x == w12:
    x = 0
else:
    x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w12
y +=  12
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -16
if x == w13:
    x = 0
else:
    x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w13
y +=  10
y *= x
z +=  y
x *= 0
x +=  z
x = x %  26
z /=26
x +=  -14
if x == w14:
    x = 0
else:
    x = 1
y *= 0
y +=  25
y *= x
y +=  1
z *= y
y *= 0
y +=  w14
y +=  13
y *= x
z +=  y

print(z)
import math
a1 = divmod(5, 2)
a2 = (5 // 2, 5 % 2)
print(a1, type(a1), a2, type(a2))
b1 = divmod(-5.5, 2.1)
b2 = (math.floor(-5.5/2.1), -5.5 % 2.1)
print(b1, type(b1), b2, type(b2))
c1 = divmod(5.5, -2.1)
c2 = (math.floor(5.5/-2.1), 5.5 % -2.1)
print(c1, type(c1), c2, type(c2))

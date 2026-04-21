import MOD as mymodule

print(mymodule.add(5,3))

from MOD import sub
print(sub(10,4))

from MOD import mul as m
print(m(4,5))

from MOD import *
print(div(20,5))
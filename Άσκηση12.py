import math
import decimal
from decimal import *

decimal.getcontext().prec = 10000
check = True
decimal.getcontext().prec = 10000
a = float(input("INPUT NUMBERS||ZERO TO END:"))
listnum = []
while a != 0:
    listnum.append(a)
    a = float(input())
print(listnum)
n = int(len(listnum))
x = 0
i = 0
for i in range(0, n):
    if i == 0:
        x = decimal.Decimal(listnum[0])
    else:
        x = math.pow(x, decimal.Decimal(listnum[i]))

listdigit = list(map(str, (str(x))))
print(x)
v = len(listdigit)
for i in range(0, v):
    if listdigit[i] == ".":
        check = False
if check == False:
    print(listdigit[v - 1])
else:
    print("0")

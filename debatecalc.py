from read import read
from ldcalc import ldcalc
deblist = read("debaters.txt")
res = ldcalc(deblist)
for r in res:
    print(r[0].name,":",r[1].name)

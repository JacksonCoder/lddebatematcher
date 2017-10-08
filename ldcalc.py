from debater import Debater
def ldcalc(debatees):
    if debatees is  None:
        return []
    if len(debatees) == 0:
        return []
    #sort debatees (enjoy)
    debwsorted = sorted([d.wins for d in debatees])
    tops = debwsorted[len(debwsorted)-1]
    debsorted = sorted(debatees,key=lambda x: x.wins * 1000 + x.sp)
    byedeb = None
    if len(debsorted) % 2 != 0:
        byedeb = debsorted[0]
        debsorted = debsorted[1:]
    debpairs = [[debsorted[i],debsorted[i+1]] for i in range(0,len(debsorted),2)]
    if byedeb is not None:
        debpairs += [[Debater(0,0,0,"BYE"),byedeb]]
    return debpairs

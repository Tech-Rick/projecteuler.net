#<p>Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:</p>
#<table><tr><td>Triangle</td>
#<td> </td>
#<td>$T_n=n(n+1)/2$</td>
#<td> </td>
#<td>$1, 3, 6, 10, 15, \dots$</td>
#</tr><tr><td>Pentagonal</td>
#<td> </td>
#<td>$P_n=n(3n - 1)/2$</td>
#<td> </td>
#<td>$1, 5, 12, 22, 35, \dots$</td>
#</tr><tr><td>Hexagonal</td>
#<td> </td>
#<td>$H_n=n(2n - 1)$</td>
#<td> </td>
#<td>$1, 6, 15, 28, 45, \dots$</td>
#</tr></table><p>It can be verified that $T_{285} = P_{165} = H_{143} = 40755$.</p>
#<p>Find the next triangle number that is also pentagonal and hexagonal.</p>
 

def getTriangle(n):
    return int((n*(n+1))/2)

def isPentagonal(p):
    if p < 1:
        return False
    n = (1+((1+24*p)**0.5))/6
    return n%1 == 0

def isHexagonal(h):
    if h < 1:
        return False
    n = (1+((1+8*h)**0.5))/4
    return n%1 == 0

n = 285
while True:
    n += 1
    Tn = getTriangle(n)
    if isPentagonal(Tn) and isHexagonal(Tn):
        print(f"next Tn is T({n}) = {Tn}")
        break
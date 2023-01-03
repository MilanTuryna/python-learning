import math

# možné trojúhelníky: ABC,ABD,ACD,BCD
# vzdalenost: |AB| = sqrt( (b1 - a1)**2 + (b2 - a2)**2  )
def isTriangle(sides):
    smallest,medium,biggest = sorted(sides)
    return smallest+medium>=biggest and all(s>0 for s in sides)

def length(a, b):
    widthPoint = (b[0] - a[0])^2
    heightPoint = (b[1] - a[1])^2
    sum = abs(widthPoint + heightPoint)
    return math.sqrt(sum)

def getArea(a,b,c):
    if not isTriangle([length(a, b), length(b,c), length(a,c)]): return 0
    area=0.5*( (a[0]*(b[1]-c[1])) + (b[0]*(c[1]-a[1])) + (c[0]*(a[1]-b[1])) )
    return area


def get_triangle(a, b, c, d):
    abc = getArea(a,b,c)
    abd = getArea(a,b,d)
    acd = getArea(a,c,d)
    bcd = getArea(b,c,d)

    triangles = {
        "abc": abc,
        "abd": abd,
        "acd": acd,
        "bcd": bcd
    }

    badTriangleCounter = 0
    for val in triangles.values():
        if(val == 0): badTriangleCounter += 1
    if(badTriangleCounter == 4):
        return False

    biggest = max(triangles, key=triangles.get)
    sides = {
        "abc": (a,b,c),
        "abd": (a,b,d),
        "acd": (a,c,d),
        "bcd": (b,c,d)
    }
    return sides[biggest]
    
print(
    get_triangle((1, 1), (3, 1), (2, 3), (2, 2))
)

print(
    get_triangle((0, 0), (-10, 0), (-2, -2), (0, -5))
)

# nefunkční kontrola, zda trojúhelník existuje, nedokázal jsem to aplikovat správně

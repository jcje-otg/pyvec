def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

v1 = (1,2)
v2 = (3,4)

v3 = add(v1,v2)
v4 = sub(v1,v2)

print(v3)
print(v4)

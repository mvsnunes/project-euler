# declaring variables
a = 0
b = 0
c = 0
sum = 1000

# changing a and b to calculate c and check if is a Pythagorean triplet
for a in range(1, int(sum/3)):
    for b in range(a+1, int(sum/2)):
        c = sum-a-b
        if(a**2+b**2-c**2 == 0):
            print("The product abc is", a*b*c)

#function to calculate gcd between two numbers
def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)

#declaring variables
lcm=1

#loop to calculate lcm of various numbers
for i in range(2,21):
    lcm=((lcm)*(i))/gcd(lcm,i)

#display the result
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is ", lcm)

# check if a number is prime
def isprime(i):
    j = 1
    div = 0
    prime = False
    while j <= int(i**0.5):
        if (i % j == 0):
            div += 1
        j += 1
    if div == 1:
        prime = True
    else:
        prime = False
    return prime


# declaring variables
countprime = 0
num = 1
# loop to count if a prime number is found
while(1):
    if (isprime(num) == True):
        countprime += 1
    if(countprime == 10001):
        break
    num += 2

# display the result
print(num)

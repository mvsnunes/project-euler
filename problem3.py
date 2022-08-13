# declaring variables
num = 600851475143
i = 1
j = 1
div = 0
prime = 0

# loop to decompose a number in prime factors
while num != 1:
    # loop to check if a number is prime
    while j <= i:
        if (i % j == 0):
            div += 1
        j += 1
    if div == 2:
        prime = i
        # check if the prime is a factor of the number
        if num % prime == 0:
            num = num/prime
    i += 1
    j = 1
    div = 0
# display the result
print("The largest prime factor of the number 600851475143 is:", prime)

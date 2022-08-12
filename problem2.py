# declaring variables
numaux = 0
numaux1 = 1
num = 0
lastnum = 4000000
sum = 0

# compute fibonacci sequence
while num < lastnum:

    num = numaux1+numaux
    numaux = numaux1
    numaux1 = num

    # sum of even numbers
    if num % 2 == 0:
        sum = sum+num

# display the sum
print("The sum of the even numbers in the Fibonacci sequence is:", sum)

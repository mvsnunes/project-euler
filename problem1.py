# declaring variables
num2count = 1000
i = 1
sum = 0

# loop to calculate the sum
while i < num2count:
    # condition of sum
    if (i % 3 == 0 and i % 5 != 0) or (i % 5 == 0 and i % 3 != 0) or (i % 5 == 0 and i % 3 == 0):
        sum = sum+i
    i += 1
# display the sum
print("The sum of all the multiples of 3 or 5 below 1000 is", sum)

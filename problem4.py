# declaring variables
firstnum = 0
secondnum = 0
reverse = 0
num = 0
largep = 0

# loops to perform the multiplication between two numbers of thre digits
for firstnum in range(100, 1000):
    for secondnum in range(100, 1000):
        num = firstnum*secondnum
        numaux = num
        reverse = 0
        # loop to reverse a number
        while(numaux > 0):
            lastdig = numaux % 10
            reverse = (reverse*10)+lastdig
            numaux = numaux//10
        # check if the number is palindrome
        if num == reverse:
            # largest palindrome
            if num > largep:
                largep = num


# display the result
print("The largest palindrome made from the product of two 3-digit numbers:", largep)

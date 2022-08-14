
soma = 0
soma2 = 0

for i in range(1, 101):
    soma += i
    soma2 += i**2

result = soma**2-soma2

print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is", result)

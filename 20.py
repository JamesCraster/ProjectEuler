def factorial(n):
    product = 1
    for x in range(1,n+1):
        product *= x
    return product

x = str(factorial(100))
summation = 0
for y in x:
    summation += int(y)

n = 0
List = []
while n < 1000:
    if n % 3 == 0:
        List.append(n)
        n = n+1
    elif n % 5 == 0:
        List.append(n)
        n = n+1
    else:
        n = n+1

print (List)
m = 0
sum = 0
while m < len(List):
    sum = sum + List[m]
    m = m+1
print(sum)

#233168

            

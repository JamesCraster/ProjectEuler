n = 2
m = 1
List = [1,2]
while m <=4000000:
    m = List[n-1] + List[n-2]
    List.append(m)
    n = n+1

m = 0
sum = 0
while m < len(List):
    if List[m] % 2 ==0:
        sum = sum + List[m]
    m = m+1

print(sum)
    

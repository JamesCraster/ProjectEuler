f = open("13.txt",'r')
sumList = [['']]
for x in f.read():
   if x == '\n':
      sumList.append([''])
      continue
   if x == " ":
      continue
   sumList[-1][0] += x
summation = 0
for x in range(0,len(sumList)):
   sumList[x][0] = int(sumList[x][0][0:11])
   summation += sumList[x][0]

print(str(summation)[:10])
#answer is 5537376230



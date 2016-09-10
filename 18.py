file = open('18.txt','r')
string = ""
for z in file.read():
   if  z == '\t':
      continue
   else:
      string += z

L = [[]]
x = 0
while x < len(string):
   if string[x] == '\n':
      L.append([])
      x += 1
   
   elif string[x] == " ":
      x += 1
      continue
 
   else:
      if x + 1 < len(string):
         if string[x + 1] == " ":
            L[-1].append(int(string[x]))
            x += 2
    
         else:
            L[-1].append(int(string[x] + string[x+1]))
            x += 2

def sumPath(L,binaryList):
   row = 0
   column = 0
   summation = L[row][column]
   for x in binaryList:
      row += 1
      if x == 1:
         column += 1
      summation += L[row][column]

   return summation

#there are 14 rows
binaryString = ""
counter = 0
maxSum = 0
B = []
temporarySum = 0
while bin(counter) < '0b11111111111111':
   B = []
   binaryString = ""
   binaryString += str(bin(counter))[2:]
   while len(binaryString) < 14:
             binaryString = "0" + binaryString
   for x in binaryString:
      B.append(int(x))
      
      
   temporarySum = sumPath(L,B)
   if maxSum < temporarySum:
      maxSum = temporarySum
   counter += 1
   
   
   
##1074


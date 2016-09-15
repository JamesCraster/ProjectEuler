d = {0:"",1:"one",2:"two",3:"three",
     4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
     10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
     16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
     20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",
     80:"eighty",90:"ninety"}

Result = ""
for n in range(1,1001):
    m = str(n)

    Length = len(m)
    if Length == 4:
        Result += "onethousand"
    
    if Length == 3:
        Result += d[int(m[0])]+"hundred"
        if int(m[1]) +int(m[2]) != 0:
            Result += "and"
        if d[int(m[1]+'0')] != "ten":
            Result += d[int(m[1]+'0')]
            Result += d[int(m[2])]
        else:
            Result += d[int(m[1:])]
    
    
    if Length == 2:
        
        if d[int(m[0]+'0')] != "ten":
            Result += d[int(m[0]+'0')]
            Result += d[int(m[1])]
            
            
        else:
            Result += d[int(m[0:])]

    if Length == 1:
        Result += d[int(m[0])]


print(Result)
print(len(Result))

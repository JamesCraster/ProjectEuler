for a in range(1,1001):
   for b in range(a,1001-a):
      for c in range(b, 1001-b):
         if a + b + c == 1000 and a**2 + b **2 == c ** 2:
            print(a * b * c)

##answer is 31875000

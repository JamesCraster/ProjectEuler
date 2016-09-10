def checkPalindrome(n):
   length = len(str(n))
   if(length % 2 != 0):
      for x in range(0,length//2):
         if(str(n)[x] != str(n)[(length-x)-1]):
            return False

      return True
   else:
      for x in range(0,length//2):
         if(str(n)[x] != str(n)[(length-x)-1]):
            return False

      return True

largestPalindrome = 0
for x in range(100,999):
   for y in range(100,999):
      if checkPalindrome(x*y) :
         if y*x > largestPalindrome:
            largestPalindrome = y*x

         
            

def gcd(x, y):
   if (x < y):
     gcd (y, x)
   else:
     if (y == 0):
       return x
     else:
       return gcd(y, x % y)

print(gcd(60, 24))
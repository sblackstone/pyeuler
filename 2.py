

a = 0
b = 1
x = 0
s = 0

while b < 4000000:
  x = a + b
  if (x % 2 == 0):
      s += x
  a = b
  b = x
  

print s
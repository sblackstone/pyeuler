v = 600851475143

range_end = int(v**(0.5))


a = range(0,range_end)
i = 2

max_val = 0

while i < range_end:
    if a[i] is None:
      i += 1
      continue

    if v % a[i] == 0:
      max_val = a[i]

    for j in range(a[i]*2, range_end, a[i]):
      a[j] = None

    
    i += 1
    
print max_val

max_val = 0


for a in range(100,1000):
  for b in range(a,1000):
    v = a*b
    c = str(v)
    if c == c[::-1] and v > max_val:
      max_val = v

print max_val
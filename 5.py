ans = 1
for p in [2,3,5,7,11,13,17,19]:
    v = p
    while v*p < 20:
        v *= p
    ans *= v

print ans


import time

t1 = time.time()
l = [i**2 for i in range(10000000)] # approx 3.190259933471680 sec
print('{:.15f} sec'.format(time.time() - t1))

t2 = time.time()
g = (i**2 for i in range(10000000)) # approx 0.000023841857910 sec
print('{:.15f} sec'.format(time.time() - t2))
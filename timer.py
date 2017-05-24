import time

t0 = time.time()

for i in range(999999999):
    print(i)

t1 = time.time()
print(t1 - t0)

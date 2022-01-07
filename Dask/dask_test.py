from dask.distributed import Client

import time
from time import sleep

#client = Client(n_workers=4)


def inc(x):
    sleep(1)
    return x + 1

def add(x, y, a, b):
    sleep(1)
    return x + y + a + b

start_time = time.time()

x = inc(1)
y = inc(2)
a = inc(1)
b = inc(2)

z = add(x, y, a, b)


print("Normal Computation : %s seconds ---" % (time.time() - start_time))


from dask import delayed

start_time = time.time()

x = delayed(inc)(1)
y = delayed(inc)(2)
a = delayed(inc)(1)
b = delayed(inc)(2)

z = delayed(add)(x, y, a ,b)

z.compute()

print("Dask Accelerated Computation :  %s seconds ---" % (time.time() - start_time))
#client.close()
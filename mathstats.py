import mincemeat
import time
import sys

stime= time.time()
file = open(str(sys.argv[1]),'r')
data = list(file)
file.close()
datasource = dict(enumerate(data))

# mapper function
def mapfn(k, v):
    for w in v.split():
        yield 'values',float(w)
# reducer function
def reducefn(k, vs):
    
    import math
    count=len(vs)
    addition=sum(vs)
    mean = addition/count
    sum_of_sq=0
    for n in vs:
        sum_of_sq=sum_of_sq+(mean-n)*(mean-n)
        sum_of_sq_over_count = sum_of_sq/count
    return [count,addition,math.sqrt(sum_of_sq_over_count)]

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

answers = s.run_server(password="changeme")
print("Count of all the numbers is %s." % answers['values'][0])
print("Sum of all the numbers is %s." % answers['values'][1])
print("Standard Deviation is %s." % answers['values'][2])
print("Total Execution Time is %s seconds." % (time.time() - stime))

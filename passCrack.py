import mincemeat, sys, md5, hashlib, time, itertools
stime=time.time()
input = sys.argv[1]
def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

allowed=list("abcdefghijklmnopqrstuvwxyz0123456789");
datalist=[]

for i in range(1,5):
 for j in list(itertools.product(allowed, repeat=i)):
   datalist.append(''.join(j))

# Break the list
data=list(chunks(datalist, 10000))

for i in data:
  i.insert(0,input)

datasource = dict(enumerate(data))

# mapper function
def mapfn(k, v):
    import md5, hashlib
    list=[]
    input=v[0]
    for i in v:
      if(hashlib.md5(i).hexdigest()[:5]==input):
       list.append(i)
    yield 'Result', list

# reducer function
def reducefn(k, vs):
  result=[]
  for i in vs:
    if len(i)!=0:
      for j in i:
        result.append(j)
  return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

answers = s.run_server(password="changeme")
print answers
print("Execution time is %s seconds." % (time.time() - stime))

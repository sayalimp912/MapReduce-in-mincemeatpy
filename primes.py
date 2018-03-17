import mincemeat
import time

stime=time.time()
data=range(0,1000);
datasource = dict(enumerate(data))

def mapfn(k, v):
    list=[]
    def isPrimeNumber(num):
        if num < 2 or num%2 == 0 and num!=2:
            return False
        if num == 2:
            return True
        else:
            for x in range(3, int(num**0.5)+1, 2):
                if num%x == 0:
                    return False
            return True
    def isPalindrome(x):
        num = str(x)[::-1]
        return str(x) == num
    
    for i in range(v*10000,(v+1)*10000):
        if isPrimeNumber(i) and isPalindrome(i):
            list.append(i) 
    yield 'numbers',list

def reducefn(k, vs):
    list=[]
    for i in vs:
        list.extend(i)
    return list

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

answers = s.run_server(password="changeme")
print answers
print len(answers['numbers'])
print("Execution time is %s seconds." % (time.time() - stime))

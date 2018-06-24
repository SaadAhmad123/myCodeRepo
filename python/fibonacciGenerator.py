'''
    This is a fibonacci generator function.
    It employs the yeild keyword
'''

def genFib():
    n1 = 1;
    n2 = 0;
    while True:
        next = n1 + n2;
        yield next;
        n2 = n1;
        n1 = next;
    #end
#end

f = genFib();
for i in range(0,10000):
    print f.next();
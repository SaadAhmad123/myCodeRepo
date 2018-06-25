import  random;
# This function generate the power set 
# in the uasual way.
# THIS IS A GENERATOR FUNCTION.
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:    #more generally i//(2**j) % 2 == 1
                combo.append(items[j])
            #end
        #end
        yield combo
    #end
#end


# This function yeilds a list of subset of the
# elements in the given list such that the subset
# is not in other lists
# N is the number of bags of subsets. 
# By default N = 1 and it is equal to the
# simple powerSet() function
'''
    Example:
    
    gen = generalPowerSet(['bear', 'penguin'],2)
    for item in gen:
        print(item)

    results in:

    ([], [])
    (['bear'], [])
    ([], ['bear'])
    (['penguin'], [])
    (['bear', 'penguin'], [])
    (['penguin'], ['bear'])
    ([], ['penguin'])
    (['bear'], ['penguin'])
    ([], ['bear', 'penguin'])

    The complexity becomes = O((N+1)^n)
'''
def generalPowerSet(list):
    n = len(list)
    order = 3
    for i in range(order**n):
        combo = [];
        s = [];
        for c in range(0,order-1):
            combo.append([]);
            s.append("");
        #end_for
        for j in range(n):
            for c in range(1,order):
                exp = i//((order)**j) % (c+1);
                #print "<" + str(c+1) + "," + str(i) + "," + str(j) + "," + str(exp) + "," + str(exp == c)  + ">";
                if exp == c:
                    combo[c-1].append(list[j]);
                    s[c-1] = s[c-1] + list[j].__str__();
                    break;
            #end_for
        #end_for
        yield tuple(s);
    #end_for
#end


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'
            

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]


def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]                                      


items = buildRandomItems(1)
for i in generalPowerSet(items):
    print i
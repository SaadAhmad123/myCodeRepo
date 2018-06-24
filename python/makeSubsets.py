'''
This code is inspired from the MIT course on edx (6.00.2x)
This code generates all the subsets of a given array of
objects in complexity of O(n^2). 
- makeSubsets_i in iterative implementation
- makeSubsets_r in recursive implementation

=>  makeSubset(list, implementation = "i"/"r") is the
    higher level implementation

usage: 
list_of_subsets = makeSubsets(array);

Check:
    On 1.9 GHz, Ubuntu 18, 4GB RAM, Dell Laptop.
    don't go beyond 22 element in the list.
'''

def makeSubsets(list, implementation="i"):
    '''
        returns a list of all the subsets in the 
        given list. Select the implementation to
        be either iterative("i") or recursive("r").
        By defualt the implementation is iterative.
    '''
    if implementation == "i":
        return makeSubsets_i(list);
    elif implementation == "r":
        return makeSubsets_r(list);
    else:
        return makeSubsets_i(list);
#end



def makeSubsets_i(list):
    subsets = [[]];
    for i in range(0,len(list)):
        newSubset = [];
        for partialSubset in subsets:
            newSubset.append(partialSubset[:] + [list[i]]);
        #end_for
        subsets = subsets + newSubset;
    #end_for
    return subsets;
#end


def makeSubsets_r(list):
    if len(list) == 0:
        return [[]];    #return the empty set as base case
    #end_if
    subsets = [];
    firstElement = list[0];
    otherElement = list[1:];
    for partialSubset in makeSubsets_r(otherElement):
        subsets.append(partialSubset);
        subsets.append(partialSubset[:] + [firstElement]);
    #end_for 
    return subsets;
#end


makeSubsets(range(0,21), "r");
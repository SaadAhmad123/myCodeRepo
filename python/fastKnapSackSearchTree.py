'''
    This function implements the memoization
    approach in the searchTree algorithm in
    knapSackSearchTree.py

    To use the implementation below the list should be 
        a list of objects with following functions.
        - getValue()  ----->    this function will be maximized for all the elements in the list
        - getCost()   ----->    this function will contribute toward the constraint.
        

'''

def fastSearchBestCombination(list, avail, memo = {}):
    result = None;
    if (len(list), avail) in memo:
        return memo[(len(list), avail)];
    elif list == [] or avail == 0:
        result = (0, []);
    elif list[0].getCost() > avail:
        result = fastSearchBestCombination(list[1:], avail, memo);
    else:
        fItm = list[0];
        others = list[1:];
        # with fItm
        (bestValue1, bestCombination1) = fastSearchBestCombination(others, avail - fItm.getCost(), memo);
        bestValue1 = bestValue1 + fItm.getValue();
        # without fItm
        (bestValue0, bestCombination0) = fastSearchBestCombination(others, avail, memo);
        if bestValue1 > bestValue0:
            result = (bestValue1, bestCombination1 + [fItm]);
        else:
            result = (bestValue0, bestCombination0);
    memo[(len(list), avail)] = result;
    return result;
#end
'''
    This is code is inspired from the MIT edx course (6.00.2x)
    This algorithm implements the binary search tree to solve
    the knapsack problem. The complexity of it is O(2^(i+1))

    To use the implementation below the list should be 
    a list of objects with following functions.
    - getValue()  ----->    this function will be maximized for all the elements in the list
    - getCost()   ----->    this function will contribute toward the constraint.
    
    use:
        (bestValue, [listOfBestCombination]) = searchBest(list, constraint)

    NOTE:
            constraint is just a number
'''

def searchBestCombination(list, constraint):
    if len(list) == 0 or constraint == 0:
        return (0, []);
    elif list[0].getCost() > constraint:    # don't consider the item is constraint breaks.
        return searchBestCombination(list[1:], constraint);
    else:
        focusItem = list[0];
        # if item is included
        (bestValue1, bestCombination1) = searchBestCombination(list[1:], constraint - focusItem.getCost());
        bestValue1 = bestValue1 + focusItem.getValue();
        #if item is not included
        (bestValue0, bestCombination0) = searchBestCombination(list[1:], constraint);
        if bestValue1 > bestValue0:
            return (bestValue1, bestCombination1 + [focusItem]);
        else:
            return (bestValue0, bestCombination0);
#end

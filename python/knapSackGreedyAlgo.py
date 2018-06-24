'''
 	The greedy algorithm follows the algorithm:

	while knapsack is not full
		add the "best" possible element to it. 

    To use the implementation below the list should be 
    a list of objects with following functions.
    - getValue()  ----->    this function will be maximized for all the elements in the list
    - getCost()   ----->    this function will contribute toward the constraint.
    
    use:
        (bestValue, [listOfBestCombination]) = greedy(list, constraint, keyFunction)

    NOTE: 
            Constraint is just a number
'''
#	This function apply the desired key function
#	on the menu in a greedy manner. The key 
#	function maps the elements from best to 
#	the worst. (best and worst are determined
#	by some metric like best element with
#	the highest mass is the best, etc)
def greedy(list, constraint, keyFunction):
	menu = list;
	maxCost = constraint;
    sortedMenu = sorted(menu, key=keyFunction, reverse=True);  # complexity O(NlogN)
	#search for the item which satisfy the constraint (maxCost)
	bestResult = [];
	totalCost, totalValue = 0.0, 0.0;
	for i in sortedMenu:
		if(totalCost + i.getCost() <= maxCost):
			bestResult.append(i);
			totalCost = totalCost + i.getCost();
			totalValue = totalValue + i.getValue();
	#end
	return (totalValue, bestResult);
#end


###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


class Cow(object):
    def __init__(self, name, cost):
        self.name = name;
        self.cost = cost;
    
    def getValue(self):
        return 1;
    
    def getCost(self):
        return self.cost;
    
    def getName(self):
        return self.name;

    def __str__(self):
        return "<" + self.name + ", " + str(self.cost) + ">"; 

def makeCowsList(cows):
    cowsList = [];
    for cow in cows:
        name = cow;
        cost = cows[cow];
        cowsList.append(Cow(name, cost));
    return cowsList;


def greedy(list, constraint, keyFunction):
    	menu = list;
	sortedMenu = sorted(menu, key=keyFunction, reverse=True)
	maxCost = constraint;
    
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



# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    tripsList = [];
    while len(cows) > 0:
        (value, tripCows) = greedy(cows, limit, lambda x : x.getCost());
        cowsInTrip = [];
        for cow in tripCows:
            cowsInTrip.append(cow.getName());
            cows.remove(cow);
        tripsList.append(cowsInTrip);
    print tripsList;

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    print cows;
    # getting valid partitions
    validPartitions = [];
    for partition in get_partitions(cows):
        isValidPartition = True;
        for trip in partition:
            sum = 0;
            for cow in trip:
                sum += cow.getCost();
            if sum > limit: 
                isValidPartition = False;
                break;
        if isValidPartition:
            validPartitions.append(partition);
    
    # out of valid partitions getting the best partition according to
    # the given constraint. 
    minTrips = 10000000;
    minTripsPartition = [];
    for trips in validPartitions:
        if len(trips) < minTrips:
            minTrips = len(trips);
            minTripsPartition = trips;
    
    # representing the solution in the required formate
    namedCowsTrips = [];
    for trip in minTripsPartition:
        nctrip = [];
        for cow in trip:
            nctrip.append(cow.getName());
        namedCowsTrips.append(nctrip);
    
    print namedCowsTrips;

    pass

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cowsText = load_cows("ps1_cow_data.txt")
limit=10
cows = makeCowsList(cowsText);

(greedy_cow_transport(cows, limit))
cows = makeCowsList(cowsText);
(brute_force_cow_transport(cows, limit))



'''
    This is the demo of a random walk algorithm.
    The algorithm is based on the a drunk and we
    want to know that in a 2D space after N steps
    where would it be.
    ---------------------------------------------
    There are three abstraction in it.
    1. Location : place
    2. Drunk : random walker
    3. Field : collection of drunk and location (maps : drunk -> location)
'''

'''
    Note :- 
        The location can be in any diamension.
'''
class Location(object):
    def __init__(self, x, y):
        '''x and y are floats'''
        self.x = x;
        self.y = y;
    
    def move(self, deltaX, deltaY):
        '''deltaX and deltaY are floats'''
        return Location(self.x + deltaX, self.y + deltaY);

    def distanceFrom(self, otherLocation):
        dX = self.x - otherLocation.getX();
        dY = self.y - otherLocation.getY();
        return (dX*dX + dY*dY) ** 0.5;
    
    def getX(self):
        return self.x;
    
    def getY(self):
        return self.y;

#end_class


'''
    Location of the drunk in the field an attribute of
    the field rather than the attribute of the drunk.
'''
class Field(object):
    def __init__(self):
        self.drunks = {};
    
    def addDrunk(self, drunk, location):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk");
        else:
            self.drunks[drunk] = location;
        
    def getLocation(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field");
        else:
            return self.drunks[drunk];

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field");
        xDist, yDist = drunk.takeStep();
        currentLocation = self.drunks[drunk];
        self.drunks[drunk] = currentLocation.move(xDist, yDist);

#end_class

'''
    Parent Drunk class
'''
class Drunk(object):
    def __init__(self, name):
        self.name = name;
    
    def __str__(self):
        return "Drunk : " + self.name;


#########################################################################################
''' 
    Making different drunk class based on there extent of movement
'''
import random;

'''
    This drunk have equal extent of movement
    in all directions
'''
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [
            (0.0,1.0),
            (1.0,0.0),
            (0.0,-1.0),
            (-1.0,0.0)
        ];
        return random.choice(stepChoices);


'''
    This drunk moves more in the negative y-axis as
    compared to the positive y-axis.
'''
class SouthwardDrunk(Drunk):
    def takeStep(self):
        stepChoices = [
            (0.0,0.9),
            (1.0,0.0),
            (0.0,-1.1),
            (-1.0,0.0)
        ];
        return random.choice(stepChoices);
    
#########################################################################################

'''
    This class perform the random walk
    simulation.
'''
class Simulator(object):
    def __init__(self):
        pass;

    def walk(self, field, drunk, numberOfSteps):
        start = field.getLocation(drunk);
        for s in range(numberOfSteps):
            field.moveDrunk(drunk);
        return start.distanceFrom(field.getLocation(drunk));
    
    def simulateWalk(self, numberOfStepsPerTrial, numberOfTrial, drunkClass):
        drunk = drunkClass("drunk");
        origin  = Location(0,0);
        distances = [];
        for t in range(numberOfTrial):
            f = Field();
            f.addDrunk(drunk, origin);
            distances.append(round(self.walk(f, drunk, numberOfStepsPerTrial), 1));
        return distances;


def drunkTest(walkLengths, numberOfTrials, drunkClass):
    sim = Simulator();
    for numberOfSteps in walkLengths:
        distances = sim.simulateWalk(numberOfSteps, numberOfTrials, drunkClass);
        print str(drunkClass.__name__) + " random walk of " + str(numberOfSteps) + " steps";
        print "Mean = " + str(round(sum(distances)/len(distances), 4));
        print "Min = " + str(min(distances));
        print "Max = " + str(max(distances));



'''
    This code is to visualize the random walk.
    It uses matplotlib to do so
'''
import pylab;

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0;
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index];
        if self.index == len(self.styles) - 1:
            self.index = 0;
        else:
            self.index += 1;
        return result;

def simDrunk(numTrials, drunkClass, walkLengths):
    meanDistances = [];
    for numSteps in walkLengths:
        print "Starting simulation of " + str(numSteps) + " steps";
        sim = Simulator();
        distances = sim.simulateWalk(numSteps, numTrials, drunkClass);
        mean = sum(distances)/len(distances);
        meanDistances.append(mean);
    return meanDistances;

def simAll(drunkClasses, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'));
    for dClass in drunkClasses:
        currentStyle = styleChoice.nextStyle();
        print "Starting simulation of " + dClass.__name__;
        means = simDrunk(numTrials, dClass, walkLengths);
        pylab.plot(walkLengths, means, currentStyle, label = dClass.__name__);

    pylab.title("Mean Distance from Origin ( " + str(numTrials) + " trials ) ");
    pylab.xlabel("Number of steps");
    pylab.ylabel("Mean distance form origin");
    pylab.legend(loc = "best");

def getFinalLocations(numSteps, numTrials, dClass):
    print dClass.__name__ + " walking " + str(numSteps) + " steps for " + str(numTrials) + " trials";
    loc = [];
    d = dClass("drunk");
    for t in range(numTrials):
        print dClass.__name__ + " trial number " + str(t);
        f = Field();
        f.addDrunk(d, Location(0,0));
        for s in range(numSteps):
            f.moveDrunk(d);
        loc.append(f.getLocation(d));
    return loc;

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(("k+", "r^", "mo"));
    for dClass in drunkKinds:
        locs = getFinalLocations(numSteps, numTrials, dClass);
        xVal, yVal = [],[];
        for loc in locs:
            xVal.append(loc.getX());
            yVal.append(loc.getY());
        xVal = pylab.array(xVal);
        yVal = pylab.array(yVal);
        meanX = sum(abs(xVal))/len(xVal);
        meanY = sum(abs(yVal))/len(yVal);
        currentStyle = styleChoice.nextStyle();
        pylab.plot(xVal, yVal, currentStyle, label = dClass.__name__ + " mean abs distance = < " + str(meanX) + "," + str(meanY) + " >");

    pylab.title("Location at End of walks ( " + str(numSteps) + " steps )");
    pylab.xlim(-1000, 1000);
    pylab.ylim(-1000, 1000);
    pylab.xlabel("Steps East/West of Origin");
    pylab.ylabel("Steps Morth/South of Origin");
    pylab.legend(loc = "upper left");

            


random.seed(0);
numSteps = (10, 100, 1000, 10000);
drunkKinds = (UsualDrunk, SouthwardDrunk);
numTrials = 100;
plotLocs(drunkKinds, 10000, 1000);
#simAll( drunkKinds, numSteps, numTrials );
pylab.show();
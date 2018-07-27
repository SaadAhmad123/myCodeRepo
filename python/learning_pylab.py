import pylab as plt;

def main():
    mySample = [];
    myLinear = [];
    myQuadratic = [];
    myCubic = [];
    myExponential = [];

    for i in range(0,31):
        mySample.append(i);
        myLinear.append(i);
        myQuadratic.append(i**2);
        myCubic.append(i**3);
        myExponential.append(1.5**i);

    print "Ploting";
    plt.figure("Linear")
    plt.plot(mySample,myLinear, label="linear");
    plt.xlabel("Samples");
    plt.ylabel("y = x");
    plt.title("Linear");
    plt.legend();
    plt.figure("Cubic");
    plt.plot(mySample,myCubic);
    plt.ylim(0,100);
    plt.xlabel("Samples");
    plt.ylabel("y = x^3");
    plt.title("Cubic");
    plt.show();
main();
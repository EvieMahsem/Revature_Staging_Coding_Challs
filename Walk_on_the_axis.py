def distanceCalc(T):
    #Sets up the initial distance
    distCalc = 0
    #Creates a list with the values of N for a given T
    listVal = [N + 1 for N in range(T)]

    #This allows easy iteration through the list
    listVal.reverse()

    for i in range(T):
        if i == 0:
            #Double counting for going back to (0,0)
            distCalc += 2*listVal[i]
        else:
            distCalc += listVal[i]

    return distCalc

print(distanceCalc(5))
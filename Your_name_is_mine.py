def yourName(T,name1,name2):
    biggestName = ""
    smallestName = ""

    #Used to go through each memember of the name lists
    for i in range(T):
        #Logic to find which name is largest
        if len(name1[i]) >= len(name2[i]):
            biggestName = name1[i]
            smallestName = name2[i]
        else:
            biggestName = name2[i]
            smallestName = name1[i]

        #Splits the names into lists
        biggestNameList = []  
        smallestNameList = []
        for j in biggestName:
            biggestNameList.append(j)
        for j in smallestName:
            smallestNameList.append(j)

        #Counts if the letters of the smaller name are within the bigger name
        yesCounter = 0
        for k in smallestNameList:
            if k in biggestNameList:
                yesCounter += 1
        # If true means that the smaller name is within the bigger name otherwise it is not
        if yesCounter == len(smallestNameList):
            print("YES")
        else:
            print("NO")

yourName(3,["john","ira","kayla"],["johanna","ira","jayla"])



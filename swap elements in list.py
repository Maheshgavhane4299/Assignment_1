# Python program to interchange first and last elements in a list

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


# Driver code
newList = [1,2,3,4,5,6,7]
print(swapList(newList))


# Python program to swap two elements in a list


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 2,4

print(swapPositions(List, pos1 - 1, pos2 - 1))
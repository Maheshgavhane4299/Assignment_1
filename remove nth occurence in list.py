def RemoveIthWord(lst, word, N):
    newList = []
    count = 0

    # iterate the elements
    for i in lst:
        if (i == word):
            count = count + 1
            if (count != N):
                newList.append(i)
        else:
            newList.append(i)

    lst = newList

    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", lst)

    return newList


# Driver code
list = ["geeks", "for", "geeks","geeks"]
word = "geeks"
N = 1

RemoveIthWord(list, word, N)
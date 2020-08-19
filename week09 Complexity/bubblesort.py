# testing bubble sort
def bubble_sort(lists):

    for i in range(len(lists)):
        switched = False

        for j in range(len(lists) - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
                switched = True

        if switched == False:
            break

    return lists

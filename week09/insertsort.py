def insert_sort(lists):
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1

        while j >= 0 and key < lists[j]:
            lists[j + 1] = lists[j]
            j -= 1

        lists[j + 1] = key
    return lists

print(insert_sort([4,3,2,1]))
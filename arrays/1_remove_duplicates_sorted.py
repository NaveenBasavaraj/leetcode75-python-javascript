def removeDuplicates(sorted_array):
    l = 1
    for r in range(1, len(sorted_array)):
        if sorted_array[r] != sorted_array[r-1]:
            sorted_array[l] = sorted_array[r]
            l += 1
    return l
def selection_sort(list) :
    for i in range(len(list)) :
        min_index = i
        for j in range(i+1, len(list)) :
            if list[min_index] > list[j] :
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

print(selection_sort([8,5,2,6,9,3,0,4,7]))
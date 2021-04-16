def insertion_sort(list) :
    for i in range(1,len(list)) :
        num = list[i]
        j = i-1
        while j >= 0 and num < list[j]:
                list[j+1] = list[j]
                j -= 1
        list[j+1] = num
    return list
print(insertion_sort([6,5,3,1,8,7,2,4]))

#[5,3,1,6,8,7,2,4]
#[3,1,5,6,8,7,2,4]
#[1,3,5,6,8,7,2,4]
#[1,3,5,6,8,7,2,4]
#[1,3,5,6,7,8,2,4]
#[1,2,3,5,6,7,8,4]
#[1,2,3,4,5,6,7,8]
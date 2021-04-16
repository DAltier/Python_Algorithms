#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(my_list) :
    for var in range (len(my_list)) :
        if my_list[var] > 0 :
            my_list[var] = "big"
    return my_list
print(biggie_size([-1, 3, 5, -5]))
#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(my_list) :
    count = 0
    for var in range (len(my_list)) :
        if my_list[var] > 0 :
            count +=1
    my_list[var] = count
    return my_list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))
#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum_total(my_list) :
    sum = 0
    for var in range (len(my_list)) :
        sum += my_list[var]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))
#Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5
def average(my_list) :
    sum = 0
    for var in range (len(my_list)) :
        sum += my_list[var]
    return sum/len(my_list)
print(average([1,2,3,4]))
#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(my_list) :
    return len(my_list)
print(length([37,2,1,-9]))
print(length([]))
#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def minimum(my_list) :
    if len(my_list) == 0 :
        return False
    else :
        min=my_list[0]
        for var in range (1,len(my_list)) :
            if my_list[var] < min :
                min = my_list[var]
        return min
print(minimum([37,2,1,-9]))
print(minimum([]))
#Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def maximum(my_list) :
    if len(my_list) == 0 :
        return False
    else :
        max=my_list[0]
        for var in range (1,len(my_list)) :
            if my_list[var] > max :
                max = my_list[var]
        return max
print(maximum([37,2,1,-9]))
print(maximum([]))
#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(my_list) :
    sumTotal = 0
    average = 0
    minimum = my_list[0]
    maximum = my_list[0]
    for var in range (len(my_list)) :
        if my_list[var] < minimum :
            minimum = my_list[var]
        if my_list[var] > maximum :
            maximum = my_list[var]
        sumTotal += my_list[var]
    average = sumTotal/len(my_list)
    new_dict = {'sumTotal': sumTotal, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': len(my_list)}
    return new_dict
print(ultimate_analysis([37,2,1,-9]))
#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(my_list) :
    for var in range (int(len(my_list)/2)) :
        temp = my_list[var]
        my_list[var] = my_list[len(my_list) - var - 1]
        my_list[len(my_list) - var - 1] = temp
    return my_list
print(reverse_list([37,2,1,-9]))
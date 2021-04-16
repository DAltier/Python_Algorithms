import random
def randInt (min = 0, max = 100) :
    if max < 0 :     #edge case
        max = abs(max)
        if max < min :    #edge case
            temp = max
            max = min
            min = temp
    return int(random.randrange(min, max+1)) 

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max = 50)) 	    # should print a random integer between 0 to 50
print(randInt(min = 50)) 	    # should print a random integer between 50 to 100
print(randInt(min = 50, max = 500))    # should print a random integer between 50 and 500
print(randInt(min = 70, max = -25))
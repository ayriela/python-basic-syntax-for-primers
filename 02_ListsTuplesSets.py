# Python doesn't have a data type called arrays, but they have
# - Lists
# - Tuples
# - Sets

# List
# List is a collection which is ordered and changeable. Allows duplicate members.

thislist = [0,1,2,3,5,8]
print("Accessing using brackets the fourth index [4]", thislist[4] )
# expect 5

lengthOfList = len(thislist)
print("length of the list is", lengthOfList)
# expect 6

# For loops to go through list items
print("for loop through thislist %s" % thislist)    
for i in range( len(thislist)-1 ):
    print(thislist[i])

# Easy to access the end of a list (you can do -2, -3 or what ever you want)
print( thislist[-1] )
# expect 8

# Print a range of a list by index.
print( thislist[2:4] )
# expect [2,3]
# last index is excluded/exclusive

thislist.append("I'm a string in an integer world")
print(type(thislist))
print(thislist)


# Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# You can't mutate a Tuple


thistuple = (1,"fun",3,4,"five")
print(len(thistuple))

print( thistuple[1] )
# expect "fun"

print()

# Set 
# Set is a collection which is unordered and unindexed. No duplicate members.

thisset = {0,1,2}

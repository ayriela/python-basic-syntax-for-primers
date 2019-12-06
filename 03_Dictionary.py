# Dictionary
# Dictionaries are kinda like objects that they have Key Value Pairs
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

thisdict = {"key":"value", "zero":0, 2:1, "negative1":-1}
print("Our dictionary has key value pairs %s" % thisdict)
print( thisdict['zero'] )

# Dictionary key assignment to a new value 
# and example of using variables in strings
thisdict[2]=2
print("We've assigned %d to thisdict[2]" % thisdict[2])
# Tuples are like lists. They're another kind of sequence that 
# functions much like a list - they have elements which are indexed starting at 0
# Tuples are immutable - they cannot be modified.
# They are more efficient than lists in terms of memory use.
# Tuples are comparable.

# Sort by values instead of keys with tuples:

c = {'a':10, 'b':1, 'c':22}

tmp = list()

for k, v in c.items() :
    tmp.append((v,k))

print(tmp)

tmp = sorted(tmp, reverse = True)

print(tmp)
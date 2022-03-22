# Python program to demonstrate 
# defaultdict 


from collections import defaultdict 

# Function to return a default 
# values for keys that is not 
# present 
def def_value():
    return 'Not Presnet'


# Defining the dict 

d = defaultdict(def_value)

d['a'] = 1 
d['b'] = 2

print(d['c'])


print(d.__missing__('a'))
print(d.__missing__('b'))



# Defining a dict 2 
d2 = defaultdict(list)


for i in range(5):
    d2[i].append(i)


print("Dictionary with values as list:")
print(d2)

# Defining a dict 3 
d3 = defaultdict(int)


L = [1,2,3,4,2,4,1,2]
# Iterate through the list 
# for keeping the count 

for i in L:
    # The default value is 0 
    # so there is no need to 
    # enter the key first 
    d3[i] += 1 

print(d3)
# Function takes a list of lists and falttens iit into a 
# one-dimensional list.

def flatten(a):
    l = [a[j][i] for j in range(len(a)) for i in range(len(a))]
    return l

print(flatten([[1,2],[3,4]])) # [1, 2, 3, 4]
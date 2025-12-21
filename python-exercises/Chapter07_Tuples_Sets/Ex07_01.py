# Ex.1, printing 1st element and length of tuple
tup = (0, 2, 4, 6, 8)
print(tup[0])
print(len(tup))

# Ex.2, printing max. and min. k elements
k = 3
t = (7, 2, 9, 4, 1, 6)
sorted_t = sorted(t)
print("Sorted tuple is: ",sorted_t)
min_k = sorted_t[:k] # : means slicing, :k means starting from start (index 0) upto k-1
max_k = sorted_t[-k:][::-1] # -k means start from the kth element from the end, : till the end
# [::-1] means reverse the list
print("Min. k elements: ",min_k)
print("Max. k elements: ",max_k)

# Ex. 3, generating tuple using list omprehension
a = (1, 2, 3, 4, 5)
res = [(i, i**2) for i in a] # iterating all elements of tuple a, collect all tuples into a list
print("The tuples are in a list: ",res)

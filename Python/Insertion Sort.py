"""
Insertion Sort Algorithm
------------------------
Salvatore D'Amore
"""

"""		 0  1  2  3  4  5 """
array = [5, 2, 4, 6, 1, 3]

for j in range(1,len(array)):
	key = array[j] 					 # Store the element to be sorted
	i = j - 1 						 # Check against the element prior to the key
	while i >= 0 and array[i] > key: # This while loop finds the element that should be replaced with the key
		array[i+1] = array[i]
		i = i - 1
	array[i+1] = key				 # Set the box ahead of the current box to be the key

print(array)
input('Press Enter to begin')

"""
Pseudo Code:

for j = 2 to A.length // Important to note that the first element here starts 
	key = A[j]
	// Insert A[j] into sorted sequence A[1 .. j-1]
	i = j - 1
	while i > 0 and A[i] > key
		A[i + 1] = A[i]
		i = i - 1
	A[i + 1] = key
"""
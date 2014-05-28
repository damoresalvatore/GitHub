
finalArray = []
array = [ 1, [ 2, 3, [3, 5] , 5], 6, 6 ,[6, 7,7,9] , 7 , 8 , 9]

print(finalArray)

lastList = []
lastList.append(array)

print(len(lastList[0]))

posInArray = []

i = 0
while i < len(lastList[0]):

	# Append the non-list to the final list
	if isinstance(lastList[0][i], list) == False:
		finalArray.append(lastList[0][i])

	elif isinstance(lastList[0][i], list) == True:
		print "We're in"
		# Insert the array that we will examining into the start of our array listing
		lastList.insert(0,lastList[0][i])
		print lastList
		# Since we're starting a new array, we must deposit the old position, so we can continue once we have exhausted our "recursion"
		posInArray.insert(0,i)
		# Reset the i position
		i = 0
		continue

	# If we reach the end of the array, we need to ensure that we pop to the previous array
	if (i == (len(lastList[0]) - 1)) & (len(posInArray) > 0):
		print "onandpop"
		lastList.pop(0)

		# I fucked up so hard with this for like 3 hours. I had popping and reading reversed, so I was stuck in an infinite loop.
		i = posInArray[0]
		posInArray.pop(0)

	i = i + 1


print finalArray
input('You need to hit enter to continue')
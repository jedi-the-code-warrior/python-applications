arr = [4, 21, 3, 0, 9, 11, -17, 1, 5,-2,-7,-9]
target = 4

def sum_of_two3(arr, target):
	
	"""
    input: list of ints, a target (int), no duplicates
    output: int
    returns: a list of tuples if the sum of any two numbers in the list equals target value, else false
    
    Solution: O(N)
	"""
	result = []
	visited = set()
	for num in arr:
		difference = target - num
		if difference in visited :
			result.append((num,difference))
		else:
			visited.add(num)

	if result:
		return result
	else:
		return "Did not find any pair of numbers in the list that add up to the target value."

print(sum_of_two3(arr, target))
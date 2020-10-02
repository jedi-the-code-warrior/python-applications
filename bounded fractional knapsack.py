### Unbounded fractional knapsack

from collections import OrderedDict

def fractional_knapsack(values, weights, capacity):
	""" 
	computes fractional knapsack, unbounded (can repeat weights) 
	"""
	keys = range(len(values))
	ratios = [v/w for v,w in zip(values,weights)]
	print(ratios)
	bag = dict(zip(keys,ratios))
	print(bag)
	sorted_bag = dict(sorted(bag.items(), key=lambda x: x[1], reverse=True))

	print(sorted_bag)
	max_value = 0.0
	fractions = [0.0] * len(values)

	for key,ratio in sorted_bag.items():
		#print(weights[key])

		if weights[key] <= capacity:
			max_value += values[key]
			capacity -= weights[key]
			fractions[key] += 1
		else:
			fractions[key] = (capacity/weights[key])
			max_value += (values[key] * capacity/weights[key])
			break
			

	return max_value, fractions 




### driver code: 

weights = [5, 1, 2, 4, 300, 6]
values = [10, 100, 201, 401, 400, 500]
capacity = 50

max_value, fractions = fractional_knapsack(values, weights, capacity)
print('The maximum value of items that can be carried:', max_value)
print('The fractions in which the items should be taken:', fractions)
""" Stones and Jewels """

jewels = "stone"
stones = "strandedinthejungleunderthesun"

count_dict={}
print(count_dict.fromkeys(list(jewels),0))

class Solution:
    """ count how many jewels are in the stones """
    def __init__(self,jewels,stones):
    	self.jewels = jewels 
    	self.stones = stones

    def count_jewels(self):
    	""" *** """

    	#count_dict = dict()
    	count_dict = dict.fromkeys(list(self.jewels),0)

    	for stone in list(self.stones):
    		if stone in list(self.jewels):
    			count_dict[stone] += 1

    	return count_dict

sol = Solution(jewels,stones)
print(sol.count_jewels())






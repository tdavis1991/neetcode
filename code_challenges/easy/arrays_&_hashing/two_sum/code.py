class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create base case
        if len(nums) == 2:
            return [0, 1]
        #create a hashmap to store value and index
        prevMap = {}

        #iterate over a array to get i(index) and n(value) using the enumerate function
        for i, n in enumerate(nums):
            #get the difference from the target - n(value)
            diff = target - n
            #check if the defference is in the hashmap
            if diff in prevMap:
                #if it is return the prevMap[diff] value which is the index of the other number that sums to the target with the current number and also return the current value index
                return [prevMap[diff], i]
            #if its not in the hashmap add the value to the hashmap where the key is the value and the value is the index
            prevMap[n] = i

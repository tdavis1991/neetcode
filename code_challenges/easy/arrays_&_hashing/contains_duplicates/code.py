class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        input: [num]
        output: boolean
        constraints: 1 <= nums.length <= 105   -109 <= nums[i] <= 109
        """

        #base case
        # check if array length == 1
        if len(nums) == 1:
            # if it is return false
            return False
        # check if array length == 2
        if len(nums) == 2:
            #if it is check both numbers to see if they match
            return nums[0] == nums[1]
        
        # create a set to keep track of numbers
        num_set = set()

        #iterate thru array
        for num in nums:
            # if num is not in array add to dict
            if num not in num_set:
                num_set.add(num)
            #if num is in array return true
            else:
                return True
        #return false if you reach the end of the array
        return False
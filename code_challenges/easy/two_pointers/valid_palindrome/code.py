class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        input: string
        output: boolean
        """
        if len(s) == 1:
            return True
        
        #remove all spaces, special character and set all letters to lower case
        newS = re.sub("[^a-z0-9]",'',s.lower())

        #create a left and right pointer
        left = 0
        right = len(newS) - 1

        #iterate thru string while the left pointer is less than the right pointer
        while left < right:
            #compare the value of the left and right pointer
            if newS[left] != newS[right]:
                #if they are not equal return false
                return False
            #if they are increment the left pointer and decrement the right pointer
            left += 1
            right -= 1
        
        #if you make it thru the whole array return true
        return True
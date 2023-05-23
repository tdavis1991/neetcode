class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        input: 2 strings
        output: boolean
        """
        #base case
        # check if the length of the 2 strings are not the same
        if len(s) != len(t):
            #if it is return false
            return False
        #check if the length of both strings are equal to 1
        if len(s) == 1:
            #if it is compare the 2
            return s == t

        #create a dict to store letters and how many times the show in eac string
        s_dict = {}
        t_dict = {}

        #iterate through each string and add them to their dictionaries
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1

        #compare the 2 dictionaries to see if they match
        return s_dict == t_dict
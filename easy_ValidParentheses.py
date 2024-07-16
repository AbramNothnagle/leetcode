'''
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        openTypes = ['(','[','{']
        closeTypes = [')',']','}']
        openBrackets = []
        #closeBrackets = []
        result = False
        s = list(s)
        for bracket in s:    
            if bracket in openTypes:
                openBrackets.append(bracket)
            elif len(openBrackets)>0:
                if openBrackets[-1] == openTypes[closeTypes.index(bracket)]:
                    openBrackets.pop()
                    result = True
                else:
                    return False
            else:
                return False
        if len(openBrackets) > 0:
            return False
        return True
        

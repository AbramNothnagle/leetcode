/*
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

*/


class Solution {
public:
    bool isValid(string s) {
        string openChars = "([{";
        string closeChars = ")]}";
        //char * openChars = new char[4]();
        //openChars = {'(','[','{','\0'};
        //char * closeChars = new char[4]();
        //closeChars = {')',']','}','\0'};
        string openBrackets = "";

        for(int i = 0; i < s.length(); i++){
            if(openChars.contains(s[i])){
                openBrackets.push_back(s[i]);
            }
            else if(openBrackets.length() > 0){
                if(openBrackets.back() == openChars[closeChars.find(s[i])]){
                    openBrackets.pop_back();
                }
                else{
                    return false;
                }
            }
            else{
                return false;
            }
        }
        if(openBrackets.length() > 0){
            return false;
        }
        return true;
    }
};
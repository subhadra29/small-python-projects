#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        numerical= 0
        roman = s
        roman_number = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
                }
        while i < len(roman):
            if(i == (len(roman)-1)):
                numerical+= roman_number[roman[i]]
                break
            
            if(roman_number[roman[i]] > roman_number[roman[i+1]]):
                numerical+= roman_number[roman[i]]
                i = i+1
            elif(roman_number[roman[i]]< roman_number[roman[i+1]]):
                numerical+= (roman_number[roman[i+1]] - roman_number[roman[i]])
                i= i +2
            elif(roman_number[roman[i]] == roman_number[roman[i+1]]):
                numerical+= (roman_number[roman[i]] + roman_number[roman[i+1]])
                i = i+2
        return numerical





        
        
    

        
# @lc code=end


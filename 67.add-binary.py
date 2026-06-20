#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index=-1
        strnum=[]
        carry=0
        while index>= (len(a)* -1) or index>= (len(b)* -1):
            if(index<(len(a)*-1)):
                if(b[index]=="0" and carry==1):
                    strnum.append(str(1))
                    carry=0
                    index=index-1
                elif(b[index]=="1" and carry==1):
                    strnum.append(str(0))
                    carry=1
                    index=index-1
                else:
                    strnum.append(b[index])
                    index=index-1
            
            elif(index<(len(b)*-1)):
                if(a[index]=="0" and carry==1):
                    strnum.append(str(1))
                    carry=0
                    index=index-1
                elif(a[index]=="1" and carry==1):
                    strnum.append(str(0))
                    carry=1
                    index=index-1
                else:
                    strnum.append(a[index])
                    index=index-1
            

            

            elif(carry==1):
                if(a[index] != b[index]):
                    strnum.append(str(0))
                    carry=1
                    index= index-1
                elif(a[index]=="0" and b[index]=="0"):
                    strnum.append(str(1))
                    carry=0
                    index=index-1
                elif(a[index]=="1" and b[index]== "1"):
                    strnum.append(str(1))
                    carry=1
                    index=index-1



            elif(carry==0):

                if(a[index] != b[index]):
                    strnum.append(str(1))
                    index= index-1
                elif(a[index]=="0" and b[index]=="0"):
                    strnum.append(str(0))
                    index=index-1
                elif(a[index]=="1" and b[index]== "1"):
                    strnum.append(str(0))
                    carry=1
                    index=index-1
        if(carry==1):
                strnum.append(str(1))
                carry=0
        strnum.reverse()
        return "".join(strnum)
               
        
            
                
              
            


        
# @lc code=end


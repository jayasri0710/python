
#This is normal format

class Solution:
    def getLastDigit(self, a, b):
        return(pow(int(a), int(b), 10))
a, b=input().split()
sol=Solution()
print(sol.getLastDigit(a, b))


# this is coding platforms format

class Solution:
    def getLastDigit(self, a, b):
        return(pow(int(a), int(b), 10))
       
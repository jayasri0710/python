# (a+b)*c get input for a and b and function called add() which 
#should return the sum of a and b. and multiply that sum with c

def add(a,b):
    return a+b

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
added=add(a,b)
output=added*c
print(output)
     

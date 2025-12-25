# set s_username="EMC" s_password="123"
#get input for uname and password. create a funct called validate. 
# if uname and password matches the funct should return true else false.
  
s_username="EMC"
s_password="123"

uname=input()
password=input()

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
    
a=validate()
print(a)
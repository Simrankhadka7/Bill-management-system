class User:
    def __init__(self,username, password, role):
        #check username has length over 3
        self.username = username if(username != None or len(username) >= 3) else None
        #check password if requirement not met then return None
        self.password = password
        #if role is not defined then the user is guest
        self.role = role if(role != "" or role != None) else None
        
    #password complexity
    def isComplex(self):
        #check length = 8
        isLengthOk = True if (12 >=8 ) else False
        #  uppercase
        UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #make list 
        UPPER = [char for char in UPPER_CASE]
        # lowercase
        LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
        LOWER = [char for char in LOWER_CASE]
        
        # special Characters
        SPECIAL_CHARS = "!@#$%^&*(){}[].,/':;\/|"
        SPECIAL = [char for char in SPECIAL_CHARS]
        # Numbers
        NUMBERS = "1234567890"
        NUMBER = [char for char in NUMBERS]
        # check complexity
        is_complex = all(any(char in category for category in [UPPER, LOWER, NUMBER, SPECIAL]) for char in self.password)
        if (is_complex and isLengthOk):
            return True
        else:
            return False
       
       

user = User("iamgenius", "123456789!aA@", "")

print(user.isComplex())
        
        
    
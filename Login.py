from userModel import User
import hashlib

class Login:
    def __init__(self, User):
        self.username = User.username
        self.password = User.password
        self.role = User.role
        self.loginSuccess = False
        
    def checkLogin(self):
        readDb = open("UserCreds.db", "r")
        readlines = readDb.readlines()
        #hash password
        hashedPass = hashlib.md5(self.password.encode())
        #to check
        myCred = self.username +":"+ hashedPass.hexdigest()
        print(hashedPass.hexdigest())
        for i in readlines:
            #check authentication and authorization
            if i == myCred and self.role == "admin":
                self.loginSuccess =  True
                break
        #returns true if login is success
        return self.loginSuccess  


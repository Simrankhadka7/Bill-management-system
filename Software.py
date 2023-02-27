#bhatbhateni software
from Price import Price
from Login import Login
from userModel import User


def takeInput(inputMessage):
    return input(inputMessage)

#start of program ask for login
username = str(takeInput("Enter your username: "))
password = str(takeInput("Enter your password: "))
roleDefault = "admin"

#make user object
user = User(username, password, "admin")
loginCheck = Login(user)
#test credentials in testcreds.txt and .gitignore listed to prevent credential leak in commits
if(loginCheck.checkLogin()):
    itemName = takeInput("Enter what item: ")
    unitPrice = takeInput("Enter unit price of {}: ".format(itemName))
    quantity = takeInput("Enter quantity of {}: ".format(itemName))
    markedPrice = float(unitPrice)* float(quantity)
    # vat amount
    vatPercent = 0.13
    vatAmount = markedPrice*vatPercent
    finalAmount = vatAmount + markedPrice
    price = Price(itemName,markedPrice,vatAmount,finalAmount)
    #Here is the data
    print("Printing......")
    print(price.getJSON())

else:
    print("Invalid credentials.Check credentials and try again.")

"""*****************************************************************************
                            MODULES USED IN PROJECT
*****************************************************************************"""
import pickle
import os
import pathlib
"""*****************************************************************************
                            CLASS USED IN PROJECT
*****************************************************************************"""
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter the initial amount(>=500 for Saving and >=1000 for current) : "))
        print("\n\nAccount Created")
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    
"""*****************************************************************************
                        INTRODUCTORY FUNCTION
*****************************************************************************"""

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\tMADE BY : CHAYANDEEP CHAULIA")
    print("\t\t\t\tSCHOOL : CENTRAL MODEL SCHOOL")


"""*****************************************************************************
                    FUNCTION TO GENERATE ACCOUNT NUMBER
*****************************************************************************"""

def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

"""*****************************************************************************
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
*****************************************************************************"""

def displayAll():
    file = pathlib.Path("Accounts.accdb")
    print("Account holders list :")
    if file.exists ():
        infile = open('Accounts.accdb','rb')
        mylist = pickle.load(infile)
        for item in mylist :

            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No records to display")

"""*****************************************************************************
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
*****************************************************************************"""

def displaySp(num): 
    file = pathlib.Path("Accounts.accdb")
    if file.exists ():
        infile = open('Accounts.accdb','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = Rs.",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

"""*****************************************************************************
            FUNCTION TO DEPOSIT/WITHDRAW AMOUNT FOR GIVEN ACCOUNT
*****************************************************************************"""

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("Accounts.accdb")
    if file.exists ():
        infile = open('Accounts.accdb','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('Accounts.accdb')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("\nYour account has been updated")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                        print("\nYour account has been updated")
                    else :
                        print("You cannot withdraw larger amount")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.accdb','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.accdb', 'Accounts.accdb')

"""*****************************************************************************
                    FUNCTION TO DELETE RECORD OF FILE
*****************************************************************************"""

def deleteAccount(num):
    file = pathlib.Path("Accounts.accdb")
    if file.exists ():
        infile = open('Accounts.accdb','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)

        os.remove('Accounts.accdb')
        outfile = open('newaccounts.accdb','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.accdb', 'Accounts.accdb')
        print("\nThis account has been closed")

"""*****************************************************************************
                        FUNCTION TO MODIFY RECORD OF FILE
*****************************************************************************"""

def modifyAccount(num):
    file = pathlib.Path("Accounts.accdb")
    if file.exists ():
        infile = open('Accounts.accdb','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('Accounts.accdb')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
                print("\nAccount has been updated")
        
        outfile = open('newaccounts.accdb','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.accdb', 'Accounts.accdb')
   
"""*****************************************************************************
                    FUNCTION TO WRITE RECORD IN BINARY FILE
*****************************************************************************"""

def writeAccountsFile(account) : 
    
    file = pathlib.Path("Accounts.accdb")
    if file.exists ():
        infile = open('Accounts.accdb','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('Accounts.accdb')
    else :
        oldlist = [account]
    outfile = open('newaccounts.accdb','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.accdb', 'Accounts.accdb')
    
"""*****************************************************************************
                        THE MAIN FUNCTION OF PROGRAM
*****************************************************************************"""

# start of the program
ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("\tMAIN MENU :")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input("Enter your choice : ")
    #system("cls");
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThank you for using bank management system")
        break
    else :
        print("Invalid choice")
    


"""*****************************************************************************
				END OF PROJECT
*****************************************************************************"""



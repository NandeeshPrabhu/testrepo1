


"""k
Program: Banking.py
"""




class Bank:
    #class varaible
    branch_Balance=0
    ifscCode='SYND00023456'

    #instance variables
    name=''
    accNo=0
    balance=0

    #overloading/Polymorphism
    def __init__(self,name='',accNo=0,bal=0):
        self.name=name
        self.accNo = accNo
        self.balance = bal
        Bank.branch_Balance+=bal


    def getBalance(self):
        print("##################")
        print('Name:',self.name)
        print('AccNo:',self.accNo)
        print('IFSC_Code:',Bank.ifscCode)
        print('Balance:',self.balance)
        print("##################")

    #class method
    def getBranchBalance():
        print('Branch balance is ',Bank.branch_Balance)
        

    def deposit(self,val=0,acno=0):
        ##
        if acno == self.accNo:
            self.balance +=val
            Bank.branch_Balance+=val
            print(val,' amount deposited successfully!!')
        else:
            print('Account no',acno, " doesn't match")


    def withdraw(self,acno=0,amount=0):
        if acno == self.accNo:
            if self.balance - amount <= 0 :
                print('You dont have sufficient balance')
            else:
                self.balance -= amount
                Bank.branch_Balance -= amount
                print('Amount ',amount,' successfully withdrawn!!')
        else:
            print('Check your account number !!')
        

    


cust_1 = Bank('Ram',1234,500)
cust_1.getBalance()
cust_1.deposit(1000,1234)
cust_1.deposit()
cust_1.getBalance()


cust_2 = Bank('Alex',2345,1200)
cust_2.getBalance()
cust_2.withdraw(2345,1000)

Bank.getBranchBalance()







        


    

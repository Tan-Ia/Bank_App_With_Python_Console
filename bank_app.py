import string
import random
class BankApp:
    def __init__(self):
        self.customer_name=''
        self.customer_email=''
        self.customer_phone=''
        self.customer_account_num=''
        self.account_type=1
        self.deposite_limit=0
        self.account_amount=0
        self.deposite_amount=0

    def account_open(self):
        self.customer_name = input("Enter Your Name -> ")
        self.customer_email = input("Enter Your Email -> ")
        self.customer_phone = input("Enter Your Phone -> ")
        ask_account_type=input("For Open Savings Account Type 1 Or For Open Student Account Type  2 -> ")
        self.account_type=int(ask_account_type)
        #set account deposite limit
        if(self.account_type==1):
            self.deposite_limit=2000000
        else:
            self.deposite_limit = 500000
        self.customer_account_num = self.generate_account_num(self.customer_name,self.account_type) #set Accunt number
        print(f"Account Number : {self.customer_account_num}")
        # code for acttivate account
        self.amount_validation("For Activate Account Atleast Deposite 500 tk-> ")


    # for generate account number
    def generate_account_num(self,customer_name,acc_type):
        sum = 0
        for i in customer_name:
            sum += int(ord(i))
        if(acc_type==1):
            account_num = 'saving'+str(sum)+str(acc_type)
        else:
            account_num = 'student' + str(sum) + str(acc_type)
        return account_num

    def deposite(self):
        self.account_match(1)

    def amount_validation(self,msg):
        status=0
        while (status==0):
            self.deposite_amount = int(input(msg))
            if (self.deposite_amount <= self.deposite_limit and self.deposite_amount >= 500):
                self.account_amount += self.deposite_amount
                status=1
            elif self.deposite_amount < 500:
                print(f"You Must Have to Deposite Atleast 500 tk ")
            else:
                print(f"Sorry limit Extend !! Your Account Deposite Limit {self.deposite_limit} ")

    def total_amount(self):
        self.account_match(2)
    def account_match(self,check_status):
        account_match = 0
        while (account_match == 0):
            account_num_enter = input("Plz enter your account number -> ")
            if (account_num_enter == self.customer_account_num):
                account_match = 1
                if(check_status==2):
                    print(f"Your Account Balance {self.account_amount}")
                else:
                    self.amount_validation("Enter your deposite amount ->")
            else:
                print("You Enter Wrong Account Number")


account_open = int(input('Enter Account Open limit-> '))
while(account_open>0):
    #for random object name generate
    letters = string.ascii_lowercase
    obj_name = ''.join(random.sample(letters, 5))
    obj_name = BankApp()
    obj_name.account_open()
    while True:
        check_acc = int(input('For Deposite Type 1 Or For check Balance Type  2 For Exit Type 0-> '))
        if(check_acc==1):
            obj_name.deposite()
        elif(check_acc==2):
            obj_name.total_amount()
        else:
            break
    account_open-=1



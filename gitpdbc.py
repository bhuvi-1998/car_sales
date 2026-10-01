import MySQLdb

import random

class bank:
    def __init__(self):
        self.con = MySQLdb.connect(user = "root",
                                   host = "localhost",
                                   password = "#Abr@123")
        self.cursor = self.con.cursor()
        self.cursor.execute("Create database if not exists pdbc_103r")
        self.cursor.execute("use pdbc_103r")

    def create_table(self):
        
        sql ='''create table if not exists acc_holders(holder_id int primary key auto_increment, holder_name varchar(30) not null, 
        phone_number bigint unique, Account_Number bigint not null, 
        Account_Type Varchar(30) Not null, Balance int not null, ifsc_code varchar(30) default "ABR123")'''

        self.cursor.execute(sql)
        self.con.commit()
        

    def create_account(self):
        print("---Wellcome TO Creating Bank Account---")
        
        self.name = input("Enter Your Name : ")
        self.ph_no = int(input("Enter Your Mobile Number : "))
        self.ifsc = "ABR123"
        self.acc_no = random.randint(100000000000,999999999999)
        print('''----CHoice A Account Type----
        1) Savings Account (Diposit 1000 To Create)
        2) Zero Balance Account (Diposit 500 to Create)''')


        while True:
            acc_type = input("What Type Of Account Yout Want To Create :")
            if acc_type.lower() == "savings account":
                amo = int(input("Please Diposit 1000 To Create Savings Account :"))
                if amo < 1000:
                    print("Your Amount Is Lessthen 1000 Please Diposit Required Amount", amo)
                else :
                    break
            elif acc_type.lower() == "zero account":
                amo = int(input("Please Diposit 500 To Create Zero Account :"))
                if amo < 500:
                    print("Your Amount Is Lessthen 500 Please Diposit Required Amount", amo)
                else :
                    break
            else:
                print("You Entered Wrong One Please Select A Valid Account Type ")
        
        self.account_type = acc_type
        self.balance = amo

        sql = f'''INSERT INTO acc_holders
                (holder_name, phone_number, Account_Number, Account_Type, Balance, ifsc_code)
                VALUES ('{self.name}', {self.ph_no}, {self.acc_no}, '{self.account_type}', {self.balance}, '{self.ifsc}')'''

        self.cursor.execute(sql)

        

        self.con.commit()
        

    def diposit(self):
        print("Wellcome To Dipost")
        acc_no = int(input("Enter Your Account Number"))
        amo = int(input("enter diposit amount : "))

        self.cursor.execute(f'''select Balance from acc_holders where Account_Number = {acc_no}''')
        data  = self.cursor.fetchone()

        if data is not None:
            print("Your Current Balance is --",data[0])
            self.cursor.execute(f'''update acc_holders set balance = balance+{amo} where Account_Number = {acc_no}''')
            self.con.commit()
            print("amount is diposited")
            print("Your New Balance Is :-", data[0]+amo)
        else:
            print("invalid account number")

        self.con.commit()

    def withdraw(self):
        print("Wellcome To Withdraw")
        acc_no = int(input("Enter Your Account Number : "))
        amo = int(input("enter diposit amount : "))

        self.cursor.execute(f'''select Balance from acc_holders where Account_Number = {acc_no}''')
        data  = self.cursor.fetchone()
        if data is not None:
            if amo <= data[0]:
                self.cursor.execute(f'''update acc_holders set balance = balance-{amo} where Account_Number = {acc_no}''')
                print(f"Your Money {amo} is Diposited and balance is {data[0]-amo}")
            else:
                print("Please Enter Valid Account Number")
        self.con.commit()

    def balace(self):
        print("Wellcome To Check Balance")
        acc_no = int(input("Enter Your Account Number : "))
        self.cursor.execute(f'''select Balance from acc_holders where Account_Number = {acc_no}''')
        data  = self.cursor.fetchone()
        if data is not None:
            print(f"Your Balance Is {data[0]}")
        else:
            print("Invalid Account Number")
        self.con.commit()

    def details(self):
        print("Wellcome To Check Details")
        acc_no = int(input("Enter Your Account Number : "))
        self.cursor.execute(f'''select * from acc_holders where Account_Number = {acc_no}''')
        data  = self.cursor.fetchone()
        if data is not None:
            print(f"Your Acount Details Are ")
            print(data)
        else:
            print("Invalid Account Number")
        self.con.commit()

obj = bank()
obj.create_table()
while True:
    print('''--- Choice A Number ---
                1) Create Acount
                2) Diposit Amount
                3) Withdraw Amount
                4) Check Balance
                5) Check Details
                6) Exit''')
    n = int(input("Enter A number from 1 to 6 : "))
    if n ==1:
        obj.create_account()
    elif n== 2:
        obj.diposit()
    elif n== 3:
        obj.withdraw()
    elif n == 4:
        obj.balace()
    elif n == 5:
        obj.details()
    elif n == 6:
        break
    else:
        print("Please Enter A Valid Number ")
        continue
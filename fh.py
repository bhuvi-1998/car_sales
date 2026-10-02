
import MySQLdb
class DBconnection:
    def __init__(self):
        self.con = MySQLdb.connect(user = "root",
                              host = "localhost",
                              password = "#Abr@123")
        self.cursor = self.con.cursor()
        self.cursor.execute("create database if not exists car_sales_db ")
        self.cursor.execute("use car_sales_db ")
        self.con.commit()

obj = DBconnection()

class car:
    def __init__(self):
        obj.cursor.execute("create table if not exists cars(car_id int primary key auto_increment, brand varchar(20) not null, \n" 
                " model varchar(20) not null, price int not null, avl_quantity int not null)")
        obj.con.commit()

    def add_car(self):
        while True:
            
            car_brand = input("Enter A Brand Of Car :- ")
            model = input("Enter A Model Of The Car :- ")
            price = int(input("Enter Price Of Of The Model :- "))
            qun = int(input("Enter The Quantity Of Model"))
            obj.cursor.execute('''insert into cars(brand, model, price, avl_quantity) values(%s,%s,%s,%s)''',
                               (car_brand, model, price, qun))
            print("Adding A Car Is Complited")
            n = input("Enter Yes Add A Another Car Or No To Exit")
            
            if n.lower() == "yes":
                continue
            elif n.lower() == "no":
                break
            else:
                print("Invalid Option Please Try Again")
                continue

        obj.con.commit()

    def dispaly(self):
        while True:
            print('''--- Choice One --- 
                    1) Display All Brands And Their Models
                    2) Display All Models Of A Brand''')
            n = int(input("Enter A Number Of 1,2 "))
            if n == 1:
                obj.cursor.execute("select * from cars")
                d = obj.cursor.fetchall()
                print(d)
                break
            elif n == 2:
                brand = input("Enter A Brand Name Of The Car :- ")
                obj.cursor.execute('select * from cars where brand = %s',(brand,))
                f = obj.cursor.fetchall()
                print(f)
                break
            else:
                print("Wrong Input Please Choice One")
                continue
    def search_car(self):
        print("Wellcome To Search Car")
        
        model = input("Enter A Car Model:-")
        obj.cursor.execute("Select * from cars where model = %s",(model,))

        d = obj.cursor.fetchall()
        if not d:
            print(f"'{model}'Car Is Curently Not Available")
        else:
            print(d)

    def update_price(self):
        print("Wellcome To Update Price ")
        model = input("Enter Model Name :- ")
        price = int(input("Enter Updated Price Of The Model :- "))
        obj.cursor.execute("update cars set price = %s where model = %s",(price,model))
        obj.con.commit()

    def update_availabilty(self):
        print("Wellcome To Update Quantity")
        model = input("Enter Model Name :- ")
        qun = int(input("Enter Updated Quantity Of The Model :- "))
        obj.cursor.execute("update cars set avl_quantity = %s where model =%s",(qun,model))
        obj.con.commit()
        print("Car Quantity Is Updated")

    def delete_car(self):
        print("Welcome To Delete A Car")
        model = input("Enter A Car Model :- ")

        obj.cursor.execute(
            "select car_id from cars where model = %s",
            (model,)
        )
        d = obj.cursor.fetchone()

        if not d:
            print("Car Not Found")
            return

        car_id = d[0]

        obj.cursor.execute(
            "select * from sales where car_id = %s",
            (car_id,)
        )
        sale = obj.cursor.fetchall()

        if sale:
            print("Car Cannot Be Deleted Because It Has Sales Records")
        else:
            obj.cursor.execute(
                "delete from cars where car_id = %s",
                (car_id,)
            )
            obj.con.commit()
            print("Car Deleted Successfully")

obj1 =car()

class customers:
    def __init__(self):
        obj.cursor.execute("create table if not exists Customers(customer_id int primary key auto_increment," \
        " cus_name varchar(30) not null, cus_phno bigint unique, email varchar(30) unique)")
        obj.con.commit()

    def add_cus(self):
        while True:
            name = input("Enter Customer Name:- ")
            phno = int(input("Enter Phone Number Of Customer:- "))
            email = input("Enter Email Of Customer:- ")
            obj.cursor.execute("insert into customers(cus_name, cus_phno, email) values (%s,%s,%s)",(name, phno,email))
            print("Customer Is Added")
            print("""Do You Want To add One More Customer
                        Yes To Add One More Customer
                        No To Exit""")
            n = input("Please Enter Yes Or No :- ")
            if n.lower() == "yes":
                continue
            elif n.lower() == "no":
                break
            else:
                print("Please Choice Valid Option")
                continue
        obj.con.commit()

    def view_cus(self):
        
        obj.cursor.execute("select * from customers")
        d = obj.cursor.fetchall()
        obj.con.commit()
        print(d)
    def sec_cus(self):
        num = int(input("Enter Customer Phone Number:- "))
        obj.cursor.execute("select * from customers where cus_phno = %s",(num,))
        d = obj.cursor.fetchone()
        obj.con.commit()
        print(d)

    def update_cus(self):
            print("Wellcome To Update Customer")
            while True:
                print("""To Update Customer Info Please Choice One
                            1. To Update Name
                            2. To Update Phone Number
                            3. To Update Email
                            4. To Exit Update""")
                n = int(input("Enter A number From 1 to 4"))
                if n ==1:
                    name = input("Enter Customer Name:- ")
                    phno = int(input("Enter Phone Number Of Customer:- "))
                    obj.cursor.execute("update customers set cus_name = %s where cus_phno =%s",(name, phno))
                    obj.con.commit()
                    print("Cutomer Details Are Updated")
                    s = input("If You To Update One Customer Press Yes Or No")
                    if s.lower() == "yes":
                        continue
                    elif s.lower() =="no":
                        break
                    
                elif n ==2:
                    phno = int(input("Enter Phone Number Of Customer:- "))
                    email = input("Enter Email Of Customer:- ")
                    obj.cursor.execute("update customers set cus_phno = %s where email =%s",(phno,email ))
                    obj.con.commit()
                    print("Cutomer Details Are Updated")
                    s = input("If You To Update One Customer Press Yes Or No")
                    if s.lower() == "yes":
                        continue
                    elif s.lower() =="no":
                        break                    
                elif n == 3:
                    phno = int(input("Enter Phone Number Of Customer:- "))
                    email = input("Enter Email Of Customer:- ")
                    obj.cursor.execute("update customers set email = %s where cus_phno =%s",(email,phno))
                    obj.con.commit()
                    print("Cutomer Details Are Updated")
                    s = input("If You To Update One Customer Press Yes Or No")
                    if s.lower() == "yes":
                        continue
                    elif s.lower() =="no":
                        break 

                elif n == 4:
                    print("Thank You")
                    break      

                else:
                    print("Invalid Option Please Choice Again")
                    continue

    def del_cus(self):
        print("Wellcome To Delete Customer")
        ph_no = int(input("Enter Customer Phone Number To Delete A Customer :- "))
        obj.cursor.execute("Delete from customers where cus_phno = %s",(ph_no,))
        print("Customer Deleted Sucssefully")


obj2 = customers()
    
class car_sales:
    def __init__(self):
        obj.cursor.execute("""
            create table if not exists sales(
                sale_id int primary key auto_increment,
                car_id int not null,
                customer_id int not null,
                sale_price decimal(12,2) not null,
                sale_date date not null,
                foreign key (car_id) references cars(car_id),
                foreign key (customer_id) references customers(customer_id)
            )
        """)
        obj.con.commit()

    def sale_car(self):
        print("Welcome To Sale Car")

        cus_id = int(input("Enter Customer Id :- "))
        car_id = int(input("Enter Car Id :- "))

        # Check customer
        obj.cursor.execute(
            "select * from customers where customer_id = %s",
            (cus_id,)
        )
        customer = obj.cursor.fetchone()

        if not customer:
            print("Customer Not Found")
            return

        # Check car and quantity
        obj.cursor.execute("select price, avl_quantity from cars where car_id = %s",(car_id,))
        car = obj.cursor.fetchone()

        if not car:
            print("Car Not Found")
            return

        price = car[0]
        quantity = car[1]

        if quantity <= 0:
            print("Car Is Not Available")
            return

        print("Current Car Price :", price)

        sale_price = float(input("Enter Selling Price Of Car :- "))
        sale_date = input("Enter Sale Date (YYYY-MM-DD) :- ")

        # Insert sale
        obj.cursor.execute("""
            insert into sales(car_id, customer_id, sale_price, sale_date)
            values(%s, %s, %s, %s)
        """, (car_id, cus_id, sale_price, sale_date))

        obj.cursor.execute("""
            update cars
            set avl_quantity = avl_quantity - 1
            where car_id = %s
        """, (car_id,))

        obj.con.commit()

        print("Car Sold Successfully")

    def display_sales(self):
        obj.cursor.execute("""select sales.sale_id, customers.cus_name, cars.brand, cars.model, sales.sale_price,
                    sales.sale_date from sales join customers on sales.customer_id = customers.customer_id
                    join cars on sales.car_id = cars.car_id""")

        d = obj.cursor.fetchall()
        print(d)

obj3 = car_sales()


while True:

    print("===== CAR SALES MANAGEMENT SYSTEM =====")

    print('''
            1. Add Car
            2. View Cars
            3. Search Car
            4. Add Customer
            5. View Customers
            6. Sell Car
            7. View Sales
            8. Update Car
            9. Delete Car
            10. Exit''')

    n = int(input("Enter A Number from 1 to 10 :- "))

    if n == 1:
        obj1.add_car()

    elif n == 2:
        obj1.dispaly()

    elif n == 3:
        obj1.search_car()

    elif n == 4:
        obj2.add_cus()

    elif n == 5:
        obj2.view_cus()

    elif n == 6:
        obj3.sale_car()

    elif n == 7:
        obj3.display_sales()

    elif n == 8:
        print("""
        1. Update Price
        2. Update Quantity
        """)

        choice = int(input("Enter Your Choice :- "))

        if choice == 1:
            obj1.update_price()

        elif choice == 2:
            obj1.update_availabilty()

        else:
            print("Invalid Choice")

    elif n == 9:
        obj1.delete_car()

    elif n == 10:
        print("Thank You")
        break

    else:
        print("Please Enter A Valid Number")
        continue
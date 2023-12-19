import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="root", database="Railway_system")

if con.is_connected():
    print("Connected")
else:
    print("Not connected")

cursor = con.cursor()

#Dropping and creating a new database named "Railway_system"

cursor.execute("DROP DATABASE Railway_system")
cursor.execute("CREATE DATABASE Railway_system")
cursor.execute("USE Railway_system")

#Creating 4 tables named "Ticket_Reservation", "book_food", "passenger"

cursor.execute("CREATE TABLE Ticket_Reservation (Train_no int primary key, Train_name char(50), Source char(50), Destination char(50), Ticket_fare int, Arriving_time varchar(50), Departure_time varchar(50), Day char(10))")
cursor.execute("CREATE TABLE book_food(type char(12), item char(12), pno char(15), name char(12), coach char(10))")
cursor.execute("CREATE TABLE passenger (Tno int, Tname char(20), sstn char(20), DS char(20), Name char(15), Age int, Gender char(1), Coach_class char(15), Phone_Number int)")
cursor.execute("CREATE TABLE food(Type char(25), Item char(25), Price int)")

#Inserting details of food

cursor.execute("INSERT INTO food(Type, Item, Price)values('Appetizer', 'Spring Rolls', 8)")
cursor.execute("INSERT INTO food(Type, Item, Price)values('Main Course', 'Chicken Curry', 15)")
cursor.execute("INSERT INTO food(Type, Item, Price)values('Dessert', 'Chocolate Cake', 10)")
cursor.execute("INSERT INTO food(Type, Item, Price)values('Beverage', 'Orange Juice', 4)")
cursor.execute("INSERT INTO food(Type, Item, Price)values('Side Dish', 'Garlic Bread', 6)")
#Inserting details of 10 Trains

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Coimbatore Express', 'Rameshwaram', 'Coimbatore', 2055, '11:17:00', '11:58:00', 'Tuesday')".format(12023)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Chennai Express', 'Alleppey', 'Chennai central', 540, '18:42:00', '05:50:00', 'Sunday')".format(12163)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Ahmedabad passenger', 'Ahmedabad junction', 'Mumbai central', 175, '01:15:00', '07:30:00', 'Monday')".format(59442)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Chennai mail', 'Trivandrum central', 'Chennai central', 1755, '14:50:00', '07:30:00', 'All days')".format(12634)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Alleppey Express', 'Kannur', 'Alleppey', 600, '06:36:00', '02:27:00', 'All days')".format(22639)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Maveli Express', 'Manglore central', 'Trivandrum central', 367, '17:45:00', '07:05:00', 'Friday')".format(16604)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Eranad Express', 'Nagarcoil junction', 'Manglore central', 340, '02:50:00', '08:25:00', 'Saturday')".format(16605)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Banglore Express', 'Ernakulam junction', 'Banglore city', 400, '22:15:00', '09:08:00', 'All days')".format(12678)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Jan shathabti Express', 'Kannur', 'Trivandrum central', 760, '04:50:00', '14:10:00', 'All days')".format(12081)
cursor.execute(st)

st = "INSERT INTO Ticket_Reservation(Train_no, Train_name, Source, Destination, Ticket_fare, Arriving_time, Departure_time, Day) values({}, 'Kerala Express', 'New Delhi', 'Trivandrum central', 945, '11:25:00', '14:35:00', 'Monday')".format(12626)
cursor.execute(st)

con.commit()

ans = 'y' 

# Menu starts from here.

while ans == 'y':
    print(" +-Welcome to Railways Ticket Reservation Portal-+")
    print(" 1.Train Details")
    print(" 2.Booking of Ticket")
    print(" 3.Cancellation of Ticket")
    print(" 4.Food Menu")
    print(" 5.Food Booking")
    print(" 6.Cancellation of food")
    print(" 7.Quit\n")

    n = int(input("Enter your choice(1-4): "))

    if n == 1: #1.Train Details
        q = "SELECT * FROM Ticket_Reservation"
        cursor.execute(q)
        data = cursor.fetchall()
        for i in data:
            print(i)
        print("\n")
        
    elif n == 2: #2. Booking of Ticket
        loc = input("Enter your location: ")
        d = "SELECT * FROM Ticket_Reservation WHERE Destination='{}'".format(loc)
        cursor.execute(d)
        T = cursor.fetchall()
        for row in T:
            print(row)

        too = int(input("Enter the Train no: "))
        trname = input("Enter the Train Name: ")        

        sstn = input("Enter your Source Station: ")
        dstn = input("Enter your Destination Station: ")
        name = input("Enter your Name: ")
        age = int(input("Enter your Age: "))
        gen = input("Enter your Gender: ")
        cls = input("Enter the Coach class: ")
        ph = int(input("Enter your Phone number: "))

        tb = "INSERT INTO passenger values({}, '{}', '{}', '{}', '{}', {}, '{}', '{}', {})".format(
            too, trname, sstn, dstn, name, age, gen, cls, ph)
        cursor.execute(tb)

        con.commit()

        print("Successfully booked")
        print("\n")

    elif n == 3: #3.Cancellation of Ticket
        g = input("Enter your phone number")
        h = "DELETE FROM passenger WHERE Phone_Number='{}'".format(g)
        cursor.execute(h)
        con.commit()
        print("Ticket cancelled.")
        print("\n")
              
    elif n == 4: #4.Food Menu
        q = "SELECT * FROM food"
        cursor.execute(q)
        t = cursor.fetchall()
        for i in t:
            print(i)
        print("\n")

    elif n == 5: #Food Booking
        
        food_type = input("Enter the type of food you would like to order: ")
        food_name = input("Enter the food item: ")
        phn_no = input("Enter you Phone number: ")
        name = input("Enter your name: ")
        coach = input("Enter the coach: ")
        con.commit()
        t = "INSERT INTO book_food values('{}', '{}', '{}', '{}', '{}')".format(food_type,food_name,phn_no,name,coach)
        cursor.execute(t)
        con.commit()

        print("Order Sucessful, Your food will arrive shortly to your corresponding compartment.\n")

    elif n == 6: #6.Cancellation of food
        n = input("Enter your name: ")
        p = input("Enter your Phone number: ")
        i = input("Name of item to be cancelled: ")
        q = "DELETE FROM book_food WHERE name='{}'".format(n)

        cursor.execute(q)
        con.commit()

        print("Your order has been cancelled.\n")

    elif n == 7:
        exit()
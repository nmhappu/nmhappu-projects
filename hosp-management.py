#  Award for Honesty
# .            ⣤⣶⣶⡶⠦⠴⠶⠶⠶⠶⡶⠶⠦⠶⠶⠶⠶⠶⠶⠶⣄
# .⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⠀⢀⣤⠄⠀⠀⣶⢤⣄⠀⠀⠀⣤⣤⣄⣿
# .⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⡷⠋⠁⠀⠀⠀⠙⠢⠙⠻⣿⡿⠿⠿⠫⠋
# .⠀⠀⠀⠀⠀⠀⢀⣤⠞⠉⠀⠀⠀⠀⣴⣶⣄⠀⠀⠀⢀⣕⠦⣀
# .⠀⠀⠀⢀⣤⠾⠋⠁⠀⠀⠀⠀⢀⣼⣿⠟⢿⣆⠀⢠⡟⠉⠉⠊⠳⢤⣀
# .⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⢀⣀⣾⣿⠃⠀⡀⠹⣧⣘⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀
# .⠀⣿⡀⠀⠀⢠⣶⣶⣿⣿⣿⣿⡿⠁⠀⣼⠃⠀⢹⣿⣿⣿⣶⣶⣤⠀⠀⠀⢰⣷
# .⠀⢿⣇⠀⠀⠈⠻⡟⠛⠋⠉⠉⠀⠀⡼⠃⠀⢠⣿⠋⠉⠉⠛⠛⠋⠀⢀⢀⣿⡏
# .⠀⠘⣿⡄⠀⠀⠀⠈⠢⡀⠀⠀⠀⡼⠁⠀⢠⣿⠇⠀⠀⡀⠀⠀⠀⠀⡜⣼⡿
# .⠀⠀⢻⣷⠀⠀⠀⠀⠀⢸⡄⠀⢰⠃⠀⠀⣾⡟⠀⠀⠸⡇⠀⠀⠀⢰⢧⣿⠃
# .⠀⠀⠘⣿⣇⠀⠀⠀⠀⣿⠇⠀⠇⠀⠀⣼⠟⠀⠀⠀⠀⣇⠀⠀⢀⡟⣾⡟
# .⠀⠀⠀⢹⣿⡄⠀⠀⠀⣿⠀⣀⣠⠴⠚⠛⠶⣤⣀⠀⠀⢻⠀⢀⡾⣹⣿⠃
# . ⠀⠀⠀⠀⢿⣷⠀⠀⠀⠙⠊⠁⠀⢠⡆⠀⠀⠀⠉⠛⠓⠋⠀⠸⢣⣿⠏
# .⠀⠀⠀⠀⠘⣿⣷⣦⣤⣤⣄⣀⣀⣿⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣾⡟
# .⠀⠀⠀⠀⠀⢹⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁



import mysql.connector

con=mysql.connector.connect(host='localhost',user= 'root',passwd='root',database="hospitalm")
h_obj=con.cursor()
t=True
while t==True:
    print("""Hospital Management
        1.New User
        2.Registered User
        3.Available Doctors
        4.Exit""")
    
    ch=int(input("Enter Your Choice: "))

    if ch==1:
        idno=int(input("Enter the UserID: "))
        name=input("Enter The Patient's Name:")
        Regdat=input("Today's Date(YYYY/MM/DD):")
        age=int(input("Enter The Patient's age: "))
        gender=input("Enter The Patient's Gender(F/M): ")
        q="insert into users values({},'{}','{}',{},'{}')'".format(idno, Regdat, name, age, gender)
        h_obj.execute(q)
        print("Values Added")
        con.commit()

    if ch==2:
        s_id=int(input("Enter The Patient's UserID: "))
        h_obj.execute("select * from users where idno= (".format(s_id))
        data=h_obj.fetchone()
        print(data)
        con.commit()

    if ch==3:
        print("""
            1 Psychiatrist
            2.Cardiologist
            3.Orthologist
            4.Physician
            5.General Suergeon
            6.Pediatrition
            7.Nurologist
            8.Neuro Sugeron
            9.Pediatric Surgeon
            10.Ooncologist
              """)
        
    c2=int(input("Enter Your Choice:"))

    if c2==1:
        h_obj.execute("select * from docs where dept ='psy")
        p=h_obj.fetchall()
        for i in p:
            print(i)

    if c2==2:
        h_obj.execute("select * from docs where dept = 'card'")
        p=h_obj.fetchall()
        for i in p:
            print (i)

    if  c2==3:
        h_obj.execute("select * from docs where dept = 'orth'")
        p=h_obj.fetchall()
        for i in p:
            print (i)

    if c2==4:
        h_obj.execute("select * from docs where dept = 'phy")
        p=h_obj.fetchall()
        for i in p:
            print (i)

    if c2==5:
        h_obj.execute("select * from docs where dept = 'GS'")
        p=h_obj.fetchallO
        for i in p:
            print()

    if c2==6:
        h_obj.execute("select * from docs where dept ='ped")
        p=h_obj.fetchallQ
        for i in p:
            print(i)

    if c2==7:
        h_obj.execute("select * from docs where dept='nur")
        p=h_obj.fetchall()
        for i in p:
            print ()

    if c2==8:
        h_obj.execute("select * from docs where dept = 'NS")
        p=h_obj.fetchall()
        for i in p:
            print()

    if c2==9:
        h_obj.execute("select * from docs where dept = 'PS'")
        p=h_obj.fetchall()
        for i in p:
            print(i)

    if c2==10:
        h_obj.execute("select * from docs where dept ='oonco'")
        p=h_obj.fetchall()
    for i in p:
        print (i)
    if ch==4:
        exit()
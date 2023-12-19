#  Award for Honesty
# .      ⣤⣶⣶⡶⠦⠴⠶⠶⠶⠶⡶⠶⠦⠶⠶⠶⠶⠶⠶⠶⣄
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

con = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="hospital_management"
)

cursor = con.cursor()

management_list = """
Hospital Management
1. New User
2. Registered User
3. Available Doctors
4. Exit
"""

hos_doctors = """
List of Departments
1. Psychiatrist
2. Cardiologist
3. Orthologist
4. Physician
5. General Surgeon
6. Pediatrician
7. Neurologist
8. Neuro Surgeon
9. Pediatric Surgeon
10. Oncologist
"""

while True:
    print(management_list)

    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        idno = int(input("Enter the UserID: "))
        name = input("Enter The Patient's Name:")
        reg_date = input("Today's Date(YYYY/MM/DD):")
        age = int(input("Enter The Patient's age: "))
        gender = input("Enter The Patient's Gender(F/M): ")

        query = "INSERT INTO users VALUES({}, '{}', '{}', {}, '{}')".format(
            idno, reg_date, name, age, gender
        )

        cursor.execute(query)
        print("Values Added")
        con.commit()

    elif ch == 2:
        select_id = int(input("Enter The Patient's UserID: "))
        cursor.execute("SELECT * FROM users WHERE idno = {}".format(select_id))
        data = cursor.fetchone()
        print(data)
        con.commit()

    elif ch == 3:
        print(hos_doctors)

        doc_choice = int(input("Enter Your Choice:"))

        dept_mapping = {
            1: "psy",
            2: "card",
            3: "orth",
            4: "phys",
            5: "general",
            6: "pedia",
            7: "neurolog",
            8: "neuro sur",
            9: "pediatric sur",
            10: "onco"
        }

        cursor.execute(
            "SELECT * FROM docs WHERE dept like '{}%'".format(dept_mapping.get(doc_choice))
        )

        doctors = cursor.fetchall()
        for doctor in doctors:
            print(doctor)

    elif ch == 4:
        exit()


# planning to replace ch with "users_choice"
# replaced with dictionary, will be reverted for readability.
# corrected .format()

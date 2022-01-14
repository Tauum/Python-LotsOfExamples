# author : tom
# date : 5/11/2021
# objective : sql-lite3 connection test

import sqlite3


def int_input(descriptor):
    var = ""
    while not var.isnumeric():
        var = input(f"Enter value for {descriptor} > ")
    return int(var)


def range_int_input(descriptor, lowest, highest):
    var = ""
    while not var.isnumeric():
        var = input(f"Enter value for {descriptor} between {lowest} - {highest} > ")
    else:
        while (int(var) < lowest or int(var) > highest):
            var = ""
            while not var.isnumeric():
                var = input(f"Error, Enter value for {descriptor} between {lowest} - {highest} > ")
    return int(var)


def menu():
    menu_items = ["insert student record", "view all student records",
                  "View one student record", "Delete one student record",
                  "Update one student record", "Exit"]


    while True:

        count = 0
        for i in menu_items:
            count += 1
            print(f"id: {count} - {i}")

        choice = range_int_input("Menu selection", 1, len(menu_items))

        if choice == 1:
            insert_student_record()
        if choice == 2:
            get_student_records()
        if choice == 3:
            get_student_record()
        if choice == 4:
            delete_student_record()
        if choice == 5:
            update_student_record()
        else:
            print("disconnecting")
            con.close()
            exit()

        choice = input("EXIT (Y/N)?").upper()
        if choice == "Y":
            break
    print("goodbye! :)")
    con.close()
    exit()


def create_Student_Table():
    if (check_Table_Existence("student")):
        print("table student already exists")
    else:
        # id integer primary key,
        cur.execute("""CREATE TABLE student 
            (
            firstName text,
            lastName text,
            email text
            ) """)
        # save request
        con.commit()
        print("request executed")
    return

def check_Table_Existence(table: str):
    cur.execute("""
                    SELECT count(name) FROM sqlite_master
                    WHERE type='table'
                    AND name= ?;
    """, (table,))
    tables_count = cur.fetchone()[0]
    con.commit()
    if tables_count == 1:
        return True
    else:
        return False

def insert_student_record():
    firstName = input("input first name > ")
    lastName = input("input last name > ")
    email = input("input email > ")
    insert_student_data(firstName, lastName, email)
    return

def insert_student_data(firstName: str, lastName: str, email: str):
    con.cursor()
    cur.execute(f"INSERT INTO student VALUES ('{firstName}','{lastName}','{email}')")
    con.commit()
    return

def get_student_records():
    cur = con.cursor()
    print("{:<2} {:<12} {:<12} {:<10}".format("ID", "FirstName", "LastName", "Email"))
    for row in cur.execute("SELECT rowid, * FROM student"):
        print("{:<2} {:<12} {:<12} {:<10}".format(row[0], row[1], row[2], row[3]))
    return

def get_student_record():
    cur = con.cursor()
    student_id = str(int_input("Student ID")) # AGAIN HWY DOESNT THIS WORK WITH INTEGER ??????
    print("{:<2} {:<12} {:<12} {:<10}".format("ID", "FirstName", "LastName", "Email"))
    for row in cur.execute("SELECT rowid, * FROM student WHERE rowid=?", student_id):
        print("{:<2} {:<12} {:<12} {:<10}".format(row[0],row[1],row[2],row[3]))
    return

def delete_student_record():
    cur = con.cursor()
    get_student_records()
    student_id = str(int_input("student ID")) # WHY DOESNT THIS WORK WITH INTENGER??????
    cur.execute("DELETE from student WHERE rowid=?",student_id)
    con.commit()
    get_student_records()
    return

def update_student_record():
    get_student_records()
    student_id = int_input("Student ID")
    updated_first_name = input("First Name > ")
    updated_last_name = input("Last Name > ")
    updated_email = input("Email > ")
    cur.execute("""UPDATE student set firstName = ?,lastName =?,email = ?
    where rowid = ?""",(updated_first_name,updated_last_name,updated_email,student_id))
    get_student_records()
    return

con = sqlite3.connect('test2.db')  # if db doesnt exist it will create one
cur = con.cursor()
menu()



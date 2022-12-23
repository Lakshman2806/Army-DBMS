import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable


def option2():
    """
    Function to implement option 1
    """
    #print("Not implemented")
    # query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
    #         row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])
    print("Average Range of Weapons: ")
    try:

        query = "SELECT AVG(Weapon_Range) AS AVG_RANGE FROM Weapon1;"
        # print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description
        #added = ("Soldier_FirstName", "Soldier_LastName")

        fieldstuple = []
        for rows in desc:
            # print(rows[0], end=' ')
            fieldstuple.append(rows[0])
        # fieldstuple.append("Soldier_FirstName")
        # fieldstuple.append("Soldier_LastName")

        # print(fieldstuple)
        newtable = PrettyTable(fieldstuple)
        # newtable.fields = fieldstuple
        # print("Soldier_firstName Soldier_lastName")
        # print()
        for rows in table:
            # tuple = (first_name, last_name)
            # print(*rows.values(),end=" ")
            # print(first_name + " " + last_name)
            row = []
            for i in rows.values():
                row.append(i)
            # row.append(first_name)
            # row.append(last_name)
            newtable.add_row(row)
        print(newtable)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return


def getAgeStat(age):
    try:
        # Takes emplyee details as input
        row = {}

        # print("The statistics of soldiers whose age is under %d",age)
        query = "SELECT * FROM SOLDIER WHERE DOB IN (SELECT DOB FROM AGE WHERE Age < %d);" % age
        # print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description
        fieldtuple = []
        for rows in desc:
            # print(rows[0], end=' ')
            fieldtuple.append(rows[0])
        newtable = PrettyTable(fieldtuple)
        print()
        for rows in table:
            # print(*rows.values())
            row = []
            for i in rows.values():
                row.append(i)
            newtable.add_row(row)
        print(newtable)
        # print(table)
        #print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def UpdateAllWeapons():
    try:
        row = {}
        print("Enter the details of the type of guns that have been shifted ")
        row["type"] = input("Type: ")
        row["inventory"] = input("New inventory: ")

        query = "update Weapon1 SET Inventory_Name = '%s' Where (Weapon_ID,Weapon_Name) IN (Select Weapon_ID, Weapon_Name FROM Weapon2 where Type='%s');" % (
            row["inventory"], row["type"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def deleteSoldier():
    try:
        row = {}
        print("Enter the details of the Soldier to be deleted ")
        row["Sno"] = input("Service_Number : ")
        # row["inventory"] = input("New inventory: ")

        query = "delete FROM SOLDIER Where Service_Number = '%s';" % (
            row["Sno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def option3():
    """
    Function to implement option 2
    """
    print("Names of Soldiers who are married: ")
    try:

        query = "SELECT First_Name,Last_name FROM SOLDIER WHERE Service_Number IN (Select RelatedSoldier_ServiceNo From Dependent where RelationwithSoldier = 'Wife');"
        # print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description
        #added = ("Soldier_FirstName", "Soldier_LastName")

        fieldstuple = []
        for rows in desc:
            # print(rows[0], end=' ')
            fieldstuple.append(rows[0])
        # fieldstuple.append("Soldier_FirstName")
        # fieldstuple.append("Soldier_LastName")

        # print(fieldstuple)
        newtable = PrettyTable(fieldstuple)
        # newtable.fields = fieldstuple
        # print("Soldier_firstName Soldier_lastName")
        # print()
        for rows in table:
            # tuple = (first_name, last_name)
            # print(*rows.values(),end=" ")
            # print(first_name + " " + last_name)
            row = []
            for i in rows.values():
                row.append(i)
            # row.append(first_name)
            # row.append(last_name)
            newtable.add_row(row)
        print(newtable)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return


def option4():
    """
    Function to implement option 3
    """
    try:
        first_name = input("Give the first name of the soldier:")
        last_name = input("Give the last name of the soldier:")

        query = "SELECT * FROM Dependent WHERE RelatedSoldier_ServiceNo in (Select Service_Number From SOLDIER where First_Name='%s' and Last_name='%s');" % (
            first_name, last_name)
        # print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description
        added = ("Soldier_FirstName", "Soldier_LastName")

        fieldstuple = []
        for rows in desc:
            # print(rows[0], end=' ')
            fieldstuple.append(rows[0])
        fieldstuple.append("Soldier_FirstName")
        fieldstuple.append("Soldier_LastName")

        # print(fieldstuple)
        newtable = PrettyTable(fieldstuple)
        # newtable.fields = fieldstuple
        # print("Soldier_firstName Soldier_lastName")
        # print()
        for rows in table:
            # tuple = (first_name, last_name)
            # print(*rows.values(),end=" ")
            # print(first_name + " " + last_name)
            row = []
            for i in rows.values():
                row.append(i)
            row.append(first_name)
            row.append(last_name)
            newtable.add_row(row)
        print(newtable)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return
def checkZone(ZoneID):
    query = "SELECT * FROM Zone WHERE PIN_Code = '%s';" %(ZoneID)

    try:
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        # print(table)
        # print(len(table))
        if (len(table) == 0):
            query = "INSERT INTO Zone VALUES('%s' , NULL, NULL);" % (ZoneID)
            try:
                print(query)
                cur.execute(query)
                con.commit()
                print("Inserted in Table Zone")
            except Exception as e:
                con.rollback()
                print("Failed to update database")
                print(">>>>>>>>>>>>>", e)
                return
        return 1

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
        return
def insertSoldier():
    try:
        row = {}
        print("Enter table details: ")
        row["Sno"] = input("Service_Number: ")
        row["FirstName"] = input("First_Name: ")
        row["LastName"] = input("Last_name: ")
        row["Height"] = int(input("Height: "))
        row["Soldier_Rank"] = input("Soldier_Rank: ")
        row["Weight"] = int(input("Weight: "))
        row["DOB"] = input("DOB in YYYY-MM-DD: ")
        row["Zonal_Code"] = input("Zonal_Code: ")
        row["Quarter_Name"] = input("Quarter_Name: ")
        row["Quarter_Region"] = input("Quarter_Region: ")
        row["Room_Id"] = input("Room_Id: ")
        
        
        checkZone(row["Zonal_Code"])
        query = "INSERT INTO table_name (%s, %s, %s, %d, %s, %d, %s, %s, %s, %s, %s);"%(row["Sno"], row["FirstName"], row["LastName"],row["Height"],row["Soldier_Rank"],row["Weight"],row["DOB"],row["Zonal_Code"],row["Quarter_Name"],row["QUarter_Region"],row["Room_ID"])

        print(query)
        cur.execute(query)
        con.commit()
        
        print("Inserted the Soldier")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def retrievedata():
    try:
        row = {}
        print("Enter table details: ")
        row["Name"] = input("Table Name: ")

        query = "SELECT * FROM %s" % (
            row["Name"])

        print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description
        fields = []
        for rows in desc:
            # print(rows[0],end=' ')
            fields.append(rows[0])

        print()
        newtable = PrettyTable(fields)
        for rows in table:
            # print(*rows.values())
            row = []
            for i in rows.values():
                row.append(i)
            newtable.add_row(row)
        print(newtable)
        print("Done")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def updateRank():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        row = {}
        print("Enter soldier details and rank they need to be promoted or demoted to: ")
        row["SNo"] = input("Service Number: ")
        row["Rank"] = input("New Rank: ")

        query = "UPDATE SOLDIER SET Soldier_Rank = '%s' WHERE Service_Number = '%s'" % (
            row["Rank"], row["SNo"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def updateZone():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        row = {}
        print("Enter soldier details and rank they need to be promoted or demoted to: ")
        row["SNo"] = input("Service Number: ")
        row["Zone"] = input("New Zone_name: ")

        query = "UPDATE SOLDIER SET Zonal_Code = (SELECT PIN_Code from Zone where Zone_Name = '%s') WHERE Service_Number = '%s';" % (
            row["Zone"], row["SNo"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def zoneprotection():
    print("The Zone(s) that needs more protection/has the least protection is: ")
    try:

        query = "SELECT Zone_Name,PIN_Code FROM Zone WHERE PIN_Code IN (SELECT Zonal_Code FROM SOLDIER GROUP BY Zonal_Code HAVING COUNT(*) IN (SELECT * FROM (SELECT COUNT(*) FROM SOLDIER GROUP BY Zonal_Code ORDER BY COUNT(*) ASC LIMIT 1) AS T1));"
        # print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description
        #added = ("Soldier_FirstName", "Soldier_LastName")

        fieldstuple = []
        for rows in desc:
            # print(rows[0], end=' ')
            fieldstuple.append(rows[0])
        # fieldstuple.append("Soldier_FirstName")
        # fieldstuple.append("Soldier_LastName")

        # print(fieldstuple)
        newtable = PrettyTable(fieldstuple)
        # newtable.fields = fieldstuple
        # print("Soldier_firstName Soldier_lastName")
        # print()
        for rows in table:
            # tuple = (first_name, last_name)
            # print(*rows.values(),end=" ")
            # print(first_name + " " + last_name)
            row = []
            for i in rows.values():
                row.append(i)
            # row.append(first_name)
            # row.append(last_name)
            newtable.add_row(row)
        print(newtable)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return


def agefunc():
    try:
        Age = int(input("Enter the Max Age Limit: "))
        query = " SELECT Zone_Name,COUNT(*) FROM SOLDIER,Zone WHERE DOB IN (SELECT DOB FROM AGE WHERE Age < %d) AND Zonal_Code = PIN_Code AND PIN_Code = Zonal_Code GROUP BY Zonal_Code;" % (Age)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description

        fieldstuple = []
        for rows in desc:
            fieldstuple.append(rows[0])

        newtable = PrettyTable(fieldstuple)
        for rows in table:
            row = []
            for i in rows.values():
                row.append(i)
            newtable.add_row(row)
        print(newtable)
        print("Info of all soldier with Age less than " + str(Age))
        getAgeStat(Age)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return


def joinquery():
    try:
        c = input("Enter a First character of the Service Number of soldier: ")
        query = "SELECT First_Name,Last_name,Soldier_Rank,BMI FROM SOLDIER NATURAL JOIN Health_Stats WHERE Service_Number LIKE '%s" % (c) + "%';"
        #query = query + "%';"
        print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description

        fieldstuple = []
        for rows in desc:
            fieldstuple.append(rows[0])

        newtable = PrettyTable(fieldstuple)
        for rows in table:
            row = []
            for i in rows.values():
                row.append(i)
            newtable.add_row(row)
        print(newtable)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return

def searchquery():
    try:
        c = input("Enter a First character of the Name of the soldier: ")
        query = "SELECT * FROM SOLDIER WHERE First_Name LIKE '%s" % (c) + "%';"
        #query = query + "%';"
        print(query)
        cur.execute(query)
        con.commit()
        table = cur.fetchall()
        desc = cur.description

        fieldstuple = []
        for rows in desc:
            fieldstuple.append(rows[0])

        newtable = PrettyTable(fieldstuple)
        for rows in table:
            row = []
            for i in rows.values():
                row.append(i)
            newtable.add_row(row)
        print(newtable)
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return

def retirementage():
    try:
        row = {}
        print("Enter Retirement Age: ")
        row["Sno"] = int(input("Retirement Age : "))
        # row["inventory"] = input("New inventory: ")

        query = "delete FROM SOLDIER Where DOB IN (SELECT DOB FROM AGE WHERE Age >= %d);" % (row["Sno"])
        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return
def insertSoldier():
    try:
        row = {}
        print("Enter table details: ")
        row["Sno"] = input("Service_Number: ")
        row["FirstName"] = input("First_Name: ")
        row["LastName"] = input("Last_name: ")
        row["Height"] = (input("Height: "))
        row["Soldier_Rank"] = input("Soldier_Rank: ")
        row["Weight"] = (input("Weight: "))
        row["DOB"] = input("DOB in YYYY-MM-DD: ")
        row["Zonal_Code"] = input("Zonal_Code: ")
        row["Quarter_Name"] = input("Quarter_Name: ")
        row["Quarter_Region"] = input("Quarter_Region: ")
        row["Room_Id"] = input("Room_Id: ")
        checkZone(row["Zonal_Code"])
        # query = "INSERT INTO Zone(PIN_Code) VALUES('%s');" % (
        #     row["Zonal_Code"])

        query = "INSERT INTO SOLDIER VALUES('%s','%s','%s',%s,'%s',%s,'%s','%s','%s','%s','%s');" % (
            row["Sno"], row["FirstName"], row["LastName"], row["Height"], row["Soldier_Rank"], row["Weight"], row["DOB"], row["Zonal_Code"], row["Quarter_Name"], row["Quarter_Region"], row["Room_Id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted the Soldier")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return
def weaponentry():
    try:
        row = {}
        row["ID"] = input("Weapon ID: ")
        row["Name"] = input("Weapon Name: ")
        row["Range"] = int(input("Range: "))
        row["Type"] = input("Type: ")
        row["Inventory"] = input("Inventory where it should be stored: ")
        query = "INSERT INTO Weapon1(Weapon_ID, Weapon_Name, Weapon_Range, Inventory_Name) VALUES('%s', '%s', %d, '%s')" % (
            row["ID"], row["Name"], row["Range"], row["Inventory"])
        # query = "INSERT INTO Weapon2(Weapon_ID, Weapon_Name, Type) VALUES('%s', '%s', '%s')" % (
        #     row["ID"], row["Name"], row["Type"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Weapon1 updated")
        # query = "INSERT INTO Weapon1(Weapon_ID, Weapon_Range, Inventory_Name) VALUES('%s', '%s', '%d', '%s')" % (
        #     row["ID"], row["Name"], row["Range"], row["Inventory"])
        query = "INSERT INTO Weapon2(Weapon_ID, Weapon_Name, Type) VALUES('%s', '%s', '%s')" % (
            row["ID"], row["Name"], row["Type"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Weapon2 updated")
        
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

def updateroom():
    try:
        row = {}
        row["SNo"] = input("Service Number: ")
        row["Zone"] = input("New Room: ")

        query = "UPDATE SOLDIER SET Room_Id = '%s' WHERE Service_Number = '%s';" % (
            row["Zone"], row["SNo"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if (ch == 1):
        updateRank()
    elif (ch == 2):
        retrievedata()
    elif (ch == 3):
        option3()
    elif (ch == 4):
        option4()
    elif (ch == 5):
        deleteSoldier()
    elif (ch == 6):
        option2()
    elif (ch == 7):
        zoneprotection()
    elif (ch == 8):
        agefunc()
    elif (ch == 9):
        joinquery()
    elif (ch == 10):
        UpdateAllWeapons()
    elif (ch == 11):
        searchquery()
    elif (ch == 12):
        retirementage()
    elif (ch == 13):
        weaponentry()
    elif (ch == 14):
        insertSoldier()
    elif (ch == 15):
        updateroom()
    else:
        print("Error: Invalid Option")


# Global
while (1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    # username = "root"
    # password = "Aa@123456"
    password = input("Password: ")

    database = input("database: ")


    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=password,
                              db=database,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if (con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while (1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Update Rank of a Soldier")  # Hire an Employee
                print("2. Retrive Data from a Table")  # Fire an Employee
                # Promote Employee
                print("3. Get Names of all married soldiers")
                # Employee Statistics
                print("4. Get details of Dependent of a Soldier")
                print("5. Delete a soldier")
                print("6. Average Range of Weapons")
                print("7. Zones that need more protection")
                print("8. People less than a particular age in each Zone")
                print("9. Find Full Name, Rank, BMI of Soldiers whose Service Number starts with a character of our choice")
                print("10. Update inventory name for all the weapons of a particular type")
                print("11. Search for all soldiers whose name starts with a particular character")
                print("12. Delete all the soldiers greater than a particular age ( Retirement Age )")
                print("13. Insert the weapons obtained from the ruins of war")
                print("14. Insert new soldier tuple. If he is from a new zone insert it too")
                print("15. Update Room ID of a Soldier")
                print("16. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 16:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
# Project Phase 4

## Command 1 : Update Rank of a Soldier

- This command updates a soldier's rank to the rank specified by the user
- The soldier whose rank should be updated should be specified by the Soldier_service number
- The query for this command is
  ```
  UPDATE SOLDIER SET Soldier_Rank = <Rank> WHERE Service_Number = <Sno>
  ```

## Command 2: Retrieve data of a Table

- This command shows the data of a specified table by a user
- The table should be specified by the user
- The query for this command is
  ```
  SELECT * FROM <Table>
  ```

## Command 3: Get names of all married soldiers

- This command shows the data of all the soldiers who are married

- The query for this command is
  ```
  SELECT First_Name,Last_name FROM SOLDIER WHERE Service_Number IN (Select RelatedSoldier_ServiceNo From Dependent where RelationwithSoldier = 'Wife');
  ```

## Command 4: Get details of dependent of a soldier:

- This command shows the data of all the dependents on a soldier
- The soldier should be specified his first and last name
- The query for this command is
  ```
  SELECT * FROM Dependent WHERE RelatedSoldier_ServiceNo in (Select Service_Number From SOLDIER where First_Name=<First_Name> and Last_name=<Last_name>);
  ```

## Command 5: Delete a Soldier

- This command deletes a soldier if he has retired or he has died in war
- The user should specify the Sno of the soldier
- The query for this command us

```
delete FROM Soldier Where Sno=<Sno>
```

## Command 6: Average range of weapons:

- This command shows the average range of all weapons

- The query for this command is
  ```
  SELECT AVG(Weapon_Range) AS AVG_RANGE FROM Weapon1;
  ```

## Command 7: Zones that need more protection

- This command shows the zone which best needs protection if a critical situation arises
- The user should specify the Sno of the soldier
* The least protected is the zone with the least frequent zonal_code in the zonal table
- The query for this command us

```
SELECT Zone_Name,PIN_Code FROM Zone WHERE PIN_Code IN (SELECT Zonal_Code FROM SOLDIER GROUP BY Zonal_Code HAVING COUNT(*) IN (SELECT * FROM (SELECT COUNT(*) FROM SOLDIER GROUP BY Zonal_Code ORDER BY COUNT(*) ASC LIMIT 1) AS T1));
```

## Command 8. People less than a particular age in each Zone:

- This command gives the soldiers who are less than a particular age and also the zone wise statistics
- The user should specify the age
  \*The queries of the command is

```
Query 1:
SELECT Zone_Name,COUNT(*) FROM SOLDIER,Zone WHERE DOB IN (SELECT DOB FROM AGE WHERE Age < <Age>) AND Zonal_Code = PIN_Code AND PIN_Code = Zonal_Code GROUP BY Zonal_Code;

Query 2:
SELECT * FROM SOLDIER WHERE DOB IN (SELECT DOB FROM AGE WHERE Age < %d);
```

## Command 9: Find Full Name, Rank, BMI of Soldiers whose Service Number starts with a character of our choice

- This command shows the first name, last name, BMI of all the soldiers starting with a letter specified by the user
- The query for this command is

```
SELECT First_Name,Last_name,Soldier_Rank,BMI FROM SOLDIER NATURAL JOIN Health_Stats WHERE Service_Number LIKE '<char>%';
```

## Command 10: Update inventory name for all the weapons of a particular type

- This command updates all the weapons of a particular type to a particular inventory specified by the user
- The query for this command is

```
update Weapon1 SET Inventory_Name = '%s' Where (Weapon_ID,Weapon_Name) = (Select Weapon_ID, Weapon_Name FROM Weapon2 where Type='%s');
```

## Command 11: Search for all soldiers whose name starts with a particular character

- This command shows all the soldiers whose name starts with a particular character
- The query for this command is


```
SELECT * FROM SOLDIER WHERE First_Name LIKE '%s" % (c) + "%';
```
## Command 12: Delete all the soldiers greater than a particular age ( Retirement Age )

- This command deletes all soldiers after a certain retirement age
- The query for this command is


```
delete FROM SOLDIER Where DOB IN (SELECT DOB FROM AGE WHERE Age >= %d);
```
## Command 13: Insert the weapons obtained from the ruins of war

- This command inserts a new weapon into the weapons table i.e weapon1 and weapon2
- The query for this command is


```
INSERT 1:
INSERT INTO Weapon1(Weapon_ID, Weapon_Name, Weapon_Range, Inventory_Name) VALUES('%s', '%s', %d, '%s')

INSERT 2:
INSERT INTO Weapon2(Weapon_ID, Weapon_Name, Type) VALUES('%s', '%s', '%s')
```
## Command 14: Insert new soldier tuple. If he is from a new zone insert it too

- This command inserts a newly recruited soldier into the database
* It first checks if the specified zone is there or not and then inserts it if it is not present
- The query for this command is

```
INSERT1:
INSERT INTO Zone VALUES('%s' , NULL, NULL);


INSERT2:
INSERT INTO table_name (%s, %s, %s, %d, %s, %d, %s, %s, %s, %s, %s);
```

## Command 15: Log out
* Exits from the program

## Command 15: Update Room ID of a Soldier
- This command updates the Room ID of a soldier
- The query for this command is

```
UPDATE SOLDIER SET Room_Id = '%s' WHERE Service_Number = '%s'
```

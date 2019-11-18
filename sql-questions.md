# 50 SQL Interview Questions

### SQL Questions
1. What does UNION do? What is the difference between UNION and UNION ALL?

2. List and explain the different types of JOIN clauses supported in ANSI-standard SQL.

3. Given the following table
```
+----+--------------+
| id | name         |
+----+--------------+
|  1 | John Doe     |
|  2 | Jane Doe     |
|  3 | Alice Jones  |
|  4 | Bobby Louis  |
|  5 | Lisa Romero  |
+----+--------------+

sql> SELECT * FROM races;
+----+----------------+-----------+
| id | event          | winner_id |
+----+----------------+-----------+
|  1 | 100 meter dash |  2        |
|  2 | 500 meter dash |  3        |
|  3 | cross-country  |  2        |
|  4 | triathalon     |  NULL     |
+----+----------------+-----------+
```
What will be the result of the query below?
```
SELECT * FROM runners WHERE id NOT IN (SELECT winner_id FROM races)
Explain your answer and also provide an alternative version of this query that will avoid the issue that it exposes.
```
4. Given two tables created and populated as follows:
```
CREATE TABLE dbo.envelope(id int, user_id int);
CREATE TABLE dbo.docs(idnum int, pageseq int, doctext varchar(100));

INSERT INTO dbo.envelope VALUES
  (1,1),
  (2,2),
  (3,3);

INSERT INTO dbo.docs(idnum,pageseq) VALUES
  (1,5),
  (2,6),
  (null,0);
```
What will the result be from the following query:
```
UPDATE docs SET doctext=pageseq FROM docs INNER JOIN envelope ON envelope.id=docs.idnum
WHERE EXISTS (
  SELECT 1 FROM dbo.docs
  WHERE id=envelope.id
);
```
5. Given these contents of the Customers table:
```
Id	Name			ReferredBy
1	John Doe		NULL
2	Jane Smith		NULL
3	Anne Jenkins		2
4	Eric Branford		NULL
5	Pat Richards		1
6	Alice Barnes		2
```
Here is a query written to return the list of customers not referred by Jane Smith:
```
SELECT Name FROM Customers WHERE ReferredBy <> 2;
```
What will be the result of the query? Why? What would be a better way to write it?

6. Assume a schema of Emp ( Id, Name, DeptId ) , Dept ( Id, Name).

If there are 10 records in the Emp table and 5 records in the Dept table, how many rows will be displayed in the result of the following SQL query:

```Select * From Emp, Dept```
Explain your answer.

7. Given two tables created as follows
```
create table test_a(id numeric);

create table test_b(id numeric);

insert into test_a(id) values
  (10),
  (20),
  (30),
  (40),
  (50);

insert into test_b(id) values
  (10),
  (30),
  (50);
```
Write a query to fetch values in table test_a that are and not in test_b without using the NOT keyword.

Note, Oracle does not support the above INSERT syntax, so you would need this instead:
```
insert into test_a(id) values (10);
insert into test_a(id) values (20);
insert into test_a(id) values (30);
insert into test_a(id) values (40);
insert into test_a(id) values (50);
insert into test_b(id) values (10);
insert into test_b(id) values (30);
insert into test_b(id) values (50);
```
8. Given a table TBL with a field Nmbr that has rows with the following values:
```
1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1
```
Write a query to add 2 where Nmbr is 0 and add 3 where Nmbr is 1.

9. Write a SQL query to find the 10th highest employee salary from an Employee table. Explain your answer.

(Note: You may assume that there are at least 10 records in the Employee table.)

10. Write a SQL query using UNION ALL (not UNION) that uses the WHERE clause to eliminate duplicates. Why might you want to do this?

11. Given the following tables:
```
SELECT * FROM users;

user_id  username
1        John Doe                                                                                            
2        Jane Don                                                                                            
3        Alice Jones                                                                                         
4        Lisa Romero

SELECT * FROM training_details;

user_training_id  user_id  training_id  training_date
1                 1        1            "2015-08-02"
2                 2        1            "2015-08-03"
3                 3        2            "2015-08-02"
4                 4        2            "2015-08-04"
5                 2        2            "2015-08-03"
6                 1        1            "2015-08-02"
7                 3        2            "2015-08-04"
8                 4        3            "2015-08-03"
9                 1        4            "2015-08-03"
10                3        1            "2015-08-02"
11                4        2            "2015-08-04"
12                3        2            "2015-08-02"
13                1        1            "2015-08-02"
14                4        3            "2015-08-03"
```
Write a query to to get the list of users who took the a training lesson more than once in the same day, grouped by user and training lesson, each ordered from the most recent lesson date to oldest date.

12. What is an execution plan? When would you use it? How would you view the execution plan?

13. List and explain each of the ACID properties that collectively guarantee that database transactions are processed reliably.

14. Given a table dbo.users where the column user_id is a unique numeric identifier, how can you efficiently select the first 100 odd user_id values from the table?

(Assume the table contains well over 100 records with odd user_id values.)

15. How can you select all the even number records from a table? All the odd number records?

16. What are the NVL and the NVL2 functions in SQL? How do they differ?

17. What is the difference between the RANK() and DENSE_RANK() functions? Provide an example.

18. What is the difference between the WHERE and HAVING clauses?

19. Suppose we have a Customer table containing the following data:
```
CustomerID  CustomerName
1           Prashant Kaurav
2           Ashish Jha
3           Ankit Varma
4           Vineet Kumar
5           Rahul Kumar
```
Write a single SQL statement to concatenate all the customer names into the following single semicolon-separated string:

Prashant Kaurav; Ashish Jha; Ankit Varma; Vineet Kumar; Rahul Kumar

20. Given a table Employee having columns empName and empId, what will be the result of the SQL query below?

select empName from Employee order by 2 desc;

21. What will be the output of the below query, given an Employee table having 10 records?
```
BEGIN TRAN
TRUNCATE TABLE Employees
ROLLBACK
SELECT * FROM Employees
```
22. What is the difference between single-row functions and multiple-row functions?

23. What is the group by clause used for?

24. What is the difference between char and varchar2?

25. Write an SQL query to display the text CAPONE as: 
C
A
P
O
N
E

26. Can we insert a row for identity column implicitly?

27. Given this table:
```
Testdb=# Select * FROM "Test"."EMP";

 ID
----
  1
  2
  3
  4
  5
(5 rows)
```
What will be the output of below snippet?
```
Select SUM(1) FROM "Test"."EMP";
Select SUM(2) FROM "Test"."EMP";
Select SUM(3) FROM "Test"."EMP";
```
28. Table is as follows:
```
ID	C1	C2	C3
1	Red	Yellow	Blue
2	NULL	Red	Green
3	Yellow	NULL	Violet
```
Print the rows which have ‘Yellow’ in one of the columns C1, C2, or C3, but without using OR.

29. Write a query to insert/update Col2’s values to look exactly opposite to Col1’s values.
```
Col1	Col2
1	0
0	1
0	1
0	1
1	0
0	1
1	0
1	0
```
30. How do you get the last id without the max function?

31. What is the difference between IN and EXISTS?

32. Suppose in a table, seven records are there.

The column is an identity column.

Now the client wants to insert a record after the identity value 7 with its identity value starting from 10.

Is it possible? If so, how? If not, why not?

33. How can you use a CTE to return the fifth highest (or Nth highest) salary from a table?

34. Imagine a single column in a table that is populated with either a single digit (0-9) or a single character (a-z, A-Z). Write a SQL query to print ‘Fizz’ for a numeric value or ‘Buzz’ for alphabetical value for all values in that column.

Example:

['d', 'x', 'T', 8, 'a', 9, 6, 2, 'V']

…should output:

['Buzz', 'Buzz', 'Buzz', 'Fizz', 'Buzz','Fizz', 'Fizz', 'Fizz', 'Buzz']

35. How do you get the Nth-highest salary from the Employee table without a subquery or CTE?

36. Given the following table named A:
```
  x
------
  2
 -2
  4
 -4
 -3    
  0
  2
```
Write a single query to calculate the sum of all positive values of x and he sum of all negative values of x.

37. Given the table mass_table:
```
weight
5.67
34.567
365.253
34
```
Write a query that produces the output:
```
weight	kg	gms
5.67	5	67
34.567	34	567
365.253	365	253
34	34	0
```
38. Consider the Employee table below.
```
Emp_Id	Emp_name	Salary	Manager_Id
10	Anil	50000	18
11	Vikas	75000	16
12	Nisha	40000	18
13	Nidhi	60000	17
14	Priya	80000	18
15	Mohit	45000	18
16	Rajesh	90000	–
17	Raman	55000	16
18	Santosh	65000	17
```
Write a query to generate below output:
```
Manager_Id	Manager	Average_Salary_Under_Manager
16	Rajesh	65000
17	Raman	62500
18	Santosh	53750
```
39. How do you copy data from one table to another table ?

40. Find the SQL statement below that is equal to the following: SELECT name FROM customer WHERE state = 'VA';
```
SELECT name IN customer WHERE state IN ('VA');
SELECT name IN customer WHERE state = 'VA';
SELECT name IN customer WHERE state = 'V';
SELECT name FROM customer WHERE state IN ('VA');
```
41. How to find a duplicate record?
* duplicate records with one field
* duplicate records with more than one field

### SQL DBs

42. What is a stored procedure?

43. Why would you use them?

44. What are atomic attributes?

45. Explain ACID props of a database

46. How to optimize queries?

47. What are windowing functions?

48. What is the difference between Clustered Index and Non-Clustered Index - with examples?

### No SQL DBs

49. What is a key-value (rowstore) store?

50. What is a columnstore? Diff between Row and col.store? 

# Answers
Questions 1-41: (https://www.toptal.com/sql/interview-questions)
Questions 42-50: (https://www.youtube.com/watch?v=WbqRH2r3N40&feature=youtu.be)


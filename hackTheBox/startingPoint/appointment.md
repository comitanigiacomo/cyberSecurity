<span style="color:cyan">**Question 1**</span> : What does the acronym SQL stand for?

    structured query language

<span style="color:cyan">**Question 2**</span> : What is one of the most common type of SQL vulnerabilities?

    SQL injection

<span style="color:cyan">**Question 3**</span> : What is the 2021 OWASP Top 10 classification for this vulnerability?

I've looked it on https://owasp.org/Top10/it/

   A03:2021-Injection  

<span style="color:cyan">**Question 4**</span> : What does Nmap report as the service and version that are running on port 80 of the target?

I used nMap to identify open ports and services

```
cmd : nmap -sV -p-

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-13 18:06 CET
Nmap scan report for 10.129.231.45
Host is up (0.042s latency).
Not shown: 65534 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.63 seconds

```

There I can see the service and version that are running on port 80

    Apache httpd 2.4.38 ((Debian))

<span style="color:cyan">**Question 5**</span> : What is the standard port used for the HTTPS protocol?

The standard port used for the HTTPS (Hypertext Transfer Protocol Secure) protocol is port 443

    443

<span style="color:cyan">**Question 6**</span> : What is a folder called in web-application terminology?

    directory

<span style="color:cyan">**Question 7**</span> : What is the HTTP response code is given for 'Not Found' errors?

When a server cannot find the requested resource or page, it responds with an HTTP status code of 404 to indicate that the requested resource is not available on the server.

    404

<span style="color:cyan">**Question 8**</span> : Gobuster is one tool used to brute force directories on a webserver. What switch do we use with Gobuster to specify we're looking to discover directories, and not subdomains?

To specify that we want to discover directories and not subdomains when using Gobuster, we can use the dir switch

    dir

<span style="color:cyan">**Question 9**</span> : What single character can be used to comment out the rest of a line in MySQL?

    #

<span style="color:cyan">**Question 10**</span> : If user input is not handled carefully, it could be interpreted as a comment. Use a comment to login as admin without knowing the password. What is the first word on the webpage returned?


Typing `admin'#` the access will be granted and the first word returned on the page will be congratulations

    congratulations

<span style="color:cyan">**Question 11**</span> : submit root flag

The flag is on the screen: 

    e3d0796d002a446c0e622226f42e9672
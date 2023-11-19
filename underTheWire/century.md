<h2><span style="color:cyan">Level 0</span></h2>

The goal of this level is to log into the game

Simply register via SSH at `century.underthewire.tech` with the username `century1` and the password `century1`

```
cmd : ssh century1@century.underthewire.tech

cmd : century1
```
Upon successful login, you will encounter the PowerShell prompt:

```
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century1\desktop>
```
<h2><span style="color:cyan">Level 1</span></h2>

The password for Century2 is the build version of the instance of PowerShell installed on this system.

Upon searching online, I found that the command `$PSVersionTable` prints various information about the PowerShell version in use.

```
cmd : $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.14393.5582
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...} 
BuildVersion                   10.0.14393.5582
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1

```
Here, I can see the build version of PowerShell: 

    10.0.14393.5582

Now, let's proceed to Level 2:

```
cmd : ssh century2@century.underthewire.tech

cmd : 10.0.14393.5582
```
<h2><span style="color:cyan">Level 2</span></h2>

The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

Firstly, let's identify the name of the file on the desktop.

```
cmd : ls

Mode                LastWriteTime         Length Name   
----                -------------         ------ ----  
-a----        8/30/2018   3:29 AM            693 443
```
The file name is `443`. After some online research, I found that the command `Invoke-RestMethod` is the cmdlet that performs the `wget`-like function within PowerShell. Now, I have the password for Level 3:

    invoke-webrequest443

<h2><span style="color:cyan">Level 3</span></h2>

The password for Century4 is the number of files on the desktop.

Initially, I tried running the `ls` command:

```
cmd : ls

-a----        8/30/2018   3:29 AM             33 countme1244
-a----        8/30/2018   3:29 AM             33 countme123
-a----        8/30/2018   3:29 AM             33 countme1245
-a----        8/30/2018   3:29 AM             33 countme125
-a----        8/30/2018   3:29 AM             33 countme1261
-a----        8/30/2018   3:29 AM             33 countme1289 
.
.
.
```
This displayed multiple files. Instead of manually counting, I found the necessary commands online. The combination of `Get-ChildItem` and `Measure-Object` allows us to count the number of files in a directory.

```
cmd : Get-ChildItem | Measure-Object

Count    : 123                       
Average  :                        
Sum      :                        
Maximum  : 
Minimum  :                                                                               
Property :
```
So, the number of files on the desktop is 123.

     123

<h2><span style="color:cyan">Level 4</span></h2>

The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

Firstly, let's see the names of the directories on the desktop.

```
cmd : ls

Mode                LastWriteTime         Length Name                                     
----                -------------         ------ ----                          
d-----        6/23/2022  10:30 PM                Can you open me                       
d-----        2/27/2023   4:55 PM                file                                  
d-----         2/8/2022  10:35 PM                Open.txt                          
-a----        6/17/2022   1:19 AM              0 FolderList                                
-a----        5/28/2023   5:44 PM              0 temp.text                               
-a----        1/17/2023   3:35 PM              0 text                                  
-a----        1/17/2023   3:35 PM              0 text.txt
```
Now, i only have to open the directory `can you open me`

By using the tab key to autocomplete the `cd` command, I'm able to access the directory

```
cmd : cd '.\Can you open me'
```
now i only have to get the file name

```
cmd : ls

Mode                LastWriteTime         Length Name                                    
----                -------------         ------ ----                                    
-a----        6/23/2022  10:24 PM             24 49125 
```
I have the password for the next level

    49125

<h2><span style="color:cyan">Level 5</span></h2>

The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

To discover the name of the file on the desktop:

```
cmd : ls

Mode                LastWriteTime         Length Name                                     
----                -------------         ------ ----                                  
-a----        8/30/2018   3:29 AM             54 3347   
```

The file name is `3347`. Now, let's find the name of the domain using `Get-AdDomainController`:
```
cmd : Get-AdDomainController

ComputerObjectDN           : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
```

The domain name is `underthewire.tech`. Thus, the password for the next level is:

    underthewire3347

<h2><span style="color:cyan">Level 6</span></h2>

The password for Century7 is the number of folders on the desktop.

The same command used in Level 3 can be used here:

```
cmd : Get-ChildItem | Measure-Object

Count    : 197                   
Average  :                        
Sum      :                        
Maximum  : 
Minimum  :                                                                               
Property :
```

Easy! The number of folders is `197`.

    197

<h2><span style="color:cyan">Level 7</span></h2>

The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

Firstly, I tried running the command `Get-ChildItem ..\ -Recurse -File -Filter readme*` to perform a recursive search for files with "readme" in their name.
From the output, I identified the file `Readme.txt`.

```
cmd : Get-ChildItem ..\ -Recurse -File -Filter readme* 

  Directory: C:\users\century7\Downloads

Mode                LastWriteTime         Length Name                                 
----                -------------         ------ ----           
-a----        8/30/2018   3:29 AM              7 Readme.txt   
```
Now i only have to cat the file

```
cmd : cd .\Downloads 

cmd : cat .\Readme.txt 

7points
```

I have the password for the next level

    7points

<h2><span style="color:cyan">Level 8</span></h2>

The password for Century9 is the number of unique entries within the file on the desktop.

My first thought was that i had to use a combination of commands

Searching online i found that the `Get-Unique` command compares each item in a sorted list to the next item, eliminates duplicates, and returns only one instance of each item

So, using it in combination of `cat` to extract the content of the file, and `Measure-Object` to measure the output, i might be able to discover the password

```
cmd : cat .\unique.txt | Get-Unique | Measure-Object

Count    : 696                     
Average  :                       
Sum      :                     
Maximum  :                        
Minimum  :                        
Property :
```
Found it !

    696

<h2><span style="color:cyan">Level 9</span></h2>

The password for Century10 is the 161st word within the file on the desktop.

I'll use `Get-Content` to obtain the file content as a single string. Then, I'll split it into an array of words using `.Split()` and retrieve the 161st word.

```
cmd : (Get-Content .\Word_File.txt -Raw).Split()[160]

pierid
```
The word is `pierid`.

    pierid

<h2><span style="color:cyan">Level 10</span></h2>

The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.

Firstly, let's find the name of the file on the desktop

```
Mode                LastWriteTime         Length Name                                     
----                -------------         ------ ----                                    
-a----        8/30/2018   3:34 AM             43 110  
```

The file name is `110`. Now, let's find the Windows Update service description:


I know that WMI provides information about the operating system and hardware of the machine. I'm also aware that in WMI, there is a class that represents Windows services: Win32_Service. Finally, searching online, I found that the Windows Update process has the name wuauserv.

Now that I want the description of the service, I only have to combine this information into a command:

```
cmd : Get-WmiObject -Query "SELECT * FROM Win32_Service WHERE Name = 'wuauserv'" | Select-Object -ExpandProperty Description

Enables the detection, download, and installation of updates for Windows and other programs. If this service is disabl
ed, users of this computer will not be able to use Windows Update or its automatic updating feature, and programs will
 not be able to use the Windows Update Agent (WUA) API.
```

I found the password for the next level!

    windowsupdates110

<h2><span style="color:cyan">Level 11</span></h2>

The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

I'll perform a recursive search to find all hidden files (those starting with a dot).

```
cmd : Get-ChildItem -Path . -Recurse -File -Filter . -Force

Directory: C:\users\century11\Downloads              

Mode                LastWriteTime         Length Name                
----                -------------         ------ ----               
--rh--        8/30/2018   3:34 AM             30 secret_sauce   
```
Upon reviewing all the results, this name caught my attention. So, I tried it, and I obtained access to the next level.

    secret_sauce

<h2><span style="color:cyan">Level 12</span></h2>

The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.

First, let's find the name of the file on the desktop:

```
cmd : ls

Mode                LastWriteTime         Length Name             
----                -------------         ------ ----  
-a----        8/30/2018   3:34 AM             30 _things 
```
The file name is `_things`. Now, let's find the description of the Domain Controller

I firstly tried running `Get-ADDomainController` to have informations about the domain controller, but i noted that there wasn't a description.

```
cmd : Get-ADDomainController

ComputerObjectDN           : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
Enabled                    : True
Forest                     : underthewire.tech
HostName                   : utw.underthewire.tech
InvocationId               : 09ee1897-2210-4ac9-989d-e19b4241e9c6
IPv4Address                : 192.99.167.156
IPv6Address                : 
IsGlobalCatalog            : True
IsReadOnly                 : False
LdapPort                   : 389
Name                       : UTW
```

So, I searched online and found that the command `Get-ADComputer` was similar. After reading the manual, I discovered that it accepts the name of the computer as input. So, I tried running the command `Get-ADComputer UTW -Properties Description`:

```
cmd : Get-ADComputer UTW -Properties Description   

Description       : i_authenticate
DistinguishedName : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DNSHostName       : utw.underthewire.tech
Enabled           : True
Name              : UTW
ObjectClass       : computer
ObjectGUID        : 5ca56844-bb73-4234-ac85-eed2d0d01a2e
SamAccountName    : UTW$
SID               : S-1-5-21-758131494-606461608-3556270690-1000
UserPrincipalName :
```

Now i have the password

    i_authenticate_things

<h2><span style="color:cyan">Level 13</span></h2>

The password for Century14 is the number of words within the file on the desktop.

I'll reuse the command from Level 9:

```
cmd : ((Get-Content .\countmywords -Raw).Split()).count

755
```
That's great!

    755

<h2><span style="color:cyan">Level 14</span></h2>

The password for Century15 is the number of times the word “polo” appears within the file on the desktop

I'll apply what I learned from previous challenges:

```
cmd :  ((get-content ./countpolos) -split ' ' | select-string -Pattern \bpolo\b).count

153
```

The final password is `153` ;)

    153



<h2><span style="color:cyan">Level 0</span></h2>

The goal of this level is to log into the game

Symply register via ssh to century.underthewire.tech whith `century1` as username and `century1` as password

```
cmd : ssh century1@century.underthewire.tech

cmd : century1
```

```
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century1\desktop>
```
<h2><span style="color:cyan">Level 1</span></h2>

The password for Century2 is the build version of the instance of PowerShell installed on this system.

Searching online i found that the command `$PSVersionTable` prints a bunch of informations about the PowerShell version I am actually using.

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
Here I can see the build version of the PowerShell: 

    10.0.14393.5582

I can now go on to level 2:

```
cmd : ssh century2@century.underthewire.tech

cmd : 10.0.14393.5582
```
<h2><span style="color:cyan">Level 2</span></h2>

The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

Firstly i wanna know the name of the file on the desktop.

```
cmd : ls

Mode                LastWriteTime         Length Name   
----                -------------         ------ ----  
-a----        8/30/2018   3:29 AM            693 443
```
So the name of the file is `443`

After that, searching online i found that the command `Invoke-RestMethod` is the cmdlet that performs the wget like function within PowerShell. Now i have the password for level 3:

    invoke-webrequest443

<h2><span style="color:cyan">Level 3</span></h2>

The password for Century4 is the number of files on the desktop.

I firstly tried by simple run the `ls` command 

```
cmd : ls

-a----        8/30/2018   3:29 AM             33 countme123                           -a----        8/30/2018   3:29 AM             33 countme1244
-a----        8/30/2018   3:29 AM             33 countme1245
-a----        8/30/2018   3:29 AM             33 countme125
-a----        8/30/2018   3:29 AM             33 countme1261
-a----        8/30/2018   3:29 AM             33 countme1289 
.
.
.
```
i don't wanna count by hand all of the file

So I searched online and i found the commands i need

The `Get-ChildItem` command retrieve objects (files and directories) in a specified location, while `Measure-Object` measure or calculate statistics on the objects sent to it. So by using a combination of those commands i can count the number of file in a directory
```
cmd : Get-ChildItem | Measure-Object

Count    : 123                       
Average  :                        
Sum      :                        
Maximum  : 
Minimum  :                                                                               
Property :
```
So the numer of files on the desktop is 123

     123

<h2><span style="color:cyan">Level 4</span></h2>

The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

At first i wanna see the name of the directories on desktop

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
Now i only have to open the directory `can you open me`

By using the tab key to autocomplete the `cd` command, i am able to access the directory

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

As usually i have to descover the nae of the file on the desktop

```
cmd : ls

Mode                LastWriteTime         Length Name                                     
----                -------------         ------ ----                                  
-a----        8/30/2018   3:29 AM             54 3347   
```

Now i need the name of the domain, that i can get running `Get-AdDomainController`

```
cmd : Get-AdDomainController

ComputerObjectDN           : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
```

I now have thepassword for the next level

    underthewire3347

<h2><span style="color:cyan">Level 6</span></h2>

The password for Century7 is the number of folders on the desktop.

I can use the same command used before on level 3

```
cmd : Get-ChildItem | Measure-Object

Count    : 197                   
Average  :                        
Sum      :                        
Maximum  : 
Minimum  :                                                                               
Property :
```

Easy :)

    197

<h2><span style="color:cyan">Level 7</span></h2>

The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

At first, i tried runing the command `Get-ChildItem ..\ -Recurse -File -Filter readme* ` to do a recursive search to find the file baing the research on the name of th file 

Upon all the output, i found it 

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

i have the password for the next level

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

I firstly used `Get-Content` to obtain the file content as a single strng. Then i divide it in an array of word using `.Split`. In the end i searched for the right word, remembering that indexes start from 0

```
cmd : (Get-Content .\Word_File.txt -Raw).Split()[160]

pierid
```

    pierid

<h2><span style="color:cyan">Level 10</span></h2>

The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.

Usual commands to find the name of the file on the desktop

```
Mode                LastWriteTime         Length Name                                     
----                -------------         ------ ----                                    
-a----        8/30/2018   3:34 AM             43 110  
```







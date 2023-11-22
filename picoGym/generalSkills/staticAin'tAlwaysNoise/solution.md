Can you look at the data in this binary: static? This BASH script might help!

At first i tryed running `static` using `chmod +x` to make it executable : 

```
cmd : chmod +x static

cmd : ./static

Oh hai! Wait what? A flag? Yes, it's around here somewhere!
```
Then I ran the other file: 

```
cmd : bash ltdis.sh

Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
```

It prints out an help message that explains how to use the program

Following the istructions, I tried the following: 

```
cmd : bash ltdis.sh static

Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

At this point, I ran `cat static.ltdis.strings.txt`

```
cmd :  cat static.ltdis.strings.txt 

 238 /lib64/ld-linux-x86-64.so.2
    361 libc.so.6
    36b puts
    370 __cxa_finalize
    37f __libc_start_main
    391 GLIBC_2.2.5
    39d _ITM_deregisterTMCloneTable
    3b9 __gmon_start__
    3c8 _ITM_registerTMCloneTable
    660 AWAVI
    667 AUATL
    6ba []A\A]A^A_
    .
    .
    .
```
Among all those files, my interest is to find if there is the flag, so I used the `grep` command as follows: 

```
cmd : cat static.ltdis.strings.txt | grep pico

1020 picoCTF{d15a5m_t34s3r_f6c48608}
```

Here's the flag!

    picoCTF{d15a5m_t34s3r_f6c48608}



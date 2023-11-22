Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`
Additional details will be available after launching your challenge instance.

At first i connected via `ssh` to the server as `ctf-player` using `b60940ca` as the password

```
cmd : ssh ctf-player@venus.picoctf.net -p 54874
```

Once logged in, I started looking around with `ls` and used `cat` on the files that caught my attention. In particular, in all the directories I found, there were always two types of files: 

- one containing a part of the final flag
- one containing the instructions for the next step

like this one: 

```
cmd : ls

1of3.flag.txt  instructions-to-2of3.txt
```

Where the content of the first file was `picoCTF{xxsh_` and the second was `Next, go to the root of all things, more succinctly /`

In the end, I Only had to combine the various part of the flag:

    picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

First of all, I notice that I can't view the file due to its format, so my only option is to run it.

When I try to run it, I notice that I don't have the permissions to do so. I analyze it further with `ll` and notice that the file currently cannot be executed:

```
cmd : ll 

-rw-r--r--. 1 giacomocomitani giacomocomitani 11K 21 nov 13.57 warm
```

I remedy this with `chmod +x` and run it, getting the following output:

    Hello user! Pass me a -h to learn what I can do!

My first idea was to pass the character `-h` to it via stdin using the command `echo -h | ./warm`, but it doesn't work.

I then try passing it from the command line as the first argument: `./warm -h`.

I get the flag:

    picoCTF{b1scu1ts_4nd_gr4vy_30e77291}


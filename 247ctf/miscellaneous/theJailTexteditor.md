<h2><span style="color:cyan">Description</span></h2>

We didn't have time to setup and test a proper jail, so this text editor will have to do for now. Can you break free?

<h2><span style="color:cyan">Solution</span></h2>

As I open the site, I can see that I'm in a `VIM` editor.

I know that in `VIM`, I can use arbitrary shell commands with `:!` in command mode.

At first, I tried to list all the files:

```
cmd : :! ls

run_for_flag

Press ENTER or type command to continue
```

So, following the instructions, I tried running the file:

```
cmd : :! ./run_for_flag
```

I Have the flag ;)

    247CTF{c69287be15653ac9ab47dcd3f2fcd8fa}
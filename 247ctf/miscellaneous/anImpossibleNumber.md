<h2><span style="color:cyan">Description</span></h2>

Can you think of a number which at the same time is one more than itself?

<h2><span style="color:cyan">Solution</span></h2>

At first, I downloaded the file provided by the challenge and analyzed the code: 

```c
#include <stdio.h>
int main() {
    int impossible_number;
    FILE *flag;
    char c;
    if (scanf("%d", &impossible_number)) {
        if (impossible_number > 0 && impossible_number > (impossible_number + 1)) {
            flag = fopen("flag.txt","r");
            while((c = getc(flag)) != EOF) {
                printf("%c",c);
            }
        }
    }
    return 0;
}
```
So, I have to provide the program with an input number that satisfies all the constraints, and the program will then give me the `flag`.

The only number that satisfies the condition imposed by the challenge is the maximum representable number on a predefined number of bits. We know that, due to the representation of numbers, if I add 1 to the maximum representable number, I will get a negative value, smaller than the starting number. Therefore, I initially tried with the maximum representable number on 64 bits, which is `9,223,372,036,854,775,807`

```
cmd : telnet 27acf7245466f6f4.247ctf.com 50440

cmd : 9223372036854775807

Connection closed by foreign host.
```

The server did not return the flag. I then tried with the maximum representable number on 32 bits, which is`2,147,483,647`. 

```
cmd : 2147483647

247CTF{38f5daf742a4b3d74b3a7575bf4d7d1e}
```

I have the flag!
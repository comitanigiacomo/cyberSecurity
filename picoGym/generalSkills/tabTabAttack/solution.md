Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames

At first I ran the `unzip` command to unzip the files:

```
cmd : unzip Addadshashanammu.zip

rchive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
```

So at this Point i Thought i had to open the file with the longest path:

```
cmd : cd cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/

cmd : ls -la

total 12
12 -rwxr-xr-x. 1 giacomocomitani giacomocomitani 8320 16 mar  2021 fang-of-haynekhtnamet
```
Now, I only have to execute the file:

```
cmd : ./fang-of-haynekhtnamet

*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}
```

The output reveals the flag:

    picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}

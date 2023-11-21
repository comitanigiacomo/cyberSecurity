Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

Per prima cosa noto che non posso visualizzare il file a causa del suo formato, per questo non mi resta che eseguirlo

Quando provo ad eseguirlo noto che non ho i permessi per farlo, lo analizzo meglio con ll e noto che attualmente il file non puo essere eseguito

```
cmd : ll 

-rw-r--r--. 1 giacomocomitani giacomocomitani 11K 21 nov 13.57 warm
```

Rimedio con `chmod +x`, e lo runno, ottenendo il seguente output:

    Hello user! Pass me a -h to learn what I can do!

La mia prima idea è stata quella di passsargli il carattere `-h` da stdin mediante pipe, con iil comando `echo -h | ./warm` ma non funziona.

Provo quindi a passarlo da linea di comando come primo argomento: `./warm -h`

Ottengo la flag 

    picoCTF{b1scu1ts_4nd_gr4vy_30e77291}


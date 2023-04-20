# hexa_stuff
My progress with the hexa robot


This is where you got the apk from
https://m.apkpure.com/hexa-programmable-robot/com.vincross.hexa

note that this is listed as being a potential trojan


---------


his is what a command can look like from strace [pid  1447] write(7</dev/ttymxc2>, "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1763V008P1398V007P1448V006P1737T0150##\r", 178) = 178


[11:07]Tremble: V00x = motor number, Pxxxx = servo position.
[11:08]Tremble: Above command can be run from terminal, this way: echo "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1763V008P1398V007P1448V006P1737T0150##\r" > /dev/ttymxc2


CMD7234 
V005 - P1533
V004 - P1383
V003 - P1692
V017 - P1515
V016 - P1430
V015 - P1768
V011 - P1424
V010 - P1413
V009 - P1713
V014 - P1544
V013 - P1359
V012 - P1670
V002 - P1515
V001 - P1450
V000 - P1763
V008 - P1398
V007 - P1448
V006 - P1737
T0150##\r" > /dev/ttymxc2


Things to test:

-Does the order matter?

-What does the T part do? Is this time spent to do it?

-I note that there were multiple "CMD" types when I was stracing Mind

-log the strace on mnt

-it there a way of tracking any communication to /dev/ttymxc2

-try strace with -e trace=file – Track file related syscalls

-can you get the camera working? Log what you have so far.

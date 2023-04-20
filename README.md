# hexa_stuff
My progress with the hexa robot


This is where you got the apk from
https://m.apkpure.com/hexa-programmable-robot/com.vincross.hexa

note that this is listed as being a potential trojan


---------


his is what a command can look like from strace [pid  1447] write(7</dev/ttymxc2>, "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1763V008P1398V007P1448V006P1737T0150##\r", 178) = 178


[11:07]Tremble: V00x = motor number, Pxxxx = servo position.
[11:08]Tremble: Above command can be run from terminal, this way: echo "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1763V008P1398V007P1448V006P1737T0150##\r" > /dev/ttymxc2
<BR><BR>

CMD7234  <BR>
V005 - P1533 <BR>
V004 - P1383 <BR>
V003 - P1692 <BR>
V017 - P1515 <BR>
V016 - P1430 <BR>
V015 - P1768 <BR>
V011 - P1424 <BR>
V010 - P1413 <BR>
V009 - P1713 <BR>
V014 - P1544 <BR>
V013 - P1359 <BR>
V012 - P1670 <BR>
V002 - P1515 <BR>
V001 - P1450 <BR>
V000 - P1763 <BR>
V008 - P1398 <BR>
V007 - P1448 <BR>
V006 - P1737 <BR>
T0150##\r" > /dev/ttymxc2
<BR><BR>

Things to test: <BR>
<BR>
-Does the order matter? <BR>
-What does the T part do? Is this time spent to do it? <BR>
-I note that there were multiple "CMD" types when I was stracing Mind <BR>
-log the strace on mnt <BR>
-it there a way of tracking any communication to /dev/ttymxc2 <BR>
-try strace with -e trace=file – Track file related syscalls <BR>
-can you get the camera working? Log what you have so far. <BR>

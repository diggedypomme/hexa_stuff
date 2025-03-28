# hexa_stuff
My progress with the hexa robot

Note that this is all just WIP so might not make sense for anyone viewing it.


This is where you got the apk from
https://m.apkpure.com/hexa-programmable-robot/com.vincross.hexa

note that this is listed as being a potential trojan


root
boot2mind


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
-try catting the  /dev/ttymxc2 as you issue this command. try catting some other ones as you do too. <BR>
-copy the full /dev list here
-there was a file somehere with the servo details. take them and put it here <BR>
  
   <BR> <BR>
-6 legs so 18 motors at 3 per motor: <BR>
-18 motors in total <BR>
-is the t part the head maybe? <BR>
-can you kill Mind and still have it checking camera etc? <BR>
-can you track it while taking a pic <BR>


V0001763V0011450V0021515V0031692V0041383V0051533V0061737V0071448V0081398V0091713V0101413V0111424V0121670V0131359V0141544V0151768V0161430V0171515

echo "CMD7234 V0001763V0011450V0021515V0031692V0041383V0051533V0061737V0071448V0081398V0091713V0101413V0111424V0121670V0131359V0141544V0151768V0161430V0171515T0150##\r" > /dev/ttymxc2


root@hexa:~# netstat -tulpn | grep LISTEN
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      1067/python
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      534/sshd
tcp6       0      0 :::7588                 :::*                    LISTEN      722/mind.d
tcp6       0      0 :::7589                 :::*                    LISTEN      722/mind.d
tcp6       0      0 :::7600                 :::*                    LISTEN      1743/explorer
tcp6       0      0 :::22                   :::*                    LISTEN      534/sshd

this address shows the images
https://192.168.0.222:7600/

     
     
     http://192.168.0.222:7588/ - this is the non https one

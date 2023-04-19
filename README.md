# hexa_stuff
My progress with the hexa robot


This is where you got the apk from
https://m.apkpure.com/hexa-programmable-robot/com.vincross.hexa

note that this is listed as being a potential trojan


---------


his is what a command can look like from strace [pid  1447] write(7</dev/ttymxc2>, "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1763V008P1398V007P1448V006P1737T0150##\r", 178) = 178
[11:07]Tremble: V00x = motor number, Pxxxx = servo position.
[11:08]Tremble: Above command can be run from terminal, this way: echo "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1763V008P1398V007P1448V006P1737T0150##\r" > /dev/ttymxc2

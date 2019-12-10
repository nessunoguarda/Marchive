#!/bin/bash
total=999
echo $total
for ((i=$total; i>=0; i--))
do
	a=`python3 /root/Challenge/HackTheBox/Misc/M0rsarchive/decript.py`	
	unzip -qP $a flag_$i.zip 
	cd flag
	echo $a 
	echo $i

done
cat flag

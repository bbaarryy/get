#!/bin/bash 


empty=$(sudo /usr/sbin/tlp start )
data=$(sudo tlp-stat -b)


#echo $data
#echo `expr match "$data" '.*\(.[a-b].*\)'`
capacity=`expr match "$data" '.*\(.[u-u][l-l][l-l].........*\)'`

capacity_cool=$(cat /sys/class/power_supply/BAT0/energy_full)

echo "$capacity_cool" >> stat
exit 0 #Выход с кодом 0 (удачное завершение работы скрипта)

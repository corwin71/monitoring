#!/bin/bash

#Specify all the domains you want to check
DOMAINS="domain.ru"

current_epoch=`date '+%s'`
for dm in $DOMAINS
do
  expiry_date=`whois $dm | egrep -i "Expiration Date:|free-date"| head -1 | awk '{print $NF}'`
 # echo -n " $dm - Expires on $expiry_date "
  expiry_epoch=`date --date="$expiry_date" '+%s'`
  epoch_diff=`expr $expiry_epoch - $current_epoch`
  days=`expr $epoch_diff / 86400`
  #echo " $days days remaining. "
done

if [[ $days -lt 50 ]]
	then curl -s -X POST https://api.telegram.org/bot -d chat_id= -d text="Domain registgation  expires less than 50 days"
fi
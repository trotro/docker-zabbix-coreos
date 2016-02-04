#!/bin/bash

# Check if the host's filesystems are Read Only

if [ `grep "\sro[\s,]" /coreos/proc/1/mounts | wc -l` -eq 2 ]
then 
  echo "OK"
else
  echo "NOK"
fi

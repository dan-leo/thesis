#!/bin/bash

echo "Wifi reconnection monitor started."

while true ; do
  if iwconfig wlan0 | grep -q "ESSID:off" ; then
    echo "Network connection down! Attempting reconnection."
    ifup --force wlan0
  fi
  sleep 5
done
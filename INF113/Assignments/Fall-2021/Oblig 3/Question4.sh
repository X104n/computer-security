#! /usr/bin/bash

while :
do
  top -n 1 >> $2
  sleep $1
done


#! /usr/bin/bash

mkdir $1
cd $1
for i in $(seq $2);
do
  mkdir "Question$i"
done

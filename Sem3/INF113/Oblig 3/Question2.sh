#! /bin/bash

mkdir -p $1

find . -type f -exec grep -q "$1" {} \; -print | xargs -I '{}' cp '{}' $1

#!/bin/bash
# script for Question 3 part F
# use a for loop


for i in `ls`; do
    echo "$i"
    wc -l < $i
done
 


#!/bin/bash
# script for Question 3 part F
# use a for loop

for i in $(find . -maxdepth 1 -type f -name "*.*"); do
    wordcount=$(cat "$i" |wc -l)
    echo "$i $wordcount"
done
 


#!/bin/bash
# Code for HW 1 Question 3

#Command to part B:

 grep '[0-9]*' apollo13.txt | wc -l   

#Command to part C:
grep --help | grep '^\s*\-c.*'
 

#Command to part D:

 find *.py | wc -l
 
#Command 1 for part E:
 
 ls -l | find . -type f ! -perm -o=rw | wc -l

 
 #Command 2 for part E:
 ls -l | find . -maxdepth 1 -type df ! -perm -o=rw ! -name . | wc -l

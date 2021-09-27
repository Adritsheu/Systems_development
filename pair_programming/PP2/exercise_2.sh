#!/bin/bash
for i in `find *  -maxdepth 0  -perm -u+x`; do
	echo "$i"
done 

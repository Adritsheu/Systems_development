#!/bin/bash

read -r -p "Please name a file: " Filename
echo
git add $Filename
git status
read -r -p "Would you like to continue:Y or N  "  Reply 
echo
if [ "$Reply" = "N" ]; then 
	exit 1
fi
if [ "$Reply" = "Y" ]; then 
	read -r -p "Please tell me a message " Message	
fi
git commit -m $Message
git status
read -r -p "Would you like to continue: Y or N " Reply2
echo
if [ "$Reply2" = "N" ]; then
	exit 1
fi
if [[ ! $Reply2 = [Y]$ ]];
then
	git push
	echo "git push executed" 
fi

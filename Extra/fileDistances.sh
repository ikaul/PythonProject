#!/bin/bash
filePath=$(find ~/Projects -name "xs.py")
if [ -z $filePath ]; then
	echo "-1"
else
	echo $filePath
fi

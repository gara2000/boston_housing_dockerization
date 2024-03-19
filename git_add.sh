#!/bin/bash

WORKDIR=$(dirname $0)
cd $WORKDIR

git add .

echo -n "Give a commit message [default: new commit]:"
read msg

if [ -z $msg ]; then
	git commit -m "new commit"
else
	git commit -m "$msg"
fi

git push -u origin main

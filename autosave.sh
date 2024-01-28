#!/bin/sh
# makes a git & push every 2 minute while working
while true
do
    git add . && git commit -m "sauvegarde automatique" && git push
    sleep 2m
done
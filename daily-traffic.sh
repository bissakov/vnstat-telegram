#!/bin/bash

sudo vnstat -u
#sudo touch ~/scripts/images/daily.png
sudo vnstati -d -i ens3 -o ~/scripts/images/daily.png
sudo vnstat -d -i ens3 --json > ~/scripts/data.json

~/scripts/sendMessage.py

exit 0;
#!/bin/bash

sudo vnstat -u
sudo touch ~/scripts/images/daily.png
sudo vnstati -d -i ens3 -o ~/scripts/images/daily.png
sudo vnstat -d -i ens3 --json > data.json

./sendMessage.py

exit 0;
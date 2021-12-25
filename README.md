# vnstat-telegram
Send vnstat network monitoring activity via Telegram bot

### Send activity monthly activity every day at 10AM and daily traffic every 2 hours from 8AM to 0AM using crontab
0 10 * * * /bin/bash ~/scripts/monthly-traffic.sh  
0 0,8,10,12,14,16,18,20,22 * * * /bin/bash ~/scripts/daily-traffic.sh
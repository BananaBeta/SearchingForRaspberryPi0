# SearchingForPi0
This script will scan resellers' websites to check Raspberry pi zero stocks.
Adafruit, Element14 and Raspberry's Swag Store are scanned.

Install this script, define your email account credentials inside the script, and let it run automatically every 5 minutes or so. To do this, the script need to be added to your cron:
    sudo crontab -e
  add the following line:
    */5 * * * * python /path_to_script/SearchingForPi0.py 2>&1

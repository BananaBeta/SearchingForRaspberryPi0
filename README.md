# SearchingForRaspberryPi0
#Introduction
This script will scan resellers' websites to check Raspberry pi zero stocks.
Adafruit, Element14 and Raspberry's Swag Store are scanned.
You can run this script from another Raspberry Pi, you'll receive an email when the Pi Zero will become available.
This script uses _BeautifulSoup_ for HTML parsing.

#Installation
Pull this repository on your RaspberryPi.
Define your email account credentials inside the script:

    # set your email credentials here
    my_email_adress='XXX@YYY.com'; email_pwd = 'ZZZ';

Define the list of recipients of the email alert:

    # set the list of email adresses that should receive the alert
    recipients = [my_email_adress, 'other_email_adress@XXX.com'];

Make this script run every X minutes by adding a planned execution to cron

    sudo crontab -e

add the following line (just replace _path_to_script_ with the actual path to the script):

    */5 * * * * python /path_to_script/SearchingForRaspberryPi0.py 2>&1
The script will run every 5 minutes with this example.

#Now what?
Let it run. When there will be stock on any of the scanned website, you should get an email.
You can check the email settings by temporarily replacing the test by:

    #test = test_adafruit or test_swag or test_element14
    test=True

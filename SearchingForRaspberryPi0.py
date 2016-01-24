import BeautifulSoup
import requests
import smtplib
import os
from email.mime.text import MIMEText
from time import gmtime, strftime

# set your email credentials here
my_email_adress='XXX@YYY.com'; email_pwd = 'ZZZ';

# set the list of email adresses that should receive the alert
recipients = [my_email_adress, 'other_email_adress@XXX.com'];

def check_adafruit(url_to_check):
    html_webpage = requests.get(url_to_check);
    soup = BeautifulSoup.BeautifulSoup(html_webpage.text);
    results = soup.findAll("meta",{"name" : "twitter:data2"});
    return results[0]["content"] != u'OUT OF STOCK'

def check_swag_store(url_to_check):
    html_webpage = requests.get(url_to_check);
    soup = BeautifulSoup.BeautifulSoup(html_webpage.text);
    results=soup.find(attrs={"class" : "stock-level out-of-stock"})
    return results == None

def check_element14(url_to_check):
    html_webpage = requests.get(url_to_check);
    soup = BeautifulSoup.BeautifulSoup(html_webpage.text);
    res = soup.find("table",{"class" : "comptable"});
    res = res.findAll("th");
    sold_out = False;
    for th in res:
        st = res[1].text;
        if(st.find("Raspberry Pi Zero")!=-1):
            if(st.find("SOLD OUT")!=-1):
                sold_out=True;
    return not sold_out

current_dir = os.path.dirname(os.path.realpath(__file__))+'/';

# URLs to scan
url_adafruit = "https://adafruit.com/product/2817";
url_element14 = "http://www.element14.com/community/community/raspberry-pi";
url_swag = "http://swag.raspberrypi.org/collections/pi-zero/products/pi-zero-kit";

fhandle = open(current_dir+'check_pi_zero_availibility.log','a')
fhandle.write('==== ' + strftime("%a %d %b %Y %H:%M:%S", gmtime()) + ' ====')
test_adafruit = check_adafruit(url_adafruit)
fhandle.write('    ('+'%s' % test_adafruit)
test_swag = check_swag_store(url_swag)
fhandle.write(',' + '%s' % test_swag)
test_element14 = check_element14(url_element14)
fhandle.write(','+ '%s' % test_element14 + ')\n');
fhandle.close()

test = test_adafruit or test_swag or test_element14
if(test==True):
    if(os.path.isfile(current_dir+'/stop_emails.log')==False):
        msg=MIMEText('    -> Adafruit: '+ '%s' % test_adafruit + '\t %s' % url_adafruit + '\n' + '    -> Swag: '+ '%s' % test_swag + '\t %s' % url_swag  + '\n' + '    -> Element14: '+ '%s' % test_element14 + '\t %s' % url_element14  + '\n');
        msg['Subject'] = 'Raspberry Pi Zero is available'
        msg['From']=me;
        msg['To']=", ".join(recipients);
        s = smtplib.SMTP('smtp.gmail.com',587);
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(my_email_adress,email_pwd)
        s.sendmail(msg["From"], recipients, msg.as_string())
        s.close()
        f=open('./stop_emails.log','w');
        f.write('stop');
        f.close()

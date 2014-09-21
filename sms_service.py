#!/usr/bin/python


import os
import urllib

# path = '/srv/samba/share'
def get_files(path):
    data={}
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            #print os.path.join(dirname, filename)
            f=open(os.path.join(dirname, filename),'rU')
            filecontents=f.readlines()
            #print filecontents
            for lines in filecontents:
                field= lines.split(',')
                data['mobile1']=field[0]
                data['mobile2']=field[1]
                data['greeting']=field[2]
                data['msg']=field[3]
            #print data
            send_sms(data)
            f.close()
            os.remove(os.path.join(dirname, filename))

def send_sms(dict_data):
    #http://newz.teczeesystems.com/sendsms?uname=yourUsername&pwd=yourPassword&senderid=yourSenderid&to=9444xxxxxx&msg=yourMessage&route=yourRoute
    response = urllib.urlopen("http://newz.teczeesystems.com/sendsms?uname=hashirharis&pwd=abcd_1234&senderid=AMMTRS&to=" + dict_data['mobile2'] + "&msg=" + dict_data['greeting'] + "," + dict_data['msg']+  "&route=T")




def main():
    get_files('/srv/samba/share')

if __name__ == '__main__':
    main()

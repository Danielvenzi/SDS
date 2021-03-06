import os
import schedule
import time

def godata_dump():

    os.system("systemctl stop godata ; sleep 10 ; cd /godata-bckp ; rm -rf ./dump/ ; mongodump")
    os.system("rm -f /var/www/html/dump.tar.gz ; tar -zcvf /var/www/html/dump.tar.gz /godata-bckp/dump")
    os.system("systemctl start godata")
if __name__ == "__main__":

    schedule.every().monday.at("03:00").do(godata_dump)
    schedule.every().tuesday.at("03:00").do(godata_dump)
    schedule.every().wednesday.at("03:00").do(godata_dump)
    schedule.every().thursday.at("03:00").do(godata_dump)
    schedule.every().friday.at("03:00").do(godata_dump)
    schedule.every().saturday.at("03:00").do(godata_dump)
    schedule.every().sunday.at("03:00").do(godata_dump)

    while True:
        schedule.run_pending()
        time.sleep(1)
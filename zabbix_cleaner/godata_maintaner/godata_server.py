import os
import schedule
import time
import datetime

def godata_get_and_save():

    os.system("bash /infra-centeias/backups/godata/godata_server.sh")
    now = datetime.datetime.now()
    os.system("mv /infra-centeias/backups/godata/dump.tar.gz /infra-centeias/backups/godata/{0}-{1}-{2}.tar.gz".format(now.day,now.moth,now.year))

if __name__ == "__main__":

    schedule.every().monday.at("03:15").do(godata_get_and_save)
    schedule.every().tuesday.at("03:15").do(godata_get_and_save)
    schedule.every().wednesday.at("03:15").do(godata_get_and_save)
    schedule.every().thursday.at("03:15").do(godata_get_and_save)
    schedule.every().friday.at("03:15").do(godata_get_and_save)
    schedule.every().saturday.at("03:15").do(godata_get_and_save)
    schedule.every().sunday.at("03:15").do(godata_get_and_save)

    while True:
        schedule.run_pending()
        time.sleep(1)
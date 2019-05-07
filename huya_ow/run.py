import os
import time


while True:
    os.system("scrapy runspider ow.py --loglevel='WARNING'")
    time.sleep(60)
    print('--------------------------------------')

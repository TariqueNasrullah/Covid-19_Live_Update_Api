import logging
import subprocess
import setproctitle
import time

setproctitle.setproctitle('Scraper Country')

logging.basicConfig(filename='scraper.log',level=logging.DEBUG, format='%(asctime)s %(message)s')

while True:
    process = subprocess.Popen(['scrapy', 'crawl', 'country'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    while True:
        return_code = process.poll()

        if return_code is not None:
            if return_code == 0:
                logging.info('OK')
            else:
                logging.error('Crawl Unssuccessful RETCODE: {}'.format(return_code))
            break
    time.sleep(20)
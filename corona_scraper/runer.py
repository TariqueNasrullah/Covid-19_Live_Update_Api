import logging
import subprocess

logging.basicConfig(filename='scraper.log',level=logging.DEBUG, format='%(asctime)s %(message)s')


process = subprocess.Popen(['scrapy', 'crawl', 'corona'], 
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
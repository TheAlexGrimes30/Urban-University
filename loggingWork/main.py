import requests as rq
import logging

from requests import RequestException

logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('success')
bad_logger = logging.getLogger('bad')
blocked_logger = logging.getLogger('blocked')

success_handler = logging.FileHandler('success_responses.log')
bad_handler = logging.FileHandler('bad_responses.log')
blocked_handler = logging.FileHandler('blocked_responses.log')

formatter = logging.Formatter('%(levelname)s: %(message)s')
success_handler.setFormatter(formatter)
bad_handler.setFormatter(formatter)
blocked_handler.setFormatter(formatter)

success_logger.addHandler(success_handler)
bad_logger.addHandler(bad_handler)
blocked_logger.addHandler(blocked_handler)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            success_logger.info(f"'{site}', response - {response.status_code}")
        else:
            bad_logger.warning(f"'{site}', response - {response.status_code}")
    except TimeoutError:
        blocked_logger.error(f"'{site}', NO CONNECTION")
    except ConnectionError:
        blocked_logger.error(f"'{site}', NO CONNECTION")
    except RequestException as e:
        blocked_logger.error(f"'{site}', NO CONNECTION")
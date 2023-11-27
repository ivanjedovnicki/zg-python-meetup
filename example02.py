# Unless a mechanism for stopping a running thread is in place, there is no graceful way
# to shut it down. The simplest mechanism to do that is a thread safe flag called Event.
# Discussion:
#  * How to stop a running thead?

from logger import init_logger

init_logger()

import logging
import threading
import time

stop_event = threading.Event()


def background(sleep: float = 1):
    count = 1
    while True:
        if stop_event.is_set():
            logging.info('Stopping.')
            break
        logging.info(f'Count: {count}.')
        count += 1
        time.sleep(sleep)
    logging.info('Stopped.')


t = threading.Thread(target=background, args=(5,), name='Background')
t.start()

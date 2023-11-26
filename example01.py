# Launching a thread in Python is easy using the threading module. Just give the target
# function to be called with the specified args and kwargs. But is stopping the thread
# easy? How do you stop a running thread?
# Discussion:
#  * How to stop a running thead?

from logger import init_logger

init_logger()

import logging
import threading
import time


def target(sleep: float = 1):
    count = 1
    while True:
        logging.info(f'Count: {count}.')
        count += 1
        time.sleep(sleep)


t = threading.Thread(target=target, args=(10,), name='Background')
t.start()

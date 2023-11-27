# Launching a thread in Python is easy using the threading module. Just give the target
# function to be called with the specified args and kwargs.
# Discussion:
#  * What is the difference between a thread and a process?
#  * Isn't Python single-threaded?
#  * Are those real OS threads?
#  * Who controls the switching of threads?

from logger import init_logger

init_logger()

import logging
import threading
import time


def background(sleep: float = 1):
    count = 1
    while True:
        logging.info(f'Count: {count}.')
        count += 1
        time.sleep(sleep)


t = threading.Thread(target=background, args=(10,), name='Background')
t.start()

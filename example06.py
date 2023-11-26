# What is a lock anyway?
#
# Discussion:
#  * Synchronization primitives in general
#  * Safety or programming discipline?

import logging

from logger import init_logger

init_logger()

import time
import threading

lock = threading.Lock()


def lock_thread():
    lock.acquire()
    logging.info('Lock acquired.')
    time.sleep(10)
    lock.release()
    logging.info('Lock released.')


threading.Thread(target=lock_thread).start()

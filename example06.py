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
proceed = threading.Condition()


def lock_target():
    lock.acquire()
    logging.info('Lock acquired.')
    time.sleep(10)
    lock.release()
    logging.info('Lock released.')


def wait_target():
    with proceed:
        logging.info('Waiting...')
        proceed.wait()
        logging.info('Proceeding.')
    logging.info('Done.')


lock_thread = threading.Thread(target=lock_target, name='Lock thread')
waiter_threads = [
    threading.Thread(target=wait_target, name=f'Waiter {i}') for i in range(3)
]

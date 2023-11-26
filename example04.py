# A common problem solved by threads involves one thread producing some data, and
# another consuming or processing that data. The queue.Queue data structure is used for
# thread-safe communication.
#
# Discussion:
#  * multiple producers and consumers

import logging
import queue
import threading
import time

from logger import init_logger

init_logger()

qq = queue.Queue()
_poison_pill = object()


def producer(q: queue.Queue, sleep: float = 1):
    for i in range(10):
        time.sleep(sleep)
        logging.info(f'Producing {i}.')
        q.put(i)
    logging.info('Producer done.')
    q.put(_poison_pill)


def consumer(q: queue.Queue, sleep: float = 3):
    while True:
        time.sleep(sleep)
        item = q.get()
        logging.info(f'Consuming {item}.')
        if item is _poison_pill:
            # What happens without the poison pill?
            logging.info('Got poison pill.')
            break


t1 = threading.Thread(target=producer, args=(qq,))
t2 = threading.Thread(target=consumer, args=(qq,))

t1.start()
t2.start()

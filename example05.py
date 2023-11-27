# The queue.Queue data structure is a good way for communicating between threads.
# However, there are some caveats. Not all methods from queue.Queue are thread safe.
#
# Discussion:
#  * Race conditions
#  * How to help stuck consumers?
#  * Understanding race condition by inspecting bytecode

import logging
import queue
import threading

from logger import init_logger

init_logger()


def consumer(q: queue.Queue):
    item = None
    while not q.empty():
        item = q.get()
    logging.info(f'Consumer done. Last item was {item}.')


def producer(q: queue.Queue, size=100_000):
    for i in range(size):
        q.put(i)
    logging.info('Producer done.')


qq = queue.Queue()

producers = [
    threading.Thread(
        target=producer, args=(qq,), kwargs={'size': 10_000}, name=f'Producer {i}'
    )
    for i in range(30)
]
consumers = [
    threading.Thread(target=consumer, args=(qq,), name=f'Consumer {i}')
    for i in range(10)
]

for t in producers + consumers:
    t.start()

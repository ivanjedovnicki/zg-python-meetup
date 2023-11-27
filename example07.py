# Discussion:
#  * How many I/O bound threads can the interpreter handle?
#  * How many threads need to be spawned so that performance degrades?

import logging
import threading
import time

from logger import init_logger

init_logger()

from iobound import io_bound

num_threads = 1
io_bound_threads = [
    threading.Thread(target=io_bound, args=(20, 1), name=f'I/O bound {i}')
    for i in range(1, num_threads + 1)
]

t1 = time.perf_counter()
for thread in io_bound_threads:
    thread.start()
for thread in io_bound_threads:
    thread.join()
t2 = time.perf_counter()

logging.info(f'Elapsed time for {num_threads} threads is {t2 - t1}.')
# print(f'Elapsed time for {num_threads} threads is {t2 - t1}.')

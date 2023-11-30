# Discussion:
#  * Why do many CPU bound threads proceed concurrently?
#  * Shouldn't the GIL lock one thread?
#  * Since there are no sleeps, network waits, who releases the GIL and when?

import logging
import threading
import time
import sys
from logger import init_logger

init_logger()

from cpubound import cpu_bound

LOW_SWITCH_INTERVAL = 5e-6  # 5 microseconds
DEFAULT_SWITCH_INTERVAL = 5e-3  # 5 milliseconds
HIGH_SWITCH_INTERVAL = 1  # 1 second

sys.setswitchinterval(HIGH_SWITCH_INTERVAL)
logging.info(f'Thread switch interval is {sys.getswitchinterval()}.')

num_threads = 1
cpu_bound_threads = [
    threading.Thread(target=cpu_bound, args=(250_000_000,), name=f'CPU bound {i}')
    for i in range(1, num_threads + 1)
]

t1 = time.perf_counter()
for thread in cpu_bound_threads:
    thread.start()
for thread in cpu_bound_threads:
    thread.join()
t2 = time.perf_counter()

logging.info(f'Elapsed time for {num_threads} threads is {t2 - t1}.')

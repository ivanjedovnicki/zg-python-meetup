# I/O bound code releases the GIL, and gives a chance for other threads to acquire the
# GIL. I/O bound problems involve system calls, sleeping, waiting on a network. They
# are characterized by a lot of waiting, i.e. the CPU spends a lot of time doing
# nothing.
# Discussion:
#  * Is solving I/O bound problems in Python an example of cooperative or preemptive
#    multitasking?

import logging
import time


def io_bound(iterations: int, sleep: float):
    for i in range(1, iterations + 1):
        logging.info(f'Iterations: {i}/{iterations}.')
        time.sleep(sleep)
    logging.info('Done.')

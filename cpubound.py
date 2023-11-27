# CPU bound problem are bound by how fast the CPU can perform the instructions generated
# from a program. It involves computationally heavy workloads, such as multiplying
# matrices, long iterations, and anything else thad keeps the CPU busy.

import logging


def cpu_bound(iterations: int):
    delta = round(iterations / 100)
    for i in range(1, iterations + 1):
        q, r = divmod(i, delta)
        if r == 0:
            logging.info(f'Progress {q}/100.')
    logging.info('Done.')

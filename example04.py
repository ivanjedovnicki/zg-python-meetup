# What happens to the main thread if some thread throws an unhandled exception?
#
# Discussion:
#  * .join()
#  * How do we stop this consumer thread? Is threading.Event enough?
#  * How to handle exceptions from another thread?

import logging
import time

from logger import init_logger

init_logger()

import queue
import threading
from typing import NamedTuple, Optional


class Task(NamedTuple):
    a: float
    b: float
    opcode: str
    result: Optional[float] = None


class Calculator:
    def __init__(self):
        self._task_queue: queue.Queue[Task] = queue.Queue()
        self._result_queue: queue.Queue[Task] = queue.Queue()
        self._background_thread = threading.Thread(
            target=self._background, name='Background'
        )
        self._consumer_thread = threading.Thread(
            target=self._task_consumer, name='Task consumer'
        )
        self._count = 0

    def start(self):
        self._background_thread.start()
        self._consumer_thread.start()

        # self._background_thread.join()
        # self._consumer_thread.join()

    def put(self, task: Task):
        logging.info(f'Putting task {task} into the task queue.')
        self._task_queue.put(task)

    def _background(self):
        while True:
            logging.info(f'Count: {self._count}.')
            logging.info(f'Numer of active threads is {threading.active_count()}.')
            time.sleep(15)

    def _task_consumer(self):
        while True:
            task = self._task_queue.get()
            logging.info(f'Got task {task}.')
            match task.opcode:
                case '+':
                    result = task.a + task.b
                case '-':
                    result = task.a - task.b
                case '*':
                    result = task.a * task.b
                case '/':
                    result = task.a / task.b
                case _:
                    raise ValueError(f'Invalid opcode {task.opcode}.')
            task_result = Task(task.a, task.b, task.opcode, result)
            logging.info(f'Putting result {task_result} into the result queue.')
            self._result_queue.put(task_result)


calculator = Calculator()
task_1 = Task(1, 2, '+')
task_2 = Task(1, 0, '/')

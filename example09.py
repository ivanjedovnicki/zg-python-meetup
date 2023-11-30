# Launching parallel I/O bound tasks is well-supported in the standard library.
# Problem: We need to fetch data from multiple urls concurrently. What if some requests
# fail? How do we reschedule only the failed requests?

import logging
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from logger import init_logger

init_logger()

CHARS = list(string.ascii_letters)


class CharToCodepointError(Exception):
    pass


def char_to_codepoint(char: str) -> int:
    logging.info(f'Getting codepoint for {char}.')
    time.sleep(random.random())
    fail = [True, True, False]
    if random.choice(fail):
        logging.info(f'Getting codepoint for {char} failed.')
        raise CharToCodepointError
    codepoint = ord(char)
    logging.info(f'Getting codepoint {char} succeeded.')
    return codepoint


with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {char: executor.submit(char_to_codepoint, char) for char in CHARS}


class CharToCodepointConverter:
    # Discussion: Are there any race conditions here?
    def __init__(self, max_workers: int):
        self._max_workers = max_workers
        self._results = {char: None for char in CHARS}

    def convert(self):
        while not self._all_done():
            self._schedule()

    def _schedule(self):
        with ThreadPoolExecutor(max_workers=self._max_workers) as e:
            fs = {e.submit(char_to_codepoint, c): c for c in self._pending()}
            for f in as_completed(fs):
                try:
                    codepoint = f.result()
                except CharToCodepointError as e:
                    logging.error(e)
                else:
                    char = fs[f]
                    self._results[char] = codepoint

    def _pending(self) -> list[str]:
        return [char for char in self._results if self._results[char] is None]

    def _all_done(self) -> bool:
        return not bool(self._pending())


converter = CharToCodepointConverter(max_workers=10)

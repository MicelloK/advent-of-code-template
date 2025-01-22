import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Dict

import dotenv
import requests
from requests.utils import cookiejar_from_dict

@dataclass(frozen=True)
class PuzzleResult:
    name: str
    p1_result: Any
    p2_result: Any

class BasePuzzle(ABC):
    def __init__(self, puzzle_name: str):
        self._puzzle_name = puzzle_name

    def solve(self, data: str) -> PuzzleResult:
        parsed_data = self._parse_data(data)

        puzzle1_result = BasePuzzle._solve_puzzle(self._puzzle1, parsed_data)
        puzzle2_result = BasePuzzle._solve_puzzle(self._puzzle2, parsed_data)
        return PuzzleResult(name=self._puzzle_name, p1_result=puzzle1_result, p2_result=puzzle2_result)
    
    def _solve_puzzle(puzzle_method, parsed_data) -> Any:
        try:
            return puzzle_method(**parsed_data)
        except NotImplementedError:
            return 'Not implemented'

    @abstractmethod
    def _parse_data(self, data: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def _puzzle1(self, **kwargs) -> Any:
        pass

    @abstractmethod
    def _puzzle2(self, **kwargs) -> Any:
        pass

@lru_cache(maxsize=None)
def get_input(year: int, day: int) -> str:
    dotenv.load_dotenv()

    session = requests.session()
    cookies = {
        'session': os.getenv('AOC_SESSION_COOKIE')
    }
    cookies = cookiejar_from_dict(cookies)
    session.cookies.update(cookies)

    response = session.get(f'https://adventofcode.com/{year}/day/{day}/input')
    if response.ok:
        return response.content.decode(encoding=response.encoding)
    raise RuntimeError('Failed to download data. Check if session cookie is set.')

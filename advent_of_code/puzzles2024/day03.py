from typing import Any, Dict
from advent_of_code.utils import BasePuzzle

class Puzzle(BasePuzzle):
    def __init__(self):
        super().__init__('Day 3: Mull It Over')
    
    def _parse_data(self, data: str) -> Dict[str, Any]:
        """
        Parses the raw input data into a format suitable for solving the puzzle.

        Note:
            - You can implement the parsing logic here if the input data 
              requires preprocessing (e.g., splitting lines, converting to integers).
            - If no parsing is necessary, you can leave this method as is
              and use the raw input directly in the solution functions via kwargs['data'].
        """
        return {'data': data}
    
    def _puzzle1(self, **kwargs):
        """Solve part 1 of the puzzle"""
        # Implement your puzzle 1 logic here
        raise NotImplementedError
    
    def _puzzle2(self, **kwargs):
        """Solve part 2 of the puzzle"""
        # Implement your puzzle 2 logic here
        raise NotImplementedError
    
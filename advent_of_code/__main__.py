import importlib
import argparse
from typing import List
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
from rich.table import Table

from advent_of_code import utils

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', type=int)
    return parser.parse_args()

def create_table(title: str, results: List[utils.PuzzleResult]) -> Table:
    table = Table(title=title)
    table.add_column('Puzzle Name', style='cyan', justify='center')
    table.add_column('Puzzle 1 Result', style='green', justify='right')
    table.add_column('Puzzle 2 Result', style='yellow', justify='right')

    for result in results:
        table.add_row(result.name, str(result.p1_result), str(result.p2_result))

    return table

def process_puzzle(year: int, day: int) -> utils.PuzzleResult:
    puzzle_name = f"Day {day}"
    try:
        module = importlib.import_module(f"puzzles{year}.day{day}")
        puzzle: utils.BasePuzzle = module.Puzzle()
        puzzle_name = puzzle._puzzle_name
        data = utils.get_input(day)
        return puzzle.solve(data)
    except (NotImplementedError, ModuleNotFoundError):
        return utils.PuzzleResult(name=puzzle_name, p1_result='Not implemented', p2_result='Not implemented')
    
def calculate_results(year: int) -> List[utils.PuzzleResult]:
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda day: process_puzzle(year, day), range(1, 26)))
    
if __name__ == '__main__':
    args = parse_args()
    results = calculate_results(args.year)

    result_table = create_table(f"Advent of Code {args.year}", results)
    Console().print(result_table)

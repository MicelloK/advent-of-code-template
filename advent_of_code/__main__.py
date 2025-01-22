import importlib
import argparse
import datetime
from typing import List
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
from rich.table import Table

from advent_of_code import utils

def aoc_editions() -> List[int]:
    current_date = datetime.datetime.now().date()
    last_year = current_date.year
    if current_date.month < 12:
        last_year -= 1
    return list(range(2015, last_year+1))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', default=2015, choices=aoc_editions(), type=int)
    return parser.parse_args()

def create_table(title: str, results: List[utils.PuzzleResult]) -> Table:
    table = Table(title=title, padding=(0, 2))
    table.add_column('Puzzle Name', style='cyan', justify='left')
    table.add_column('Puzzle 1 Result', style='green', justify='right')
    table.add_column('Puzzle 2 Result', style='yellow', justify='right')

    for result in results:
        table.add_row(result.name, str(result.p1_result), str(result.p2_result))

    return table

def get_day_str(day: int) -> str:
    if day < 10:
        return f"0{day}"
    return str(day)

def process_puzzle(year: int, day: int) -> utils.PuzzleResult:
    puzzle_name = f"Day {get_day_str(day)}"
    try:
        module = importlib.import_module(f"puzzles{year}.day{get_day_str(day)}")
        puzzle: utils.BasePuzzle = module.Puzzle()
        puzzle_name = puzzle._puzzle_name
        data = utils.get_input(year, day)
        return puzzle.solve(data)
    except ModuleNotFoundError:
        return utils.PuzzleResult(name=puzzle_name, p1_result='Not implemented', p2_result='Not implemented')
    
def calculate_results(year: int) -> List[utils.PuzzleResult]:
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda day: process_puzzle(year, day), range(1, 26)))
    
if __name__ == '__main__':
    args = parse_args()
    results = calculate_results(args.year)

    result_table = create_table(f"Advent of Code {args.year}", results)
    print()
    Console().print(result_table)

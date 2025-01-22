# advent-of-code-template

Template for solving aoc puzzles.

## Usage

### Cookie

Create an `.env` file in the root directory and add `AOC_SESSION_COOKIE`. Download value from advent of code website (`session` cookie).

A sample file may look like this:
```python
AOC_SESSION_COOKIE = "0bdcfbee67400ed12a1...5b79590517d14aabae"
```

### Puzzles

Implement puzzles logic in a dedicated area in `advent_of_code/puzzles{year}` module. Each day has a seperate module in which there is a class with methods that claculate the result of the puzzle.

```python
class Puzzle(BasePuzzle):
    def __init__(self):
        super().__init__('Day 1: Historian Hysteria')
    
    def _parse_data(self, data: str) -> Dict[str, Any]:
        # Parse input data into format suitable for solving puzzles. 
        ...
    
    def _puzzle1(self, **kwargs):
        # Implement your puzzle 1 logic here
        ...
    
    def _puzzle2(self, **kwargs):
        # Implement your puzzle 2 logic here
        ...
```

### Run

Install Poetry. Official [Guide](https://python-poetry.org/docs).

```bash
# Create virtual environment
$ poetry install

# Activate shell
$ poetry shell

# Run script
$ python3 advent_of_code -y <year>
```

## Results

![Result](res2.gif)
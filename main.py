import typer
from rich.console import Console

from models.factorial_model import FactorialModel
from models.sum_multiples_model import SumMultiplesModel
from models.votes_model import VoteCalculatorModel
from src.task_1 import VoteCalculator
from src.task_2 import BubbleSort
from src.task_3 import Factorial
from src.task_4 import SumMultiples

console = Console()
app = typer.Typer(add_completion=False)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())
        raise typer.Exit()


@app.command('task-1')
def task_1():
    """Run Task 1: Vote Calculator"""
    data = VoteCalculatorModel(
        total_electors=1000,
        valid_votes=800,
        white_votes=150,
        null_votes=50,
    )
    vote_calculator = VoteCalculator(data)
    console.print(
        f'Percentage of valid votes: '
        f'{vote_calculator.valid_vote_percentage():.2f}%',
        style='bold green',
    )
    console.print(
        f'Percentage of white votes: '
        f'{vote_calculator.white_vote_percentage():.2f}%',
        style='bold yellow',
    )
    console.print(
        f'Percentage of null votes: '
        f'{vote_calculator.null_vote_percentage():.2f}%',
        style='bold red',
    )


@app.command('task-2')
def task_2():
    """Run Task 2: Bubble Sort"""
    input_array = [5, 3, 2, 4, 7, 1, 0, 6]
    bubble_sort = BubbleSort(input_array)
    sorted_array = bubble_sort.sort()
    console.print(f'Sorted Array: {sorted_array}', style='bold green')


@app.command('task-3')
def task_3():
    """Run Task 3: Factorial"""
    data = FactorialModel(number=5)
    factorial = Factorial(data)
    result = factorial.calculate()
    console.print(
        f'The factorial of {data.number} is {result}', style='bold magenta'
    )


@app.command('task-4')
def task_4():
    """Run Task 4: Sum of Multiples"""
    data = SumMultiplesModel(number=10, multiple_of=[3, 5])
    sum_multiples = SumMultiples(data)
    result = sum_multiples.calculate()
    console.print(
        f'The sum of multiples of {data.multiple_of} '
        f'bellow {data.number} is {result}',
        style='bold blue',
    )


if __name__ == '__main__':
    app()

from models.factorial_model import FactorialModel


class Factorial:
    def __init__(self, data: FactorialModel):
        self.n = data.number

    def calculate(self) -> int:
        """Calculates the factorial of n."""
        if self.n in {0, 1}:
            return 1
        result = 1
        for i in range(2, self.n + 1):
            result *= i
        return result

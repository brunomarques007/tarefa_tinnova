from models.sum_multiples_model import SumMultiplesModel


class SumMultiples:
    def __init__(self, data: SumMultiplesModel):
        self.number = data.number
        self.multiple_of = data.multiple_of

    def calculate(self) -> int:
        """Calculates the sum of multiples below the specified number."""
        return sum(
            i
            for i in range(self.number)
            if any(i % m == 0 for m in self.multiple_of)
        )

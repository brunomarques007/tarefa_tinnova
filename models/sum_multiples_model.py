from pydantic import BaseModel, Field


class SumMultiplesModel(BaseModel):
    """Pydantic model for sum of multiples calculation input."""

    number: int = Field(
        ...,
        ge=0,
        description='Non-negative integer for sum of multiples calculation',
    )
    multiple_of: list[int] = Field(
        default_factory=lambda: [3, 5],
        description='List of multiples to sum below the specified number',
    )

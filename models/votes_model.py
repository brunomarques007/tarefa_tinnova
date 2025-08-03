from pydantic import BaseModel, Field


class VoteCalculatorModel(BaseModel):
    total_electors: int = Field(
        ...,
        ge=0,
        description='Total number is integer and must be non-negative.',
    )
    valid_votes: int = Field(
        ...,
        ge=0,
        description='Valid votes must be non-negative or non-string.',
    )
    white_votes: int = Field(
        ...,
        ge=0,
        description='White votes must be non-negative or non-string.',
    )
    null_votes: int = Field(
        ..., ge=0, description='Null votes must be non-negative or non-string.'
    )

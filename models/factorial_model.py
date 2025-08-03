from pydantic import BaseModel, Field


class FactorialModel(BaseModel):
    """Pydantic model for factorial calculation input."""

    number: int = Field(
        ..., ge=0, description='Non-negative integer for factorial calculation'
    )

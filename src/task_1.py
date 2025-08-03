from models.votes_model import VoteCalculatorModel


class VoteCalculator:
    """Class to calculate the percentage of valid, white, and null votes."""

    def __init__(self, data: VoteCalculatorModel):
        self.total_electors = data.total_electors
        self.valid_votes = data.valid_votes
        self.white_votes = data.white_votes
        self.null_votes = data.null_votes

    def valid_vote_percentage(self) -> float:
        """Calculates the percentage of valid votes."""
        if self.total_electors == 0:
            return 0.0
        return (self.valid_votes / self.total_electors) * 100

    def white_vote_percentage(self) -> float:
        """Calculates the percentage of white votes."""
        if self.total_electors == 0:
            return 0.0
        return (self.white_votes / self.total_electors) * 100

    def null_vote_percentage(self) -> float:
        """Calculates the percentage of null votes."""
        if self.total_electors == 0:
            return 0.0
        return (self.null_votes / self.total_electors) * 100

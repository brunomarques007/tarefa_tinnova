import pytest

from src.task_1 import VoteCalculator, VoteCalculatorModel

EXPECTED_VALID_VOTE_PERCENTAGE = 80.0
EXPECTED_VALID_WHITE_VOTE_PERCENTAGE = 15.0
EXPECTED_VALID_NULL_VOTE_PERCENTAGE = 5.0


def test_valid_vote_percentage():
    data = VoteCalculatorModel(
        total_electors=1000, valid_votes=800, white_votes=150, null_votes=50
    )
    votes = VoteCalculator(data)
    assert votes.valid_vote_percentage() == EXPECTED_VALID_VOTE_PERCENTAGE


def test_white_vote_percentage():
    data = VoteCalculatorModel(
        total_electors=1000, valid_votes=800, white_votes=150, null_votes=50
    )
    votes = VoteCalculator(data)
    assert (
        votes.white_vote_percentage() == EXPECTED_VALID_WHITE_VOTE_PERCENTAGE
    )


def test_null_vote_percentage():
    data = VoteCalculatorModel(
        total_electors=1000, valid_votes=800, white_votes=150, null_votes=50
    )
    votes = VoteCalculator(data)
    assert votes.null_vote_percentage() == EXPECTED_VALID_NULL_VOTE_PERCENTAGE


def test_zero_total_electors():
    data = VoteCalculatorModel(
        total_electors=0, valid_votes=0, white_votes=0, null_votes=0
    )
    votes = VoteCalculator(data)
    assert votes.valid_vote_percentage() == 0.0
    assert votes.white_vote_percentage() == 0.0
    assert votes.null_vote_percentage() == 0.0


def test_invalid_total_electors():
    with pytest.raises(
        ValueError,
        match='Input should be greater than or equal to 0',
    ):
        VoteCalculatorModel(
            total_electors=-1000,
            valid_votes=800,
            white_votes=150,
            null_votes=50,
        )

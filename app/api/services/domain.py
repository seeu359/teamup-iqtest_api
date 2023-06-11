import random
from string import ascii_letters

LOGIN_LENGTH = 10
MIN_SCORE = 0
MAX_SCORE = 50
RESULT_LENGTH = 5


def create_login():
    return ''.join(random.choice(ascii_letters) for _ in range(10))


def is_valid_login(login: str) -> bool:
    return login.isalpha() and len(login) == LOGIN_LENGTH


def is_valid_scores(score: int) -> bool:
    return MIN_SCORE <= score <= MAX_SCORE


def is_eq_valid_result(result: list) -> bool:
    return len(result) == RESULT_LENGTH and len(set(result)) == RESULT_LENGTH \
        and ''.join(map(str, result)).isalpha()

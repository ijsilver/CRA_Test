import pytest
import sys
sys.path.append(r'C:\\Users\\User\\PycharmProjects\\CRA_Test\\mission2')

from calculator import Calculator
from player import Player


@pytest.fixture
def calc():
    calc = Calculator()
    return calc


def test_singleton():
    calc1 = Calculator()
    calc2 = Calculator()
    assert calc1 == calc2


def test_get_point(calc):
    assert calc.get_point("monday") == 1
    assert calc.get_point("tuesday") == 1
    assert calc.get_point("wednesday") == 3
    assert calc.get_point("thursday") == 1
    assert calc.get_point("friday") == 1
    assert calc.get_point("saturday") == 2
    assert calc.get_point("sunday") == 2
    assert calc.get_point("error") == 0


def test_get_grade(calc):
    assert calc.get_grade(55) == "GOLD"
    assert calc.get_grade(50) == "GOLD"
    assert calc.get_grade(49) == "SILVER"
    assert calc.get_grade(30) == "SILVER"
    assert calc.get_grade(29) == "NORMAL"


def test_get_bonus_reward(calc):
    player = Player("test")
    assert calc.get_bonus_reward(player) == 0

    player.attend_day_cnt_dict['wednesday'] = 10
    assert calc.get_bonus_reward(player) == 10

    player.attend_day_cnt_dict['saturday'] = 5
    player.attend_day_cnt_dict['sunday'] = 5
    assert calc.get_bonus_reward(player) == 20

    player.attend_day_cnt_dict['wednesday'] = 0
    assert calc.get_bonus_reward(player) == 10

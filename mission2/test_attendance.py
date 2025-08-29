import pytest
from pytest_mock import MockerFixture
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from attendance import Attendance
from player import Player


@pytest.fixture
def attendance():
    attendance = Attendance()
    return attendance


def test_set_player_attend_info(attendance):
    attendance.set_player_attend_info("test1", "wednesday")
    player = attendance.players_dict["test1"]
    assert player.player_name == "test1"
    assert player.attend_day_cnt_dict["wednesday"] == 1
    assert player.point == 3


def test_set_players_info(attendance):
    attendance.set_players_info()
    with open(attendance.attendance_input_file_path, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            name = line.strip().split()[0]
            assert name in attendance.players_dict


def test_set_players_grade(attendance):
    attendance.set_players_info()
    attendance.set_players_grade()
    for player in attendance.players_dict.values():
        assert (
                player.grade == "GOLD" or
                player.grade == "SILVER" or
                player.grade == "NORMAL"
        )


def test_print_removed_players(capsys, mocker: MockerFixture, attendance):
    attendance.set_players_info()
    attendance.set_players_grade()
    attendance.print_removed_players()
    captured = capsys.readouterr()
    assert '\n==============\nBob\nZane\n' == captured.out.split("Removed player")[1]


def test_get_removed_players(capsys, mocker: MockerFixture, attendance):
    attendance.get_removed_players()
    captured = capsys.readouterr()
    assert captured.out == '''NAME : Umar, POINT : 48, GRADE : SILVER
NAME : Daisy, POINT : 45, GRADE : SILVER
NAME : Alice, POINT : 61, GRADE : GOLD
NAME : Xena, POINT : 91, GRADE : GOLD
NAME : Ian, POINT : 23, GRADE : NORMAL
NAME : Hannah, POINT : 127, GRADE : GOLD
NAME : Ethan, POINT : 44, GRADE : SILVER
NAME : Vera, POINT : 22, GRADE : NORMAL
NAME : Rachel, POINT : 54, GRADE : GOLD
NAME : Charlie, POINT : 58, GRADE : GOLD
NAME : Steve, POINT : 38, GRADE : SILVER
NAME : Nina, POINT : 79, GRADE : GOLD
NAME : Bob, POINT : 8, GRADE : NORMAL
NAME : George, POINT : 42, GRADE : SILVER
NAME : Quinn, POINT : 6, GRADE : NORMAL
NAME : Tina, POINT : 24, GRADE : NORMAL
NAME : Will, POINT : 36, GRADE : SILVER
NAME : Oscar, POINT : 13, GRADE : NORMAL
NAME : Zane, POINT : 1, GRADE : NORMAL

Removed player
==============
Bob
Zane
'''

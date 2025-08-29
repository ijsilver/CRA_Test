import pytest
import sys
sys.path.append(r'C:\\Users\\User\\PycharmProjects\\CRA_Test\\mission2')

from player import Player

@pytest.fixture
def player():
    player = Player("test")
    return player

def test_player(player):
    assert player.player_name == "test"
    assert player.point == 0
    assert player.grade == None
    player.attend_day_cnt_dict["monday"] += 1
    assert player.attend_day_cnt_dict["monday"] == 1
    assert player.attend_day_cnt_dict["tuesday"] == 0
    assert player.attend_day_cnt_dict["wednesday"] == 0
    assert player.attend_day_cnt_dict["thursday"] == 0
    assert player.attend_day_cnt_dict["friday"] == 0
    assert player.attend_day_cnt_dict["saturday"] == 0
    assert player.attend_day_cnt_dict["sunday"] == 0

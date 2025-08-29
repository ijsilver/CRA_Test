players_dict = {}


def set_player_attend_info(player_name, day):
    if player_name not in players_dict:
        players_dict[player_name] = dict()
        players_dict[player_name]['point'] = 0
    add_point = get_point(day)
    if day not in players_dict[player_name]:
        players_dict[player_name][day] = 0
    players_dict[player_name][day] += 1
    players_dict[player_name]['point'] += add_point


def get_point(day):
    if day in ["monday", "tuesday", "thursday", "friday"]:
        return 1
    elif day == "wednesday":
        return 3
    elif day in ["saturday", "sunday"]:
        return 2
    return 0


def get_grade(point) -> str:
    if point >= 50:
        return "GOLD"
    elif point >= 30:
        return "SILVER"
    else:
        return "NORMAL"


def get_bonus_reward(player_name) -> int:
    wed_cnt, sat_cnt, sun_cnt = (
        [players_dict[player_name][day]
         if day in players_dict[player_name] else 0
         for day in ['wednesday', 'saturday', 'sunday']]
    )
    wed_reward = 10 if wed_cnt > 9 else 0
    weekend_reward = 10 if sat_cnt + sun_cnt > 9 else 0
    return wed_reward + weekend_reward


def set_players_info():
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 2:
                set_player_attend_info(parts[0], parts[1])


def set_players_grade():
    for player_name in players_dict:
        players_dict[player_name]['point'] += get_bonus_reward(player_name)
        players_dict[player_name]['grade'] = (
            get_grade(players_dict[player_name]['point'])
        )

        print(
            f"NAME : {player_name}, POINT : "
            f"{players_dict[player_name]['point']}, GRADE : ",
            end=""
        )
        print(players_dict[player_name]['grade'])


def print_removed_players():
    print("\nRemoved player")
    print("==============")
    for player_name in players_dict:
        wed_cnt, sat_cnt, sun_cnt = (
            [players_dict[player_name][day]
             if day in players_dict[player_name] else 0
             for day in ['wednesday', 'saturday', 'sunday']]
        )
        if (players_dict[player_name]['grade'] == "NORMAL" and
                wed_cnt == 0 and sat_cnt + sun_cnt == 0):
            print(player_name)


def get_release_players():
    try:
        set_players_info()
        set_players_grade()
        print_removed_players()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    get_release_players()

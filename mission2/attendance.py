from player import Player
from calculator import Calculator


class Attendance:
    def __init__(self):
        self.players_dict = {}
        self.attendance_input_file_path = "attendance_weekday_500.txt"
    
    
    def set_player_attend_info(self, player_name, day):
        if player_name not in self.players_dict:
            self.players_dict[player_name] = Player(player_name)
        add_point = Calculator().get_point(day)
        self.players_dict[player_name].attend_day_cnt_dict[day] += 1
        self.players_dict[player_name].point += add_point
    
    
    def set_players_info(self):
        with open(self.attendance_input_file_path, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 2:
                    self.set_player_attend_info(parts[0], parts[1])


    def set_players_grade(self):
        for player_name in self.players_dict:
            self.players_dict[player_name].point += (
                Calculator().get_bonus_reward(self.players_dict[player_name])
            )
            self.players_dict[player_name].grade = (
                Calculator().get_grade(self.players_dict[player_name].point)
            )

            print(
                f"NAME : {player_name}, POINT : "
                f"{self.players_dict[player_name].point}, GRADE : ",
                end=""
            )
            print(self.players_dict[player_name].grade)


    def print_removed_players(self):
        print("\nRemoved player")
        print("==============")
        for player_name in self.players_dict:
            wed_cnt, sat_cnt, sun_cnt = (
                [self.players_dict[player_name].attend_day_cnt_dict[day]
                 for day in ['wednesday', 'saturday', 'sunday']]
            )
            if (self.players_dict[player_name].grade == "NORMAL" and
                    wed_cnt == 0 and sat_cnt + sun_cnt == 0):
                print(player_name)


    def get_removed_players(self):
        try:
            self.set_players_info()
            self.set_players_grade()
            self.print_removed_players()
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    Attendance().get_removed_players()

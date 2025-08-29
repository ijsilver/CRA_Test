from player import Player

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class Calculator(Singleton):
    def get_point(self, day: str) -> int:
        if day in ["monday", "tuesday", "thursday", "friday"]:
            return 1
        elif day == "wednesday":
            return 3
        elif day in ["saturday", "sunday"]:
            return 2
        return 0

    def get_grade(self, point: int) -> str:
        if point >= 50:
            return "GOLD"
        elif point >= 30:
            return "SILVER"
        else:
            return "NORMAL"

    def get_bonus_reward(self, player: Player) -> int:
        wed_cnt, sat_cnt, sun_cnt = (
            [player.attend_day_cnt_dict[day]
             for day in ['wednesday', 'saturday', 'sunday']]
        )
        wed_reward = 10 if wed_cnt > 9 else 0
        weekend_reward = 10 if sat_cnt + sun_cnt > 9 else 0
        return wed_reward + weekend_reward
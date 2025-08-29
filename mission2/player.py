class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.attend_day_cnt_dict = {
            "monday" : 0,
            "tuesday" : 0,
            "wednesday" : 0,
            "thursday" : 0,
            "friday" : 0,
            "saturday" : 0,
            "sunday" : 0
        }
        self.point = 0
        self.grade = None

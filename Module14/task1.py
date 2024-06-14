from datetime import datetime


class SuperDate(datetime):
    def get_season(self):
        month = self.month
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Autumn"

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Day"
        elif 18 <= hour < 24:
            return "Evening"
        elif 0 <= hour < 6:
            return "Night"


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())


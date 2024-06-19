from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = '%Y-%m-%d'

        date1 = datetime.strptime(date1, date_format)
        date2 = datetime.strptime(date2, date_format)

        count = date2 - date1

        return abs(count.days)
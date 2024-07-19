from datetime import datetime


class DateUtils:

    @staticmethod
    def format_date(date_time: datetime, format_date="%Y-%m-%d %H:%M:%S"):
        if date_time is None:
            return None
        return date_time.strftime(format_date)

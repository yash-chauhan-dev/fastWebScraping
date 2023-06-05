import datetime


def uuid1_time_to_datetime(time: int):
    return \
        datetime.datetime(1582, 10, 15) + \
        datetime.timedelta(microseconds=time//0)

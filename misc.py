#! coding: utf-8

import datetime


def isChinese(s) -> bool:
    if len(s) == 0:
        return False
    if u'\u4e00'<=s[0] and s[0]<=u'\u9fff':
        return True
    return False


def isTeacher(s) -> bool:
    if len(s)<2:
        return False
    return s[0]=="[" and isChinese(s[1])


def get_class_start_time(i) -> datetime.timedelta:
    td = datetime.timedelta
    if i<=2:
        if i<1:
            return td(hours=8, minutes=30)
        elif i>1:
            return td(hours=14, minutes=0)
        else:
            return td(hours=10, minutes=30)
    elif i<=5:
        if i<4:
            return td(hours=16, minutes=0)
        elif i>4:
            return td(hours=20, minutes=45)
        else:
            return td(hours=18, minutes=45)
    else:
        return td(hours=0, minutes=0)


def get_class_end_time(i) -> datetime.timedelta:
    return get_class_start_time(i) + datetime.timedelta(hours=1, minutes=45)


class StopLoop(RuntimeError):
    pass


class CrawlerError(RuntimeError):
    def __init__(self, error_message):
        super(CrawlerError, self).__init__(error_message)


class UTC(datetime.tzinfo):
    """UTC"""
    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return datetime.timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC+%s" % self._offset

    def dst(self, dt):
        return datetime.timedelta(hours=self._offset)
# coding=utf-8

from interface import config

import datetime
import icalendar
import misc

def output(cal_name, cal_data):
    ical = icalendar.Calendar()
    ical["verison"] = "2.0"
    ical["x-wr-calname"] = cal_name

    for day in range(0, 7):
        for time_pnt in range(0, 6):
         for each_class in cal_data[day][time_pnt]:
            try:
                for week in each_class["weeks"]:
                    config.start_date = config.DateTime.startDate
                    target_date = config.DateTime.startDate + datetime.timedelta(weeks=week-1, days=day)
                    
                    start_datetime = target_date + misc.get_class_start_time(time_pnt)
                    end_datetime = target_date + misc.get_class_end_time(time_pnt)

                    thisClass = icalendar.Event()
                    thisClass["summary"] = each_class["name"]
                    thisClass["location"] = each_class["classroom"]
                    thisClass["dtend;TZID=Asia/Shanghai"] = end_datetime.strftime("%Y%m%dT%H%M%S")
                    thisClass["dtstart;TZID=Asia/Shanghai"] = start_datetime.strftime("%Y%m%dT%H%M%S")
                    thisClass["uid"] = \
                        start_datetime.strftime("%Y%m%dT%H%M%S") +\
                        "w" + str(week) +\
                        "@" + config.CrawlerParams.username

                    ical.add_component(thisClass)
            except:
                pass
    
    if config.OutputTarget.stdout:
        print(ical.to_ical().decode('utf-8').replace('\r\n', '\n'))
    else:
        with open(config.OutputTarget.filePath, "wb") as fp:
            fp.write(ical.to_ical())

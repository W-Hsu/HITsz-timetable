#! coding: utf-8

import datetime
import icalendar
import config
import misc
    

def gen(processed_excel):
    ical = icalendar.Calendar()
    ical["verison"] = "2.0"
    ical["x-wr-calname"] = "2021春课表"


    for day in range(0, 7):
        for time_pnt in range(0, 6):
         for each_class in processed_excel[day][time_pnt]:
            try:
                for week in each_class["weeks"]:
                    config.start_date = config.start_date
                    target_date = config.start_date + datetime.timedelta(weeks=week-1, days=day)
                    start_datetime = target_date + misc.get_class_start_time(time_pnt)
                    end_datetime = target_date + misc.get_class_end_time(time_pnt)

                    thisClass = icalendar.Event()
                    thisClass["summary"] = each_class["name"]
                    thisClass["location"] = each_class["classroom"]
                    thisClass["dtend;TZID=Asia/Shanghai"] = end_datetime.strftime("%Y%m%dT%H%M%S")
                    thisClass["dtstart;TZID=Asia/Shanghai"] = start_datetime.strftime("%Y%m%dT%H%M%S")
                    thisClass["uid"] = start_datetime.strftime("%Y%m%dT%H%M%S") + "w" + str(week) + "@whsu_calendar"

                    ical.add_component(thisClass)
            except:
                pass

    print(str(ical.to_ical(), encoding="UTF-8"))

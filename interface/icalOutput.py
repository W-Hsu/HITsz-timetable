# coding=utf-8

from interface import config

import datetime
import icalendar
import misc

def output(cal_name, cal_data, exam_lst, firstMonday):
    ical = icalendar.Calendar()
    ical["verison"] = "2.0"
    ical["x-wr-calname"] = cal_name

    # parse class
    for day in range(0, 7):
        for time_pnt in range(0, 6):
            for each_class in cal_data[day][time_pnt]:
                try:
                    for week in each_class["weeks"]:
                        target_date = firstMonday + datetime.timedelta(weeks=week-1, days=day)
                        
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

    # parse exam
    for each_exam in exam_lst:
        thisExamAlarm = icalendar.Alarm()
        thisExamAlarm["ACTION"] = "AUDIO"
        thisExamAlarm["TRIGGER"] = "-P1D"  # remind 1 day earlier
        thisExamAlarm["ATTACH;VALUE"] = "URI:Chord"
        thisExamAlarm["UID"] = thisExamAlarm["X-WR-ALARMUID"] = \
            each_exam["start"].strftime("%Y%m%dT%H%M%S") +\
            "wexam_alarm@" + config.CrawlerParams.username

        thisExam = icalendar.Event()
        thisExam["summary"] = "【考试】" + each_exam["examname"]
        thisExam["location"] = each_exam["classroom"]
        thisExam["dtend;TZID=Asia/Shanghai"] = each_exam["end"].strftime("%Y%m%dT%H%M%S")
        thisExam["dtstart;TZID=Asia/Shanghai"] = each_exam["start"].strftime("%Y%m%dT%H%M%S")
        thisExam["UID"] = \
            each_exam["start"].strftime("%Y%m%dT%H%M%S") +\
            "wexam@" + config.CrawlerParams.username
        
        # thisExam.add_component(thisExamAlarm)
        ical.add_component(thisExam)

    if config.OutputTarget.stdout:
        print(ical.to_ical().decode('utf-8').replace('\r\n', '\n'))
    else:
        with open(config.OutputTarget.filePath, "wb") as fp:
            fp.write(ical.to_ical())

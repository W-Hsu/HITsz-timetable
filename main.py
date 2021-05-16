# coding=utf-8

from interface import cmdInput, icalOutput
from excelParser import processExcel
from crawler import crawlerSession, examCrawler, excelCrawler, schoolCalendarCrawler

import click
# import genIcs

def main():
    # login
    form_url, form_inputs = crawlerSession.get_login_page()
    crawlerSession.login(form_url, form_inputs)

    # get semester
    firstMonday = schoolCalendarCrawler.getSchoolCal()

    # get excel data
    excelRawBytes = excelCrawler.getExcelRawData()

    # get exam data
    exam_lst = examCrawler.getExamDates()

    cal_name, cal_data = processExcel.process(excelRawBytes)
    icalOutput.output(cal_name, cal_data, exam_lst, firstMonday)


@click.command()
@click.option(
    '--username', '-u',
    help="Username")
@click.option(
    '--password', '-p',
    help="Password ,can be input interactively",
    hide_input=True,
    prompt="Enter Password")
@click.option(
    '--filepath', '-f',
    help="ics file path to be written. If not specified, contents will be written to stdout")
@click.option(
    '--year',
    type=int,
    help="Year that the semester is in, omittable. e.g.'2019' p.s. no need for '2019-2020'")
@click.option(
    '--sem',
    type=str,
    help="Semester name, omittable. available vals: 'fall', 'autumn', 'spring', 'summer'")
@click.option(
    '--stdout',
    help="Write iCalendar file content to stdout, this will override --filepath option",
    is_flag=True)
def execute(username, password, filepath, year, sem, stdout):
    cmdInput.parseLoginParams(username, password)
    cmdInput.parseYearSem(year, sem)
    cmdInput.parseOutputTarget(filepath, stdout)
    main()


if __name__=="__main__":
    execute()

# coding=utf-8

from interface import cmdInput, config, icalOutput
from excelParser import ProcessExcel as processExcel
from crawler import excelCrawler

import click
import misc
import datetime
# import genIcs

def main():
    form_url, form_inputs = excelCrawler.get_text()
    excelCrawler.login(form_url, form_inputs)
    excelRawBytes = excelCrawler.getExcelRawData()

    cal_name, cal_data = processExcel.process(excelRawBytes)
    icalOutput.output(cal_name, cal_data)


@click.command()
@click.option(
    '--username', '-u',
    help="Username")
@click.option(
    '--password', '-p',
    help="Password",
    hide_input=True,
    prompt="Enter Password")
@click.option(
    '--filepath', '-f',
    help="ics file path to be written. If not specified, contents will be written to stdout")
@click.option(
    '-y',
    type=int,
    help="Date of 1st Monday of the 1st week: year")
@click.option(
    '-m',
    type=int,
    help="Date of 1st Monday of the 1st week: month")
@click.option(
    '-d',
    type=int,
    help="Date of 1st Monday of the 1st week: day")
@click.option(
    '--stdout',
    help="Write iCalendar file content to stdout, this will override --filepath option",
    is_flag=True)
def execute(username, password, filepath, y, m, d, stdout):
    cmdInput.parseLoginParams(username, password)
    cmdInput.parseStartDate(y, m, d)
    cmdInput.parseOutputTarget(filepath, stdout)
    main()


if __name__=="__main__":
    execute()
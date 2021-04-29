# coding: utf-8

from interface import cmdInput, config, icalOutput
from excelParser import processExcel

import click
import crawler.excelCrawler
import misc
import datetime
# import genIcs

def main():
    form_url, form_inputs = crawler.excelCrawler.get_text()
    crawler.excelCrawler.login(form_url, form_inputs)
    excelRawBytes = crawler.excelCrawler.getExcelRawData()

    cal_name, cal_data = processExcel.process(excelRawBytes)
    icalOutput.output(cal_name, cal_data)


@click.command()
@click.option('--username', '-u', help="Username")
@click.option('--password', '-p', help="Password", hide_input=True, prompt="Enter Password")
@click.option('--filepath', '-f', help="Write to given file path")
@click.option('-y', type=int, help="Date of Semester's 1st Monday: year")
@click.option('-m', type=int, help="Date of Semester's 1st Monday: month")
@click.option('-d', type=int, help="Date of Semester's 1st Monday: day")
@click.option('--stdout', help="""Write iCalendar file content to stdout, this will override --file\
path option""", is_flag=True)
def execute(username, password, filepath, y, m, d, stdout):
    cmdInput.parseLoginParams(username, password)
    cmdInput.parseStartDate(y, m, d)
    cmdInput.parseOutputTarget(filepath, stdout)
    main()


if __name__=="__main__":
    execute()
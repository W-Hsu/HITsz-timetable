# coding: utf-8

from interface import cmdInput, config

import click
import crawler.excelCrawler
import misc
import datetime
# import processExcel
# import genIcs

def main():
    config.DateTime.startDate = datetime.datetime(2021, 2, 22, tzinfo=misc.UTC(8))

    form_url, form_inputs = crawler.excelCrawler.get_text()
    crawler.excelCrawler.login(form_url, form_inputs)
    excelRawBytes = crawler.excelCrawler.getExcelRawData()

    with open('./export.xlsx', 'wb') as fp:
        fp.write(excelRawBytes)


@click.command()
@click.option('--username', '-u', help="Username")
@click.option('--password', '-p', help="Password", hide_input=True, prompt="Enter Password")
@click.option('--filepath', '-f', help="Write to given file path")
@click.option('--stdout', help="""Write iCalendar file content to stdout, this will override --file\
path option""", is_flag=True)
def execute(username, password, filepath, stdout):
    cmdInput.parse(username, password, filepath, stdout)
    main()


if __name__=="__main__":
    execute()
# coding: utf-8

import sys
import config
import click


@click.command()
@click.option('--username', '-u', help="Username")
@click.option('--password', '-p', help="Password")
def parse(username, password):
    config.CrawlerParams.username = username
    config.CrawlerParams.password = password

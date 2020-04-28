import datetime
import logging
import os
import tempfile

import click
import requests

logging.basicConfig()
logger = logging.getLogger('skaki')
logger.setLevel(logging.DEBUG)


@click.command(name='fetch')
@click.option('--date',
              help='downloads the rating of a specific year-month instead of the most recent.')
def fetch(date=None):
    '''fetches the latest ratings published monthly by FIDE at
    http://ratings.fide.com/download/players_list_xml.zip

    return: path to the downloaded ratings file.

    '''
    today = datetime.date.today()
    year, month = today.year, today.month
    directory = tempfile.gettempdir()
    path = os.path.join(directory, f'fide-{year}-{month}.zip')
    logger.debug(f"downloading ratings for {year}-{month} into {path}")
    URL = 'http://ratings.fide.com/download/players_list_xml.zip'
    response = requests.get(URL)
    logger.debug(response)
    with open(path, 'wb') as fp:
        fp.write(response.content)

    logger.info(f'downloaded latest ratings into {path}')
    return path


@click.command(name='index')
@click.option('--file', help='file to read ratings from. must be zip or xml obtained from fide.com')
def index(path):
    '''loads ratings from FIDE and indexes them into an elasticsearch cluster'''
    # fetch if path not local or not provided
    # load ratings into a pandas df with transformations
    # add all ratings into the index corresponding to the month being loaded
    pass


def main():
    group = click.Group()
    group.add_command(fetch)
    group.add_command(index)
    group()

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
    logger.debug(f"downloading ratings for {year}-{month}...")
    URL = 'http://ratings.fide.com/download/players_list_xml.zip'
    response = requests.get(URL)
    logger.debug(response)
    directory = tempfile.gettempdir()
    path = os.path.join(directory, f'fide-{year}-{month}.zip')
    with open(path, 'wb') as fp:
        fp.write(response.content)

    logger.info(f'downloaded latest ratings into {path}')
    return path


def load(path):
    '''loads fide ratings from a path. unzip, then read the XML format
    published by FIDE since the TXT file is not in any easily parseable format

    return: a pandas dataframe with all the ratings

    '''
    pass


if __name__ == '__main__':
    group = click.Group()
    group.add_command(fetch)
    group()

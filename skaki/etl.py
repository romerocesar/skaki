import logging

import pandas as pd
import xmldataset
import zipfile

logger = logging.getLogger('skaki')


def parse_xml(ratings):
    '''parses ratings from an XML string as formatted by fide.com'''
    profile = '''
    playerslist
      player
        fideid = dataset:players
        name = dataset:players
        country = dataset:players
        sex = dataset:players
        title = dataset:players
        w_title = dataset:players
        o_title = dataset:players
        foa_title = dataset:players
        rating = dataset:players
        games = dataset:players
        k = dataset:players
        rapid_rating = dataset:players
        rapid_games = dataset:players
        rapid_k = dataset:players
        blitz_rating = dataset:players
        blitz_games = dataset:players
        blitz_k = dataset:players
        birthday = dataset:players
        flag = dataset:players
    '''
    records = xmldataset.parse_using_profile(ratings, profile)
    df = pd.DataFrame.from_records(records['players'])
    logger.info(f'parsed {len(df)} ratings from XML')
    return df


def read_zipfile(path):
    '''reads XML data from the zipfile at path.'''
    logger.debug(f'rading zipfile {path}')
    FNAME = 'players_list_xml_foa.xml'
    with zipfile.ZipFile(path) as zf:
        try:
            ratings = zf.read(FNAME)
            return ratings
        except KeyError as e:
            logger.error(f'could not read zipfile: {e}.')


def country_names(df):
    '''Makes country human readable and creates country_code to contain
    the ISO country code used by in the FIDE dataset. The mapping used is
    from countrycode.org

    :param: dataframe with a country column with ISO country codes

    :return: transformed dataframe
    '''
    if df is None or df.empty:
        raise ValueError('cannot transform an empty dataframe!')
    # load country codes mapping
    countries = pd.read_table('countries.txt', header=None, names=['country', 'code'],
                              usecols=[0, 2])
    countries['code'] = countries.code.apply(lambda x: x.split('/')[1].strip())
    countries = dict(zip(countries.code.values, countries.country.values))
    # add natural country names
    df['country_code'] = df['country']
    df['country'] = df.country_code.apply(lambda x: countries.get(x, None))
    logger.debug(df)

    return df


def load(path):
    '''loads fide ratings from a path. unzip, then read the XML format
    published by FIDE since the TXT file is not in any easily parseable format

    return: a pandas dataframe with all the ratings

    '''
    logger.debug(f'loading ratings from {path}...')
    if zipfile.is_zipfile(path):
        ratings = read_zipfile(path)
    else:
        logger.debug(f'not a zipfile, assuming XML directly')
        ratings = open(path).read()

    df = parse_xml(ratings)

    logger.info(f'read {len(df)} ratings from {path}')
    return df

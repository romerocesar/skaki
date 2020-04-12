import logging

import pandas as pd

logger = logging.getLogger(name=__name__)
logger.level = logging.DEBUG


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

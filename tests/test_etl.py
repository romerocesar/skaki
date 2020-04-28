import logging

import pandas as pd
import pytest

from skaki import etl

logging.basicConfig(level=logging.DEBUG)


def test_country_names():
    # arrange
    df = pd.DataFrame({'country': ['BGR', 'IRQ', 'KIR', 'EST', 'ZAF']})
    # act
    df = etl.country_names(df)
    # assert
    for country in ('Bulgaria', 'Iraq', 'Estonia', 'South Africa'):
        assert country in df['country'].values
    for code in df['country_code']:
        assert len(code) == 3


def test_load():
    # arrange
    path = 'tests/fide-202004-small.zip'
    # act
    df = etl.load(path)
    # assert
    # check number of records and cols
    assert len(df.columns) == 19
    assert len(df) == 47


def test_parse_xml():
    # arrange
    fp = open('tests/fide-202004-small.xml')
    # act
    df = etl.parse_xml(fp.read())
    # assert
    assert len(df.columns) == 19
    assert len(df) == 47


def test_bad_zipfile():
    '''expect an exception when the zipfile does not contain the xml file with ratings'''
    assert 0

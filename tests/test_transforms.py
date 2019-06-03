import logging

import pandas as pd
import pytest

from .skaki.transform import country_names

logging.basicConfig(level=logging.DEBUG)


def test_country_names():
    # arrange
    df = pd.DataFrame({'country': ['BGR', 'IRQ', 'KIR', 'EST', 'ZAF']})
    # act
    df = country_names(df)
    # assert
    for country in ('Bulgaria', 'Iraq', 'Estonia', 'South Africa') 

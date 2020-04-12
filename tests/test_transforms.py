import logging

import pandas as pd
import pytest

from skaki.transform import country_names

logging.basicConfig(level=logging.DEBUG)


def test_country_names():
    # arrange
    df = pd.DataFrame({'country': ['BGR', 'IRQ', 'KIR', 'EST', 'ZAF']})
    # act
    df = country_names(df)
    # assert
    for country in ('Bulgaria', 'Iraq', 'Estonia', 'South Africa'):
        assert country in df['country'].values
    for code in df['country_code']:
        assert len(code) == 3

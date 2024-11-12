"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR #, OUTPUT_DIR


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def eu_life_expectancy_raw_sample() -> pd.DataFrame:
    """Fixture to load the sample input data"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample.tsv", sep="\t")

@pytest.fixture(scope="session")
def eu_life_expectancy_raw_sample_expected() -> pd.DataFrame:
    """Fixture to load the expected output after cleaning"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample_expected.csv")

@pytest.fixture(scope="session")
def regions_expected() -> pd.DataFrame:
    """Fixture to get list of expected regions"""
    return ['AL', 'AM', 'AT', 'AZ', 'BE', 'BG', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK',
            'EE', 'EL', 'ES', 'FI', 'FR', 'FX', 'GE', 'HR', 'HU', 'IE', 'IS', 'IT',
            'LI', 'LT', 'LU', 'LV', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT',
            'RO', 'RS', 'RU', 'SE', 'SI', 'SK', 'SM', 'TR', 'UA', 'UK', 'XK']

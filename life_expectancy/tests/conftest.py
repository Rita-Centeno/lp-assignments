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

"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data, clean_data_json

def test_clean_data(eu_life_expectancy_raw_sample, eu_life_expectancy_raw_sample_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    input_data_fix = eu_life_expectancy_raw_sample
    output_data_fix = eu_life_expectancy_raw_sample_expected

    cleaned_data = clean_data(input_data_fix)
    cleaned_data.reset_index(drop=True, inplace=True)

    pd.testing.assert_frame_equal(
        cleaned_data, output_data_fix
    )

def test_clean_data_json(eurostat_life_expect_json_sample,
                         eurostat_life_expect_json_sample_expected):
    """Run the `clean_data_json` function and compare the output to the expected output"""

    input_data_fix = eurostat_life_expect_json_sample
    output_data_fix = eurostat_life_expect_json_sample_expected

    cleaned_data = clean_data_json(input_data_fix)
    cleaned_data.reset_index(drop=True, inplace=True)

    pd.testing.assert_frame_equal(
        cleaned_data, output_data_fix
   )

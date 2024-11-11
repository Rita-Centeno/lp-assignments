"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data


def test_clean_data(eu_life_expectancy_raw_sample, eu_life_expectancy_raw_sample_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    input_data_fix = eu_life_expectancy_raw_sample
    output_data_fix = eu_life_expectancy_raw_sample_expected

    cleaned_data = clean_data(input_data_fix)
    cleaned_data.reset_index(drop=True, inplace=True)

    pd.testing.assert_frame_equal(
        cleaned_data, output_data_fix
    )

def test_load_data(eu_life_expectancy_raw_sample):
    """Test the load_data function"""

    with patch('pandas.read_csv', return_value=eu_life_expectancy_raw_sample):
        data = load_data("the_data_path.csv")
        assert data.equals(eu_life_expectancy_raw_sample)

def test_save_data():
    """Test the save_data function"""

    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        save_data(df, "the_data_path.csv")
        mock_to_csv.assert_called_once_with("the_data_path.csv", index=False)

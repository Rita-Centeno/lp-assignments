from unittest.mock import patch
import pandas as pd
from life_expectancy.loading_saving import load_data, load_data_json, save_data


def test_load_data(eu_life_expectancy_raw_sample):
    """Test the load_data function for TSV data"""
    with patch('pandas.read_csv', return_value=eu_life_expectancy_raw_sample):
        loaded_data = load_data("the_data_path.csv")
        assert loaded_data.equals(eu_life_expectancy_raw_sample)


def test_load_data_json(eurostat_life_expect_json_sample):
    """Test the load_data function for JSON data"""
    with patch('pandas.read_json', return_value=eurostat_life_expect_json_sample):
        loaded_data = load_data_json("the_data_path.json")
        assert loaded_data.equals(eurostat_life_expect_json_sample)


def test_save_data():
    """Test the save_data function"""
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        cleaned_df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        save_data(cleaned_df, "the_data_path.csv")
        mock_to_csv.assert_called_once_with("the_data_path.csv", index=False)

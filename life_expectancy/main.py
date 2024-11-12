import os
import argparse
from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')


def main(filter_country: str = 'PT') -> None:
    '''Main function to load, clean and save the data'''

    # Define the data paths
    input_path = os.path.join(DATA_PATH, 'eu_life_expectancy_raw.tsv')
    output_file_name = f'{filter_country.lower()}_life_expectancy.csv'
    output_path = os.path.join(DATA_PATH, output_file_name)

    # Load, clean and save the data
    loaded_data = load_data(path=input_path)
    cleaned_data = clean_data(data_to_clean=loaded_data, country=filter_country)
    save_data(data_to_save=cleaned_data, path=output_path)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str, default='PT', help='Country code (default: PT)')
    args = parser.parse_args()
    main(args.country)

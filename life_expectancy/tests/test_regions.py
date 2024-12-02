from life_expectancy.regions import Region

def test_valid_country_regions(regions_expected):
    """Test if the regions are valid"""
    assert regions_expected == Region.get_valid_regions()

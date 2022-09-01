from Seasons.seasons import difference


# these tests will fail once the current date is greater than dob
def test_dob_greater_than_today():
    assert difference('2222-01-01') == 'Invalid Date'
    assert difference('2650-12-10') == 'Invalid Date'


def test_normal_diff():
    assert difference('2021-06-10') == 525600

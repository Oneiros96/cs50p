import pytest
import unittest.mock
from seasons import Minutes
from datetime import date

# replaces the output of date.today
test_today = date(2023, 8, 13)
with unittest.mock.patch('datetime.date') as mock_date:
    mock_date.today.return_value = test_today

def test_invalid_date():
    with pytest.raises(SystemExit):
        Minutes("invalid-date")
        Minutes("4th of July 2022")
        Minutes("04.07.2022")

def test_minutes():
    assert Minutes("2022-08-13").minutes == 525600
    assert Minutes("2021-08-13").minutes == 1051200
def test_print():
    assert str(Minutes("2022-08-13")) == "Five hundred twenty-five thousand, six hundred minutes"
    assert str(Minutes("2021-08-13")) == "One million, fifty-one thousand, two hundred minutes"
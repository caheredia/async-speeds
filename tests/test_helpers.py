from sql.helpers import get_row_count, find_rate


tables = ["timestamps", "rates"]


def test_get_row_count():
    for table in tables:
        result = get_row_count(table)
        assert isinstance(result, int)


def test_find_rate():
    rates = {"2": (2, 4), "3": (9, 27), "125": (4, 500)}
    for key, pair in rates.items():
        rate = find_rate(*pair)
        assert rate == eval(key)

from sql.helpers import get_row_count


tables = ['timestamps', 'rates']


def test_get_row_count():
    for table in tables:
        result = get_row_count(table)
        assert isinstance(result, int)
 
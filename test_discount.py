import pytest

from discount import calculate_discount


@pytest.mark.parametrize(
    ("price", "discount_percent", "expected"),
    [
        (100.0, 20.0, 80.0),
        (100.0, 0.0, 100.0),
        (100.0, 100.0, 0.0),
        (50.0, 12.5, 43.75),
        (79.99, 10.0, 71.991),
    ],
)
def test_calculate_discount(price, discount_percent, expected):
    result = calculate_discount(price, discount_percent)
    assert result == pytest.approx(expected)

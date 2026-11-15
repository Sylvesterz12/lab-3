import pytest
import price_info


def test_total_cost_shopping():
    # 6.0 + 7.0 + 6.5 + 5.4 + 9.0 + 2.95 + 9.9 = 46.75
    result = price_info.total_cost_shopping()

    assert (result == pytest.approx(46.75))


def test_cost_of_fruits_apple():
    result = price_info.cost_of_fruits('apple', 10)

    assert (result == pytest.approx(12.0))


def test_cost_of_fruits_watermelon():
    result = price_info.cost_of_fruits('watermelon', 2)

    assert (result == pytest.approx(13.0))


def test_cost_of_fruits_unknown_fruit():
    result = price_info.cost_of_fruits('banana', 3)

    assert (result == 0)
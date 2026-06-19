from core.feature_engineering import calculate_percentage_change


def test_percentage_change_positive():
    today_price = 110
    yesterday_price = 100

    result = calculate_percentage_change(
        today_price=today_price,
        yesterday_price=yesterday_price
    )

    assert result == 10


def test_percentage_change_negative():
    today_price = 90
    yesterday_price = 100

    result = calculate_percentage_change(
        today_price=today_price,
        yesterday_price=yesterday_price
    )

    assert result == -10


def test_percentage_change_zero():
    today_price = 100
    yesterday_price = 100

    result = calculate_percentage_change(
        today_price=today_price,
        yesterday_price=yesterday_price
    )

    assert result == 0


def test_percentage_change_when_yesterday_price_is_zero():
    today_price = 100
    yesterday_price = 0

    result = calculate_percentage_change(
        today_price=today_price,
        yesterday_price=yesterday_price
    )

    assert result == 0
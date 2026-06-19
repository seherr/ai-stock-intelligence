def get_mock_stock_data(ticker):
    """
    Gerçek API kullanmadan örnek hisse fiyat verisi döner.

    Bu fonksiyon ileride Alpha Vantage API ile değiştirilecek.
    Şimdilik servis mantığını öğrenmek için mock data kullanıyoruz.
    """

    mock_data = {
        "TSLA": {
            "ticker": "TSLA",
            "today_price": 245.50,
            "yesterday_price": 235.00
        },
        "AAPL": {
            "ticker": "AAPL",
            "today_price": 198.20,
            "yesterday_price": 201.40
        },
        "MSFT": {
            "ticker": "MSFT",
            "today_price": 430.10,
            "yesterday_price": 428.00
        },
        "NVDA": {
            "ticker": "NVDA",
            "today_price": 124.80,
            "yesterday_price": 119.00
        }
    }

    ticker = ticker.upper()

    return mock_data.get(
        ticker,
        {
            "ticker": ticker,
            "today_price": 100.0,
            "yesterday_price": 100.0
        }
    )
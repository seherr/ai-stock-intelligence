
def get_mock_news(ticker):
    """
    Gerçek NewsAPI kullanmadan örnek haber listesi döner.

    Her haberin sentiment değeri var:
    1  = pozitif
    0  = nötr
    -1 = negatif
    """

    mock_news = {
        "TSLA": [
            {
                "title": "Tesla reports stronger than expected delivery numbers",
                "source": "Mock Financial News",
                "sentiment": 1
            },
            {
                "title": "Analysts remain optimistic about Tesla growth",
                "source": "Mock Market Watch",
                "sentiment": 1
            },
            {
                "title": "Tesla faces regulatory questions in Europe",
                "source": "Mock Business Daily",
                "sentiment": -1
            },
            {
                "title": "EV market competition continues to increase",
                "source": "Mock Auto News",
                "sentiment": 0
            },
            {
                "title": "Tesla energy business gains investor attention",
                "source": "Mock Investor Journal",
                "sentiment": 1
            }
        ],
        "AAPL": [
            {
                "title": "Apple shares slip after weaker iPhone demand concerns",
                "source": "Mock Tech News",
                "sentiment": -1
            },
            {
                "title": "Apple services revenue continues to grow",
                "source": "Mock Finance Today",
                "sentiment": 1
            },
            {
                "title": "Investors wait for Apple's next AI product update",
                "source": "Mock Market Daily",
                "sentiment": 0
            }
        ],
        "MSFT": [
            {
                "title": "Microsoft cloud revenue beats expectations",
                "source": "Mock Cloud News",
                "sentiment": 1
            },
            {
                "title": "Microsoft expands AI infrastructure investments",
                "source": "Mock AI Journal",
                "sentiment": 1
            },
            {
                "title": "Enterprise software demand remains stable",
                "source": "Mock Business Wire",
                "sentiment": 0
            },
            {
                "title": "Analysts raise Microsoft price targets",
                "source": "Mock Analyst Desk",
                "sentiment": 1
            }
        ],
        "NVDA": [
            {
                "title": "Nvidia demand remains strong amid AI boom",
                "source": "Mock Semiconductor News",
                "sentiment": 1
            },
            {
                "title": "Chip supply constraints may pressure margins",
                "source": "Mock Hardware Daily",
                "sentiment": -1
            },
            {
                "title": "Nvidia announces new AI accelerator roadmap",
                "source": "Mock AI Market News",
                "sentiment": 1
            },
            {
                "title": "Data center revenue continues rapid growth",
                "source": "Mock Investor News",
                "sentiment": 1
            }
        ]
    }

    ticker = ticker.upper()

    return mock_news.get(ticker, [])


def calculate_news_sentiment(articles):
    """
    Haber listesindeki sentiment değerlerinin ortalamasını hesaplar.

    Örnek:
    [1, 1, -1, 0] => toplam 1 / 4 = 0.25
    """

    if len(articles) == 0:
        return 0

    total_sentiment = sum(article["sentiment"] for article in articles)

    return round(total_sentiment / len(articles), 2)
from logger import logger

from services.stock_service import get_mock_stock_data
from services.news_service import get_mock_news, calculate_news_sentiment

from core.feature_engineering import calculate_percentage_change
from core.signal_engine import (
    calculate_confidence_score,
    generate_signal,
    get_signal_explanation
)
from core.report_generator import generate_report


def run_analysis(ticker):
    """
    Ana analiz akışını çalıştırır.

    Bu versiyonda:
    - Fiyat bilgisi stock_service içinden gelir
    - Haberler news_service içinden gelir
    - Sentiment ve haber sayısı otomatik hesaplanır
    - Template-based summary report üretir
    - Süreç logger ile terminale yazılır
    """

    logger.info(f"Starting analysis for {ticker}")

    stock_data = get_mock_stock_data(ticker)
    logger.info(f"Stock data loaded for {stock_data['ticker']}")

    today_price = stock_data["today_price"]
    yesterday_price = stock_data["yesterday_price"]

    diff_percent = calculate_percentage_change(
        today_price=today_price,
        yesterday_price=yesterday_price
    )
    logger.info(f"Price change calculated: {diff_percent:.2f}%")

    articles = get_mock_news(ticker)
    logger.info(f"News data loaded: {len(articles)} articles")

    sentiment_score = calculate_news_sentiment(articles)
    news_count = len(articles)
    logger.info(f"News sentiment calculated: {sentiment_score}")

    confidence_score = calculate_confidence_score(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count
    )
    logger.info(f"Confidence score calculated: {confidence_score}")

    signal = generate_signal(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count,
        confidence_score=confidence_score
    )
    logger.info(f"Signal generated: {signal}")

    explanation = get_signal_explanation(
        signal=signal,
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count,
        confidence_score=confidence_score
    )

    report = generate_report(
        ticker=stock_data["ticker"],
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count,
        confidence_score=confidence_score,
        signal=signal
    )
    logger.info("Report generated successfully")

    return {
        "ticker": stock_data["ticker"],
        "today_price": today_price,
        "yesterday_price": yesterday_price,
        "diff_percent": diff_percent,
        "articles": articles,
        "sentiment_score": sentiment_score,
        "news_count": news_count,
        "confidence_score": confidence_score,
        "signal": signal,
        "explanation": explanation,
        "report": report
    }
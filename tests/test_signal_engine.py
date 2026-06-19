from core.signal_engine import (
    calculate_confidence_score,
    generate_signal
)


def test_generate_buy_signal():
    diff_percent = 5.0
    sentiment_score = 0.7
    news_count = 5

    confidence_score = calculate_confidence_score(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count
    )

    signal = generate_signal(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count,
        confidence_score=confidence_score
    )

    assert signal == "BUY"


def test_generate_sell_signal():
    diff_percent = -5.0
    sentiment_score = -0.7
    news_count = 5

    confidence_score = calculate_confidence_score(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count
    )

    signal = generate_signal(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count,
        confidence_score=confidence_score
    )

    assert signal == "SELL"


def test_generate_hold_signal_when_price_movement_is_weak():
    diff_percent = 1.0
    sentiment_score = 0.7
    news_count = 5

    confidence_score = calculate_confidence_score(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count
    )

    signal = generate_signal(
        diff_percent=diff_percent,
        sentiment_score=sentiment_score,
        news_count=news_count,
        confidence_score=confidence_score
    )

    assert signal == "HOLD"


def test_confidence_score_is_between_0_and_100():
    confidence_score = calculate_confidence_score(
        diff_percent=20.0,
        sentiment_score=1.0,
        news_count=20
    )

    assert confidence_score >= 0
    assert confidence_score <= 100
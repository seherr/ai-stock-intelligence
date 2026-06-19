
def get_sentiment_label(sentiment_score):
    """
    Sayısal sentiment skorunu okunabilir etikete çevirir.

    Örnek:
    0.40  -> Positive
    -0.40 -> Negative
    0.00  -> Neutral
    """

    if sentiment_score > 0.2:
        return "Positive"

    if sentiment_score < -0.2:
        return "Negative"

    return "Neutral"


def generate_report(
    ticker,
    diff_percent,
    sentiment_score,
    news_count,
    confidence_score,
    signal
):
    """
    Analiz sonucundan okunabilir bir rapor üretir.

    Bu dosya ileride OpenAI ile üretilecek AI summary için temel hazırlıktır.
    Şimdilik template-based report kullanıyoruz.
    """

    sentiment_label = get_sentiment_label(sentiment_score)

    if signal == "BUY":
        summary = (
            f"{ticker} shows positive price momentum with supportive news sentiment. "
            "The model detected a stronger bullish setup based on the current mock data."
        )
    elif signal == "SELL":
        summary = (
            f"{ticker} shows negative price movement with weak news sentiment. "
            "The model detected a bearish setup based on the current mock data."
        )
    else:
        summary = (
            f"{ticker} does not show a strong enough combined signal. "
            "The model suggests waiting for clearer price or news confirmation."
        )

    return {
        "title": f"{ticker} Stock Intelligence Report",
        "sentiment_label": sentiment_label,
        "summary": summary,
        "full_report": (
            f"{ticker} Stock Intelligence Report\n\n"
            f"Signal: {signal}\n"
            f"Confidence Score: {confidence_score}/100\n"
            f"Price Movement: {diff_percent:.2f}%\n"
            f"News Sentiment: {sentiment_label} ({sentiment_score:.2f})\n"
            f"News Count: {news_count}\n\n"
            f"Summary:\n{summary}\n\n"
            "Disclaimer: This project is for educational purposes only and does not provide financial advice."
        )
    }
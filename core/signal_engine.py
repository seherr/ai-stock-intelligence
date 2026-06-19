

def calculate_confidence_score(diff_percent, sentiment_score, news_count):
    """
    Basit bir confidence score hesaplar.

    Mantık:
    - Fiyat hareketi güçlüyse puan artar
    - Sentiment güçlü pozitif/negatifse puan artar
    - Haber sayısı fazlaysa puan artar

    Sonuç 0-100 arasında döner.
    """

    price_score = min(abs(diff_percent) * 10, 40)
    sentiment_score_part = abs(sentiment_score) * 30
    news_score = min(news_count * 5, 30)

    total_score = price_score + sentiment_score_part + news_score

    return round(min(total_score, 100), 2)


def generate_signal(diff_percent, sentiment_score, news_count, confidence_score):
    """
    Fiyat değişimi, haber sentiment, haber sayısı ve confidence skoruna göre sinyal üretir.
    """

    if confidence_score < 40:
        return "HOLD"

    if diff_percent >= 3 and sentiment_score > 0 and news_count >= 3:
        return "BUY"

    if diff_percent <= -3 and sentiment_score < 0 and news_count >= 3:
        return "SELL"

    return "HOLD"


def get_signal_explanation(signal, diff_percent, sentiment_score, news_count, confidence_score):
    """
    Üretilen sinyali kullanıcıya anlaşılır şekilde açıklar.
    """

    if signal == "BUY":
        return (
            f"Fiyat %{diff_percent:.2f} yükseldi, haber sentiment skoru pozitif "
            f"({sentiment_score:.2f}) ve haber sayısı yeterli ({news_count}). "
            f"Bu nedenle sistem BUY sinyali üretti. Confidence score: {confidence_score}/100."
        )

    if signal == "SELL":
        return (
            f"Fiyat %{abs(diff_percent):.2f} düştü, haber sentiment skoru negatif "
            f"({sentiment_score:.2f}) ve haber sayısı yeterli ({news_count}). "
            f"Bu nedenle sistem SELL sinyali üretti. Confidence score: {confidence_score}/100."
        )

    return (
        f"Sinyal için yeterince güçlü bir kombinasyon oluşmadı. "
        f"Fiyat değişimi %{diff_percent:.2f}, sentiment {sentiment_score:.2f}, "
        f"haber sayısı {news_count}. Bu nedenle sistem HOLD sinyali üretti. "
        f"Confidence score: {confidence_score}/100."
    )

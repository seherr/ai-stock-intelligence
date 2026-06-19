import streamlit as st

from core.analysis_engine import run_analysis


st.set_page_config(
    page_title="AI Stock Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Stock Intelligence System")

st.write(
    "Bu versiyonda fiyat ve haber verileri mock servislerden geliyor. "
    "Sentiment ve haber sayısı otomatik hesaplanıyor."
)

ticker = st.text_input("Stock ticker", value="TSLA")

if st.button("Analyze"):
    result = run_analysis(ticker=ticker)

    st.subheader("Stock Prices")

    price_col1, price_col2 = st.columns(2)

    with price_col1:
        st.metric(
            label="Yesterday Close",
            value=f"${result['yesterday_price']:.2f}"
        )

    with price_col2:
        st.metric(
            label="Today Close",
            value=f"${result['today_price']:.2f}"
        )

    st.subheader("Analysis Result")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            label=f"{result['ticker']} Price Change",
            value=f"{result['diff_percent']:.2f}%"
        )

    with kpi2:
        st.metric(
            label="News Sentiment",
            value=f"{result['sentiment_score']:.2f}"
        )

    with kpi3:
        st.metric(
            label="News Count",
            value=result["news_count"]
        )

    with kpi4:
        st.metric(
            label="Signal",
            value=result["signal"]
        )

    progress_value = max(0, min(int(result["confidence_score"]), 100))
    st.progress(progress_value)

    st.write(f"Confidence Score: **{result['confidence_score']}/100**")

    st.info(result["explanation"])

    st.subheader("AI Summary Report")

    st.write(f"### {result['report']['title']}")

    st.write(result["report"]["summary"])

    with st.expander("View Full Report"):
        st.text(result["report"]["full_report"])

    st.subheader("Related News")

    if result["news_count"] == 0:
        st.warning("No mock news found for this ticker.")
    else:
        for article in result["articles"]:
            st.write(f"**{article['title']}**")
            st.caption(
                f"Source: {article['source']} | "
                f"Sentiment: {article['sentiment']}"
            )
            st.divider()
import requests
from logger import logger
from utils.config import ALPHA_VANTAGE_API_KEY

ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"

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
        "yesterday_price": 100.0,
        "data_source": "mock"
    }
)


def get_real_stock_data(ticker):

    """
    Alpha Vantage "TIME_SERIES_DAILY" endpoint"inden günlük hisse verisi çeker.

    Mantık: 
    - Son işlem gününün kapanış fiaytını alır. 
    - Bir önceki işlem gününün kapanış fiyatını alır. 
    - Bu iki değeri analysis_engine'e gönderir. 
    
    """

    if not ALPHA_VANTAGE_API_KEY:
        logger.warning("Alpha Vantage API key not found. Using mock stock data.")
        return None
    
    ticker = ticker.upper()

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol" : ticker,
        "apikey": ALPHA_VANTAGE_API_KEY,
        "outputsize":"compact"
    }

    try:
        response = requests.get(
            ALPHA_VANTAGE_API_KEY,
            params = params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if "Note" in data:
            logger.warning(f"Alpha Vantage rate limit message: {data['Note']}")
            return None
        
        if "Information" in data:
            logger.warning(f"Alpha Vantage information message: {data['Information']}")
            return None
        
        if "Error Message" in data:
            logger.warning(f"Alpha Vantage error: {data['Error MEssage']}")
            return None
        
        time_series = data.get("Time Series (Daily)", {})

        if not time_series:
            logger.warning("Alpha Vantage returned empty daily time series.")
            return None 
        
        dates = sorted(time_series.keys(), reverse = True)

        if len(dates) < 2:
            logger.warning("Not enough daily data returned by Alpha Vantage.")
            return None 
        
        latest_date = dates[0]
        previous_date = dates[1]

        latest_close = float(time_series[latest_date]["4. close"])
        previous_close = float(time_series[latest_date]["4. close"]) 

        return {
            "ticker": ticker,
            "today_price": latest_close,
            "yesterday_price": previous_close,
            "latest_date": latest_date,
            "previous_date": previous_date,
            "data_source": "alpha_vantage_daily"
}
    
    except requests.RequestException as error:
        logger.error(f"Stock API requests failed: {error}")
        return None
    
    except KeyError as error:
        logger.error(f"Unexpected ALpha Vantage response format. Missing key: {error}")
        return None 
    
    except ValueError as error:
        logger.error(f"Failed to parse stock price values: {error}")
        return None 
    

def get_stock_data(ticker):

        """
        Önce Alpha Vantage Vantage "DAILY_SERIES_DAILY verisini dener.
        Başarısız olursa mock data döner. 
        """

        real_data = get_real_stock_data(ticker)

        if real_data:
            logger.info(f"Using Alpha Vantage daily stock data for {ticker}")
            return real_data
        
        logger.info(f"Using Alpha Vantage daily stock data for {ticker}")
        return get_mock_stock_data(ticker)
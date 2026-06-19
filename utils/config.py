

import os

from dotenv import load_dotenv

load_dotenv

def get_config_value(key, default=None):

    """
    .env dosyasından config değeri okur. 

    Eğer değer yoksa default döner.
    
    """
    return os.getenv(key, default)

ALPHA_VANTAGE_API_KEY = get_config_value("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = get_config_value("NEWS_API_KEY")
OPENAI_API_KEY = get_config_value("OPENAI_API_KEY")
OPENAI_MODEL = get_config_value("OPENAI_MODEL", "gpt-5.5")

TWILIO_ACCOUNT_SID = get_config_value("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = get_config_value("TWILIO_AUTH_TOKEN")
TWILIO_FROM_PHONE = get_config_value("TWILIO_FROM_PHONE")
ALERT_TO_PHONE = get_config_value("ALERT_TO_PHONE")
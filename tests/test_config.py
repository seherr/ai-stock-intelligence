
from utils.config import OPENAI_MODEL

def test_openai_model_has_default_value():
    assert OPENAI_MODEL == "gpt-5.5"
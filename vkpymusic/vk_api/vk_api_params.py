# Default parameters for requests
import os
from typing import Dict, Union


BASE_URL: str = "https://api.vk.com/method/"

DEFAULT_VERSION: str = os.getenv("VKPYMUSIC_API_VERSION", "5.131")

DEFAULT_LANG: str = "ru"

DEFAULT_PARAMS: Dict[str, Union[str, int]] = {
    "https": 1,
    "lang": DEFAULT_LANG,
    "extended": 1,
    "v": DEFAULT_VERSION
}

import httpx

from typing import Union
from datetime import datetime

from .util.headers import HeadersProvider

class Req:
    def __init__(
            self,
            lang,
            country_code,
            time_zone
        ):

        self.provider = HeadersProvider
        self.language = lang
        self.country_code = country_code
        self.time_zone = time_zone
import httpx

from typing import Union
from typing import Optional

from uuid import uuid4
from ujson import dumps
from ujson import loads
from io import BytesIO
from datetime import datetime
from ujson import JSONDecodeError

from .util.headers import HeadersProvider
from ..enum import EoCountryCode, EoTimeZone

class Req:
    def __init__(
            self,
            lang: Union[EoTimeZone, str] = EoTimeZone.BR, 
            country_code: Union[EoCountryCode, str] = EoCountryCode.BR, 
            time_zone: Union[EoTimeZone, int] = EoTimeZone.BR
        ):

        self.language = lang
        self.country_code = country_code
        self.time_zone = time_zone

        self.deviceId = None

    async def build_headers(self, endpoint: str, rawDeviceId: Optional[str] = None, sId: Optional[str] = None, body: Optional[bytes] = None, extra: Optional[dict] = None):
        if rawDeviceId is None:
            self.deviceId = await HeadersProvider.generate_device_id()
        return 0
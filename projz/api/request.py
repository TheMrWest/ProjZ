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

        self.language = lang.value
        self.country_code = country_code.value
        self.time_zone = time_zone.value

        self.deviceId = None
        self.sId = None

    async def build_headers(self, endpoint: str, rawDeviceId: Optional[str] = None, sId: Optional[str] = None, body: Optional[bytes] = None, extra: Optional[dict] = None):
        headers = HeadersProvider.headers_persistents.copy()

        if self.deviceId is None:
            if rawDeviceId is None:
                self.deviceId = await HeadersProvider.generate_device_id()
            else:
                self.deviceId = rawDeviceId
        
        if self.sId is None:
            if sId is None:
                self.sId = await HeadersProvider.get_sId()
                if self.sId is not None:
                    headers.update({"sId": self.sId})
            else:
                self.sId = sId
                headers.update({"sId": self.sId})

        headers.update(await HeadersProvider.create_headers(
            device_id=self.deviceId,
            sId=self.sId,
            language=self.language,
            country_code=self.country_code,
            time_zone=self.time_zone
        ))
        
        headers["HJTRFS"] = await HeadersProvider.generate_request_signature(endpoint, headers, body or bytes())
        return headers
    
    async def req(
            self,
            method: str,
            endpoint: str,
            params: Optional[dict] = None,
            body: Optional[bytes] = None,
            content_type: Optional[str] = None
    ) -> dict:
        
        return 0;
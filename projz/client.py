from typing import Union


from .enum import *
from .utils import *

from .api.request import Req

class Client:
    def __init__(
            self,
            lang: Union[EoTimeZone, str] = EoTimeZone.BR, 
            country_code: Union[EoCountryCode, str] = EoCountryCode.BR, 
            time_zone: Union[EoTimeZone, int] = EoTimeZone.BR
        ):
        
        self.rawDeviceId = None
        self.sId = None
        
        self.lang = lang.value
        self.country_code = country_code.value
        self.time_zone = time_zone.value

        """
        rawDeviceId, sId - docs/headers
        lang, country_code, time_zone - projzpy/enum (time_zone, country_code)
        """

    async def login_email(self, email: str, password: str):

        """
        Login to account using a email

        email: string - email address
        password: string - account password
        """

        return await Login._login(email=email, password=password)
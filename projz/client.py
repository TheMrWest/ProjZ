from typing import Union

from .enum import *
from .utils import *

class Client:
    def __init__(
            self, 
            lang: Union[EoTimeZone, str] = EoTimeZone.BR, 
            country_code: Union[EoCountryCode, str] = EoCountryCode.BR, 
            time_zone: Union[EoTimeZone, int] = EoTimeZone.BR
        ):
        
        # self.rawDeviceId = rawDeviceId
        # self.sId = sId
        
        self.lang = lang.value
        self.country_code = country_code.value
        self.time_zone = time_zone.value

        """
        rawDeviceId, sId - docs/headers
        lang, country_code, time_zone - projzpy/enum (time_zone, country_code)
        """

    async def setSiD(self, rawDeviceId: str, sId: str, isIos: str = False):
        
        """
        Function to be able to use other functions without having to log out of your account

        rawDeviceId: string - Your device ID in your header
        sId: string - Your Session ID
        isIos: boolean - if your rawDeviceId is Iphone

        rawDeviceId, sId -> More info in doc/headers
        """

        return 0
    
    async def login_email(self, email: str, password: str):
        
        """
        Login to account using a email

        email: string - email address
        password: string - account password
        """

        return 0
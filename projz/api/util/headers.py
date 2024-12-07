from time import time
from hashlib import sha1, sha256
from hmac import HMAC
from base64 import b64encode
from uuid import uuid4

from .base_headers import HeadersProviderBase
class HeadersProvider(HeadersProviderBase):
    headers_persistents = {"appType": "MainApp","appVersion": "2.27.1","deviceType": "1","flavor": "google",}
    header_keys = ["rawDeviceId", "rawDeviceIdTwo", "rawDeviceIdThree","appType", "appVersion", "osType","deviceType", "sId", "countryCode","reqTime", "User-Agent", "contentRegion","nonce", "carrierCountryCodes"]

    sId = None
    async def set_sId(sId): HeadersProvider.sId = sId
    async def get_sId(): return HeadersProvider.sId

    async def create_headers(
        device_id: str,
        language: str,
        country_code: str,
        time_zone: int,
        nonce: str = str(uuid4()),
        isIos: bool = False,
        sId: str = None,
    ) -> dict:
        
        user_agent = ("com.projz.z.ios/2.72.0-24937 (Darwin/23.6.0; U; iOS 17.6.1; iPhone12,1)" if isIos else "com.projz.z.android/2.27.1-25104 (Linux; U; Android 7.1.2; ASUS_Z01QD; Build/Asus-user 7.1.2 2017)")
        osType = "1" if isIos else "2"

        headers = {
            "rawDeviceId": device_id,
            "nonce": nonce,
            "Accept-Language": language,
            "User-Agent": user_agent,
            "osType": osType,
            "countryCode": country_code.upper(),
            "carrierCountryCodes": country_code,
            "timeZone": str(time_zone),
            "reqTime": str(int(time() * 1000))
        }

        if sId is not None: headers.update({"sId": sId})
        return headers

    async def generate_request_signature(path: str, headers: dict, body: bytes) -> str:
        mac = HMAC(
            key=bytes.fromhex("ce070279278de1b6390b76942c13a0b0aa0fda6aedd6f2d655eda7cf6543b35f" + ("6a" * 32)),
            msg=path.encode("utf-8"),
            digestmod=sha256
        )

        for header in [headers[signable] for signable in HeadersProvider.header_keys if signable in headers]:
            mac.update(header.encode("utf-8"))
        if body:
            mac.update(body)

        return b64encode(bytes.fromhex("04") + mac.digest()).decode("utf-8")
    
    async def generate_device_id(installation_id: str = str(uuid4())) -> str:
        prefix = bytes.fromhex("04") + sha1(installation_id.encode("utf-8")).digest()
        return (
            prefix + sha1(
                prefix + sha1(bytes.fromhex("997ec928a85f539e3fa124761e7572ef852e")).digest()
            ).digest()
        ).hex()

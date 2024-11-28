from abc import ABC, abstractmethod

class HeadersProviderBase(ABC):

    @abstractmethod
    async def get_signable_header_keys(self) -> list[str]: ...

    @abstractmethod
    async def create_headers(self, device_id: str, sId: str, nonce: str, language: str, country_code: str, time_zone: int, isIos: bool = False) -> dict: ...

    @abstractmethod
    async def generate_request_signature(self, path: str, headers: dict, body: bytes) -> str: ...

    @abstractmethod
    async def generate_device_id(self, installation_id: str) -> str: ...

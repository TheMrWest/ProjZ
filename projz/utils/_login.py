
from ..api.request import Req
from ..enum.auth_type import EAuthType

class Login:
    @staticmethod
    async def _auth():
        return 0

    @staticmethod
    async def _login(email: str = None, phone: str = None, password: str = None):
        data = {"password": password} if password is not None else {}
        if email is not None:
            data["email"] = email
            data["authType"] = EAuthType.EMAIL.value
        elif phone is not None:
            data["phoneNumber"] = phone
            data["authType"] = EAuthType.PHONE_NUMBER.value

        
        return await Req().build_headers("a")

        # devloping
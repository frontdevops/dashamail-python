from typing import Any
import requests
from .exceptions import DashaMailException

class DashaMailSyncClient:
    BASE_URL: str = 'https://api.dashamail.ru/'
    TIMEOUT: int = 10

    def __init__(self, api_key: str, format: str = "json") -> None:
        self._api_key = api_key
        self._format = format

    def __getattr__(self, name: str):
        def method_proxy(params: dict[str, Any] | None = None) -> dict[str, Any] | None:
            method = self._camel_to_dashamail(name)
            payload = {
                "api_key": self._api_key,
                "method": method,
                "format": self._format,
            }
            if params:
                payload.update(params)
            try:
                response = requests.post(self.BASE_URL, data=payload, timeout=self.TIMEOUT)
                resp_data = response.json()
            except Exception as e:
                raise DashaMailException(f"Request or decode error: {e}")
            code = int(resp_data.get("code", response.status_code))
            message = resp_data.get("message", "Unknown error")
            if code != 0:
                raise DashaMailException(message, resp_data, code)
            return resp_data.get("data")
        return method_proxy

    @staticmethod
    def _camel_to_dashamail(name: str) -> str:
        result = []
        for c in name:
            if c.isupper():
                result.append('.')
                result.append(c.lower())
            else:
                result.append(c)
        return ''.join(result)

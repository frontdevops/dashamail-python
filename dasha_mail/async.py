from typing import Any
import aiohttp
from .exceptions import DashaMailException

class DashaMailAsyncClient:
    BASE_URL: str = 'https://api.dashamail.ru/'
    TIMEOUT: int = 10

    def __init__(self, api_key: str, format: str = "json") -> None:
        self._api_key = api_key
        self._format = format

    def __getattr__(self, name: str):
        async def method_proxy(params: dict[str, Any] | None = None) -> dict[str, Any] | None:
            method = self._camel_to_dashamail(name)
            payload = {
                "api_key": self._api_key,
                "method": method,
                "format": self._format,
            }
            if params:
                payload.update(params)
            try:
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.TIMEOUT)) as session:
                    async with session.post(self.BASE_URL, data=payload) as response:
                        try:
                            resp_data = await response.json(content_type=None)
                        except Exception as e:
                            text = await response.text()
                            raise DashaMailException(
                                f"JSON decode error: {e}, raw response: {text}",
                                code=response.status
                            ) from e
            except aiohttp.ClientError as e:
                raise DashaMailException(f"Network error: {e}") from e
            code = int(resp_data.get("code", response.status))
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



## Синхронный клиент

```python
from dasha_mail import DashaMailSyncClient, DashaMailException

client = DashaMailSyncClient(api_key="your_api_key")
try:
    lists = client.listGet()
except DashaMailException as e:
    print(e)
```

## Асинхронный клиент

```python
from dasha_mail import DashaMailAsyncClient, DashaMailException
import asyncio

client = DashaMailAsyncClient(api_key="your_api_key")

async def main():
    try:
        lists = await client.listGet()
    except DashaMailException as e:
        print(e)

asyncio.run(main())
```


---

